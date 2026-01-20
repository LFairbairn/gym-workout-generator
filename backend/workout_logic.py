import random
import uuid
from typing import List, Optional
from .models import (
    WorkoutRequest, WorkoutResponse, Exercise,
    MuscleGroup, DifficultyLevel, WorkoutType
)
from .exercises import EXERCISE_DATABASE


def filter_exercises(
    difficulty: DifficultyLevel,
    target_muscles: Optional[List[MuscleGroup]] = None
) -> List[dict]:
    """Filter exercises based on difficulty and target muscles."""
    filtered = []
    
    for exercise in EXERCISE_DATABASE:
        # Check difficulty - include exercises at or below requested level
        difficulty_order = [DifficultyLevel.BEGINNER, DifficultyLevel.INTERMEDIATE, DifficultyLevel.ADVANCED]
        exercise_level = difficulty_order.index(exercise["difficulty"])
        requested_level = difficulty_order.index(difficulty)
        
        if exercise_level > requested_level:
            continue
        
        # Check muscle group if specified
        if target_muscles:
            if exercise["muscle_group"] not in target_muscles:
                continue
        
        filtered.append(exercise)
    
    return filtered

def generate_workout(request: WorkoutRequest) -> WorkoutResponse:
    """Generate a random workout based on user preferences."""
    
    # Filter available exercises
    available_exercises = filter_exercises(
        difficulty=request.difficulty,
        target_muscles=request.target_muscles
    )
    
    # Calculate how many exercises we need based on duration
    # Roughly 5-7 minutes per exercise including rest
    num_exercises = max(3, request.duration // 7)
    
    # Make sure we don't request more exercises than available
    num_exercises = min(num_exercises, len(available_exercises))
    
    # Randomly select exercises
    selected = random.sample(available_exercises, num_exercises)
    
    # Convert to Exercise models
    exercises = []
    for ex in selected:
        exercises.append(Exercise(
            name=ex["name"],
            muscle_group=ex["muscle_group"],
            difficulty=ex["difficulty"],
            sets=ex["sets"],
            reps=ex.get("reps"),
            duration=ex.get("duration"),
            rest=ex["rest"],
            instructions=ex["instructions"],
            equipment=ex.get("equipment")
        ))
    
    # Estimate calories (rough estimate: 5-10 calories per minute)
    calories_per_minute = {"beginner": 5, "intermediate": 7, "advanced": 10}
    calories = request.duration * calories_per_minute[request.difficulty.value]
    
    return WorkoutResponse(
        workout_id=str(uuid.uuid4()),
        workout_type=request.workout_type,
        difficulty=request.difficulty,
        exercises=exercises,
        estimated_duration=request.duration,
        total_exercises=len(exercises),
        calories_estimate=calories
    )

