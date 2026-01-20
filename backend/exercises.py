from .models import MuscleGroup, DifficultyLevel


EXERCISE_DATABASE = [
    # CHEST EXERCISES
    {
        "name": "Push-ups",
        "muscle_group": MuscleGroup.CHEST,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 10,
        "rest": 60,
        "instructions": "Start in plank position with hands shoulder-width apart. Lower your body until chest nearly touches the floor, then push back up.",
        "equipment": None
    },
    {
        "name": "Diamond Push-ups",
        "muscle_group": MuscleGroup.CHEST,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Form a diamond shape with your hands under your chest. Lower down and push back up, keeping elbows close to body.",
        "equipment": None
    },
    {
        "name": "Dumbbell Bench Press",
        "muscle_group": MuscleGroup.CHEST,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": 10,
        "rest": 90,
        "instructions": "Lie on bench with dumbbells at chest level. Press weights up until arms are extended, then lower with control.",
        "equipment": "Dumbbells, Bench"
    },
    # BACK EXERCISES
    {
        "name": "Bodyweight Rows",
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 10,
        "rest": 60,
        "instructions": "Hang from a bar or rings at waist height. Pull your chest to the bar, squeezing shoulder blades together.",
        "equipment": "Pull-up bar or rings"
    },
    {
        "name": "Pull-ups",
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 8,
        "rest": 90,
        "instructions": "Hang from bar with palms facing away. Pull yourself up until chin is over the bar, then lower with control.",
        "equipment": "Pull-up bar"
    },
    {
        "name": "Dumbbell Rows",
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Place one knee and hand on bench. Row dumbbell to hip, squeezing shoulder blade at top.",
        "equipment": "Dumbbell, Bench"
    },
    # LEG EXERCISES
    {
        "name": "Bodyweight Squats",
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 15,
        "rest": 60,
        "instructions": "Stand with feet shoulder-width apart. Lower your hips back and down until thighs are parallel to floor, then stand back up.",
        "equipment": None
    },
    {
        "name": "Lunges",
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Step forward with one leg, lowering until both knees are at 90 degrees. Push back to start and alternate legs.",
        "equipment": None
    },
    {
        "name": "Goblet Squats",
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": 12,
        "rest": 90,
        "instructions": "Hold dumbbell at chest level. Squat down keeping chest up and weight in heels, then drive back up.",
        "equipment": "Dumbbell"
    },
    # SHOULDER EXERCISES
    {
        "name": "Pike Push-ups",
        "muscle_group": MuscleGroup.SHOULDERS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 10,
        "rest": 60,
        "instructions": "Start in downward dog position with hips high. Bend elbows to lower head toward floor, then push back up.",
        "equipment": None
    },
    {
        "name": "Dumbbell Shoulder Press",
        "muscle_group": MuscleGroup.SHOULDERS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 10,
        "rest": 90,
        "instructions": "Hold dumbbells at shoulder height. Press weights overhead until arms are extended, then lower with control.",
        "equipment": "Dumbbells"
    },
    {
        "name": "Lateral Raises",
        "muscle_group": MuscleGroup.SHOULDERS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Hold dumbbells at sides. Raise arms out to sides until parallel with floor, then lower slowly.",
        "equipment": "Dumbbells"
    },
    # ARM EXERCISES
    {
        "name": "Bicep Curls",
        "muscle_group": MuscleGroup.ARMS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Hold dumbbells at sides with palms facing forward. Curl weights to shoulders, then lower with control.",
        "equipment": "Dumbbells"
    },
    {
        "name": "Tricep Dips",
        "muscle_group": MuscleGroup.ARMS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 10,
        "rest": 60,
        "instructions": "Place hands on bench behind you. Lower body by bending elbows to 90 degrees, then push back up.",
        "equipment": "Bench or chair"
    },
    {
        "name": "Hammer Curls",
        "muscle_group": MuscleGroup.ARMS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Hold dumbbells with palms facing each other. Curl weights to shoulders keeping palms facing in.",
        "equipment": "Dumbbells"
    },
    # CORE EXERCISES
    {
        "name": "Plank",
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": None,
        "duration": 30,
        "rest": 45,
        "instructions": "Hold body in straight line from head to heels, resting on forearms and toes. Keep core tight.",
        "equipment": None
    },
    {
        "name": "Crunches",
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 15,
        "rest": 45,
        "instructions": "Lie on back with knees bent. Curl shoulders off floor toward knees, then lower with control.",
        "equipment": None
    },
    {
        "name": "Mountain Climbers",
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": None,
        "duration": 30,
        "rest": 45,
        "instructions": "Start in push-up position. Drive knees toward chest alternately in a running motion.",
        "equipment": None
    },
    # FULL BODY EXERCISES
    {
        "name": "Burpees",
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 10,
        "rest": 60,
        "instructions": "From standing, drop to push-up position, perform push-up, jump feet to hands, then jump up with arms overhead.",
        "equipment": None
    },
    {
        "name": "Jumping Jacks",
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": None,
        "duration": 45,
        "rest": 30,
        "instructions": "Jump feet out wide while raising arms overhead, then jump back to start position. Repeat continuously.",
        "equipment": None
    },
    {
        "name": "Thrusters",
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 4,
        "reps": 10,
        "rest": 90,
        "instructions": "Hold dumbbells at shoulders. Squat down, then drive up explosively and press weights overhead in one motion.",
        "equipment": "Dumbbells"
    }
]


