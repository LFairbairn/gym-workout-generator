from .models import MuscleGroup, DifficultyLevel, WorkoutType


EXERCISE_DATABASE = [
    # ================================
    # STRENGTH EXERCISES
    # ================================

    # CHEST - Strength
    {
        "name": "Push-ups",
        "workout_type": WorkoutType.STRENGTH,
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
        "workout_type": WorkoutType.STRENGTH,
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
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.CHEST,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": 10,
        "rest": 90,
        "instructions": "Lie on bench with dumbbells at chest level. Press weights up until arms are extended, then lower with control.",
        "equipment": "Dumbbells, Bench"
    },
    {
        "name": "Incline Dumbbell Press",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.CHEST,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 10,
        "rest": 90,
        "instructions": "Set bench to 30-45 degrees. Press dumbbells up from chest level until arms are extended.",
        "equipment": "Dumbbells, Incline Bench"
    },
    {
        "name": "Cable Flyes",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.CHEST,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Stand between cable machines. Bring handles together in front of chest with slight bend in elbows, squeezing chest.",
        "equipment": "Cable Machine"
    },

    # BACK - Strength
    {
        "name": "Bodyweight Rows",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 10,
        "rest": 60,
        "instructions": "Hang from a bar at waist height. Pull your chest to the bar, squeezing shoulder blades together.",
        "equipment": "Bar or Smith Machine"
    },
    {
        "name": "Pull-ups",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 8,
        "rest": 90,
        "instructions": "Hang from bar with palms facing away. Pull yourself up until chin is over the bar, then lower with control.",
        "equipment": "Pull-up Bar"
    },
    {
        "name": "Dumbbell Rows",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Place one knee and hand on bench. Row dumbbell to hip, squeezing shoulder blade at top.",
        "equipment": "Dumbbell, Bench"
    },
    {
        "name": "Lat Pulldown",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Sit at lat pulldown machine. Pull bar down to upper chest, squeezing lats, then slowly release.",
        "equipment": "Lat Pulldown Machine"
    },
    {
        "name": "Deadlifts",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 4,
        "reps": 6,
        "rest": 120,
        "instructions": "Stand with feet hip-width apart. Hinge at hips to grip bar, then drive through heels to stand up straight.",
        "equipment": "Barbell"
    },

    # LEGS - Strength
    {
        "name": "Bodyweight Squats",
        "workout_type": WorkoutType.STRENGTH,
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
        "workout_type": WorkoutType.STRENGTH,
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
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": 12,
        "rest": 90,
        "instructions": "Hold dumbbell at chest level. Squat down keeping chest up and weight in heels, then drive back up.",
        "equipment": "Dumbbell"
    },
    {
        "name": "Leg Press",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": 10,
        "rest": 90,
        "instructions": "Sit in leg press machine with feet shoulder-width apart. Push platform away, then lower with control.",
        "equipment": "Leg Press Machine"
    },
    {
        "name": "Romanian Deadlifts",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 10,
        "rest": 90,
        "instructions": "Hold dumbbells in front of thighs. Hinge at hips, lowering weights along legs while keeping back flat.",
        "equipment": "Dumbbells"
    },

    # SHOULDERS - Strength
    {
        "name": "Pike Push-ups",
        "workout_type": WorkoutType.STRENGTH,
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
        "workout_type": WorkoutType.STRENGTH,
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
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.SHOULDERS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Hold dumbbells at sides. Raise arms out to sides until parallel with floor, then lower slowly.",
        "equipment": "Dumbbells"
    },
    {
        "name": "Front Raises",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.SHOULDERS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Hold dumbbells in front of thighs. Raise one arm forward to shoulder height, lower, and alternate.",
        "equipment": "Dumbbells"
    },

    # ARMS - Strength
    {
        "name": "Bicep Curls",
        "workout_type": WorkoutType.STRENGTH,
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
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.ARMS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 10,
        "rest": 60,
        "instructions": "Place hands on bench behind you. Lower body by bending elbows to 90 degrees, then push back up.",
        "equipment": "Bench"
    },
    {
        "name": "Hammer Curls",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.ARMS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Hold dumbbells with palms facing each other. Curl weights to shoulders keeping palms facing in.",
        "equipment": "Dumbbells"
    },
    {
        "name": "Tricep Pushdowns",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.ARMS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 12,
        "rest": 60,
        "instructions": "Stand at cable machine with rope attachment. Push rope down until arms are straight, squeezing triceps.",
        "equipment": "Cable Machine"
    },

    # CORE - Strength
    {
        "name": "Plank",
        "workout_type": WorkoutType.STRENGTH,
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
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": 15,
        "rest": 45,
        "instructions": "Lie on back with knees bent. Curl shoulders off floor toward knees, then lower with control.",
        "equipment": None
    },
    {
        "name": "Russian Twists",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 20,
        "rest": 45,
        "instructions": "Sit with knees bent, lean back slightly. Rotate torso side to side, optionally holding a weight.",
        "equipment": "Dumbbell (optional)"
    },
    {
        "name": "Leg Raises",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": 12,
        "rest": 45,
        "instructions": "Lie flat on back with hands under hips. Raise legs to 90 degrees, then lower slowly without touching floor.",
        "equipment": None
    },

    # FULL BODY - Strength
    {
        "name": "Thrusters",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 4,
        "reps": 10,
        "rest": 90,
        "instructions": "Hold dumbbells at shoulders. Squat down, then drive up explosively and press weights overhead in one motion.",
        "equipment": "Dumbbells"
    },
    {
        "name": "Clean and Press",
        "workout_type": WorkoutType.STRENGTH,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 4,
        "reps": 8,
        "rest": 90,
        "instructions": "Start with dumbbells at thighs. Pull weights up to shoulders in one motion, then press overhead.",
        "equipment": "Dumbbells"
    },

    # ================================
    # CARDIO EXERCISES
    # ================================

    # Cardio - Machines
    {
        "name": "Treadmill Walking",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 1,
        "reps": None,
        "duration": 600,
        "rest": 0,
        "instructions": "Walk at a brisk pace (3-4 mph) on the treadmill. Keep posture upright and arms swinging naturally.",
        "equipment": "Treadmill"
    },
    {
        "name": "Treadmill Jogging",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 1,
        "reps": None,
        "duration": 600,
        "rest": 0,
        "instructions": "Jog at a moderate pace (5-6 mph) on the treadmill. Land softly on midfoot and maintain steady breathing.",
        "equipment": "Treadmill"
    },
    {
        "name": "Treadmill Running",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 1,
        "reps": None,
        "duration": 600,
        "rest": 0,
        "instructions": "Run at a challenging pace (7+ mph) on the treadmill. Focus on form and controlled breathing.",
        "equipment": "Treadmill"
    },
    {
        "name": "Incline Treadmill Walk",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 1,
        "reps": None,
        "duration": 600,
        "rest": 0,
        "instructions": "Set treadmill to 10-15% incline. Walk at 3-3.5 mph, engaging glutes with each step.",
        "equipment": "Treadmill"
    },
    {
        "name": "Stationary Bike",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 1,
        "reps": None,
        "duration": 600,
        "rest": 0,
        "instructions": "Cycle at a steady pace with moderate resistance. Keep your core engaged and back straight.",
        "equipment": "Stationary Bike"
    },
    {
        "name": "Indoor Cycling",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 1,
        "reps": None,
        "duration": 600,
        "rest": 0,
        "instructions": "Cycle with varying resistance levels. Alternate between seated and standing positions.",
        "equipment": "Spin Bike"
    },
    {
        "name": "Rowing Machine",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 1,
        "reps": None,
        "duration": 600,
        "rest": 0,
        "instructions": "Push with legs first, then lean back and pull handle to chest. Return in reverse order. Maintain rhythm.",
        "equipment": "Rowing Machine"
    },
    {
        "name": "Elliptical Trainer",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 1,
        "reps": None,
        "duration": 600,
        "rest": 0,
        "instructions": "Move in a smooth elliptical motion, pushing and pulling the handles. Keep core engaged throughout.",
        "equipment": "Elliptical Machine"
    },
    {
        "name": "Stair Climber",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 1,
        "reps": None,
        "duration": 600,
        "rest": 0,
        "instructions": "Step continuously on the stair climber. Avoid leaning on handrails - use them only for balance.",
        "equipment": "Stair Climber"
    },

    # Cardio - No Equipment
    {
        "name": "Jumping Jacks",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": None,
        "duration": 60,
        "rest": 30,
        "instructions": "Jump feet out wide while raising arms overhead, then jump back to start position. Repeat continuously.",
        "equipment": None
    },
    {
        "name": "High Knees",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 3,
        "reps": None,
        "duration": 45,
        "rest": 30,
        "instructions": "Run in place bringing knees up to hip height. Pump arms and maintain quick tempo.",
        "equipment": None
    },
    {
        "name": "Skipping",
        "workout_type": WorkoutType.CARDIO,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 3,
        "reps": None,
        "duration": 60,
        "rest": 30,
        "instructions": "Skip rope at a steady pace, jumping just high enough for rope to pass. Keep elbows close to body.",
        "equipment": "Skipping Rope"
    },

    # ================================
    # HIIT EXERCISES
    # ================================

    {
        "name": "Burpees",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": 10,
        "rest": 30,
        "instructions": "From standing, drop to push-up position, perform push-up, jump feet to hands, then jump up with arms overhead.",
        "equipment": None
    },
    {
        "name": "Mountain Climbers",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": None,
        "duration": 30,
        "rest": 20,
        "instructions": "Start in push-up position. Drive knees toward chest alternately as fast as possible.",
        "equipment": None
    },
    {
        "name": "Jump Squats",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": 12,
        "rest": 30,
        "instructions": "Squat down then explode upward into a jump. Land softly and immediately go into next rep.",
        "equipment": None
    },
    {
        "name": "Box Jumps",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 4,
        "reps": 10,
        "rest": 30,
        "instructions": "Stand facing a sturdy box. Jump onto box with both feet, stand up fully, then step back down.",
        "equipment": "Plyo Box"
    },
    {
        "name": "Plyo Lunges",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 4,
        "reps": 16,
        "rest": 30,
        "instructions": "From lunge position, jump and switch legs mid-air, landing in lunge with opposite leg forward.",
        "equipment": None
    },
    {
        "name": "Tuck Jumps",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 3,
        "reps": 10,
        "rest": 30,
        "instructions": "Jump as high as possible, tucking knees to chest at the peak. Land softly and repeat immediately.",
        "equipment": None
    },
    {
        "name": "Speed Skaters",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": None,
        "duration": 30,
        "rest": 20,
        "instructions": "Leap side to side, landing on one foot while swinging opposite leg behind. Move like a speed skater.",
        "equipment": None
    },
    {
        "name": "Battle Ropes",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": None,
        "duration": 30,
        "rest": 30,
        "instructions": "Hold rope ends and create waves by alternating arms up and down rapidly. Keep core tight.",
        "equipment": "Battle Ropes"
    },
    {
        "name": "Kettlebell Swings",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 4,
        "reps": 15,
        "rest": 30,
        "instructions": "Hinge at hips, swing kettlebell between legs then drive hips forward to swing weight to chest height.",
        "equipment": "Kettlebell"
    },
    {
        "name": "Sprawls",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 4,
        "reps": 10,
        "rest": 30,
        "instructions": "From standing, drop hands to floor and kick legs back to plank. Immediately return to standing.",
        "equipment": None
    },
    {
        "name": "Sprint Intervals",
        "workout_type": WorkoutType.HIIT,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.ADVANCED,
        "sets": 6,
        "reps": None,
        "duration": 30,
        "rest": 60,
        "instructions": "Sprint at maximum effort on treadmill or track, then rest. Repeat for all sets.",
        "equipment": "Treadmill (optional)"
    },

    # ================================
    # FLEXIBILITY / STRETCHING EXERCISES
    # ================================

    # Upper Body Stretches
    {
        "name": "Chest Doorway Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.CHEST,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Place forearm on doorframe with elbow at shoulder height. Lean forward gently until stretch is felt in chest.",
        "equipment": "Doorway"
    },
    {
        "name": "Cat-Cow Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": 10,
        "rest": 15,
        "instructions": "On hands and knees, alternate between arching back up (cat) and dropping belly down (cow).",
        "equipment": None
    },
    {
        "name": "Child's Pose",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.BACK,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 45,
        "rest": 15,
        "instructions": "Kneel on floor, sit back on heels, and stretch arms forward on ground. Relax and breathe deeply.",
        "equipment": None
    },
    {
        "name": "Shoulder Cross-Body Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.SHOULDERS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Bring one arm across body at shoulder height. Use other hand to gently press arm closer. Switch sides.",
        "equipment": None
    },
    {
        "name": "Tricep Overhead Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.ARMS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Raise one arm overhead, bend elbow so hand reaches down back. Use other hand to gently press elbow.",
        "equipment": None
    },

    # Lower Body Stretches
    {
        "name": "Standing Quad Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Stand on one leg, bend other knee and hold foot behind you. Keep knees together and hips forward.",
        "equipment": None
    },
    {
        "name": "Standing Hamstring Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Place one heel on low surface with leg straight. Hinge at hips and lean forward until stretch is felt.",
        "equipment": "Bench or step"
    },
    {
        "name": "Hip Flexor Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Kneel on one knee with other foot forward. Push hips forward gently until stretch is felt in front of hip.",
        "equipment": None
    },
    {
        "name": "Pigeon Pose",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 2,
        "reps": None,
        "duration": 45,
        "rest": 15,
        "instructions": "From hands and knees, bring one knee forward and angle shin across mat. Extend other leg behind. Lower body toward floor.",
        "equipment": None
    },
    {
        "name": "Seated Forward Fold",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 45,
        "rest": 15,
        "instructions": "Sit with legs extended. Hinge at hips and reach toward toes, keeping back as straight as possible.",
        "equipment": None
    },
    {
        "name": "Butterfly Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 45,
        "rest": 15,
        "instructions": "Sit with soles of feet together, knees out to sides. Gently press knees toward floor using elbows.",
        "equipment": None
    },
    {
        "name": "Figure Four Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.LEGS,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Lie on back, cross one ankle over opposite knee. Pull uncrossed leg toward chest until stretch is felt in hip.",
        "equipment": None
    },

    # Core Stretches
    {
        "name": "Cobra Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Lie face down, place hands under shoulders. Press up, lifting chest while keeping hips on floor.",
        "equipment": None
    },
    {
        "name": "Supine Twist",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Lie on back, bring one knee across body toward opposite side. Keep shoulders flat on floor. Switch sides.",
        "equipment": None
    },
    {
        "name": "Kneeling Side Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.CORE,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Kneel with one leg extended to side. Reach overhead arm toward extended leg, stretching the side body.",
        "equipment": None
    },

    # Full Body Flexibility
    {
        "name": "Downward Dog",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 45,
        "rest": 15,
        "instructions": "From hands and knees, lift hips high forming an inverted V. Press heels toward floor and relax head.",
        "equipment": None
    },
    {
        "name": "World's Greatest Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.INTERMEDIATE,
        "sets": 2,
        "reps": 5,
        "rest": 15,
        "instructions": "Lunge forward, place same-side elbow to floor inside foot, then rotate and reach arm to ceiling. Alternate sides.",
        "equipment": None
    },
    {
        "name": "Standing Side Stretch",
        "workout_type": WorkoutType.FLEXIBILITY,
        "muscle_group": MuscleGroup.FULL_BODY,
        "difficulty": DifficultyLevel.BEGINNER,
        "sets": 2,
        "reps": None,
        "duration": 30,
        "rest": 15,
        "instructions": "Stand tall, reach one arm overhead and lean to opposite side. Feel stretch along entire side of body.",
        "equipment": None
    },
]
