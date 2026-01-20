import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.models import WorkoutType, DifficultyLevel, MuscleGroup

client = TestClient(app)

def test_get_options():
    """Test that the options endpoint returns all available choices."""
    response = client.get("/api/options")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "workout_types" in data
    assert "difficulty_levels" in data
    assert "muscle_groups" in data
    
    assert "strength" in data["workout_types"]
    assert "beginner" in data["difficulty_levels"]
    assert "chest" in data["muscle_groups"]

def test_generate_workout():
    """Test that we can generate a workout with valid parameters."""
    request_data = {
        "workout_type": "strength",
        "duration": 30,
        "difficulty": "beginner",
        "target_muscles": ["chest", "back"]
    }
    
    response = client.post("/api/generate-workout", json=request_data)
    
    assert response.status_code == 200
    data = response.json()
    
    assert "workout_id" in data
    assert "exercises" in data
    assert len(data["exercises"]) > 0
    assert data["workout_type"] == "strength"
    assert data["difficulty"] == "beginner"

def test_invalid_duration():
    """Test that invalid duration is rejected."""
    request_data = {
        "workout_type": "strength",
        "duration": 5,  # Too short - minimum is 15
        "difficulty": "beginner"
    }
    
    response = client.post("/api/generate-workout", json=request_data)
    
    assert response.status_code == 422  # Validation error


