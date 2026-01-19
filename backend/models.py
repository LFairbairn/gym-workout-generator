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

    