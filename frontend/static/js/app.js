// ================================
// 1. Get references to HTML elements
// ================================

const workoutForm = document.getElementById('workout-form');
const generateBtn = document.getElementById('generate-btn');
const resultsSection = document.getElementById('results');
const workoutSummary = document.getElementById('workout-summary');
const exerciseList = document.getElementById('exercise-list');
const newWorkoutBtn = document.getElementById('new-workout-btn');
const durationSlider = document.getElementById('duration');
const durationValue = document.getElementById('duration-value');

// ================================
// 2. Update duration display when slider moves
// ================================

durationSlider.addEventListener('input', function() {
    durationValue.textContent = this.value;
});

// ================================
// 3. Handle form submission
// ================================

workoutForm.addEventListener('submit', async function(event) {
    // Prevent the page from refreshing
    event.preventDefault();

    // Show loading state
    generateBtn.classList.add('loading');

    // Gather form data
    const formData = {
        workout_type: document.getElementById('workout-type').value,
        difficulty: document.getElementById('difficulty').value,
        duration: parseInt(durationSlider.value)
    };

    // Get selected muscle groups (checkboxes)
    const muscleCheckboxes = document.querySelectorAll('input[name="target_muscles"]:checked');
    if (muscleCheckboxes.length > 0) {
        formData.target_muscles = Array.from(muscleCheckboxes).map(cb => cb.value);
    }

    try {
        // Send request to our API
        const response = await fetch('/api/generate-workout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        // Check if request was successful
        if (!response.ok) {
            throw new Error('Failed to generate workout');
        }

        // Parse the JSON response
        const workout = await response.json();

        // Display the workout
        displayWorkout(workout);

    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        // Remove loading state
        generateBtn.classList.remove('loading');
    }
});

// ================================
// 4. Display workout results
// ================================

function displayWorkout(workout) {
    // Show the results section
    resultsSection.classList.remove('hidden');

    // Create summary HTML
    workoutSummary.innerHTML = `
        <p><strong>Workout Type:</strong> ${workout.workout_type}</p>
        <p><strong>Difficulty:</strong> ${workout.difficulty}</p>
        <p><strong>Duration:</strong> ${workout.estimated_duration} minutes</p>
        <p><strong>Exercises:</strong> ${workout.total_exercises}</p>
        <p><strong>Estimated Calories:</strong> ${workout.calories_estimate}</p>
    `;

    // Clear previous exercises
    exerciseList.innerHTML = '';

    // Create a card for each exercise
    workout.exercises.forEach(function(exercise) {
        const card = document.createElement('div');
        card.className = 'exercise-card';

        // Build the details section
        let details = `<span>${exercise.sets} sets</span>`;
        if (exercise.reps) {
            details += `<span>${exercise.reps} reps</span>`;
        }
        if (exercise.duration) {
            details += `<span>${exercise.duration} seconds</span>`;
        }
        details += `<span>${exercise.rest}s rest</span>`;

        // Build the card HTML
        card.innerHTML = `
            <h3>${exercise.name}</h3>
            <div class="exercise-details">${details}</div>
            <p>${exercise.instructions}</p>
            ${exercise.equipment ? `<p><strong>Equipment:</strong> ${exercise.equipment}</p>` : ''}
        `;

        exerciseList.appendChild(card);
    });

    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

// ================================
// 5. Generate another workout button
// ================================

newWorkoutBtn.addEventListener('click', function() {
    // Hide results
    resultsSection.classList.add('hidden');

    // Scroll back to form
    workoutForm.scrollIntoView({ behavior: 'smooth' });
});
