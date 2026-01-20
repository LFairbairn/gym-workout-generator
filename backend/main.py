from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import WorkoutRequest, WorkoutResponse, MuscleGroup, DifficultyLevel, WorkoutType
from .workout_logic import generate_workout


app = FastAPI(
    title="Gym Workout Generator",
    description="Generate random gym workouts based on your preferences",
    version="1.0.0"
)

# Allow frontend to make requests to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/api/generate-workout", response_model=WorkoutResponse)
async def create_workout(request: WorkoutRequest):
    """Generate a random workout based on user preferences."""
    try:
        workout = generate_workout(request)
        return workout
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/options")
async def get_options():
    """Return available workout options for the frontend."""
    return {
        "workout_types": [t.value for t in WorkoutType],
        "difficulty_levels": [d.value for d in DifficultyLevel],
        "muscle_groups": [m.value for m in MuscleGroup]
    }

