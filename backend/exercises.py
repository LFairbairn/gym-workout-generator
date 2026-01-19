from models import MuscleGroup, DifficultyLevel

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
]
