from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class WorkoutType(str, Enum):
    STRENGTH = "strength"
    CARDIO = "cardio"
    HIIT = "hiit"
    FLEXIBILITY = "flexibility"
    MIXED = "mixed"

class DifficultyLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class MuscleGroup(str, Enum):
    CHEST = "chest"
    BACK = "back"
    LEGS = "legs"
    SHOULDERS = "shoulders"
    ARMS = "arms"
    CORE = "core"
    FULL_BODY = "full_body"

class WorkoutRequest(BaseModel):
    workout_type: WorkoutType
    duration: int = Field(ge=15, le=120, description="Workout duration in minutes")
    difficulty: DifficultyLevel
    target_muscles: Optional[List[MuscleGroup]] = None

class Exercise(BaseModel):
    name: str
    muscle_group: MuscleGroup
    difficulty: DifficultyLevel
    sets: int
    reps: Optional[int] = None
    duration: Optional[int] = None  # in seconds, for cardio/timed exercises
    rest: int  # rest time in seconds
    instructions: str
    equipment: Optional[str] = None


class WorkoutResponse(BaseModel):
    workout_id: str
    workout_type: WorkoutType
    difficulty: DifficultyLevel
    exercises: List[Exercise]
    estimated_duration: int
    total_exercises: int
    calories_estimate: int



