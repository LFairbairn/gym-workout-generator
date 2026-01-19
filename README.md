# Gym Workout Generator

A random gym workout generator that creates personalized workout routines based on user preferences. Built as a Progressive Web App (PWA) with a Python backend and modern web frontend.

## Features

- **Random Workout Generation**: Creates customized workout routines based on user selections
- **User Preferences**: Select workout type, duration, difficulty level, and target muscle groups
- **Exercise Database**: Comprehensive collection of exercises with instructions
- **Progressive Web App**: Install on mobile devices and use offline
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

## Technology Stack

### Backend
- **Python 3.8+**
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with responsive design
- **JavaScript (Vanilla)**: Interactive functionality without frameworks
- **PWA**: Service Worker and Web App Manifest for offline capabilities

## Project Structure

```
gym-workout-generator/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── workout_logic.py     # Workout generation logic
│   ├── exercises.py         # Exercise database
│   └── models.py            # Data models
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css   # Application styles
│   │   ├── js/
│   │   │   ├── app.js       # Main application logic
│   │   │   └── sw.js        # Service Worker
│   │   └── images/
│   │       └── icons/       # PWA icons
│   ├── templates/
│   │   └── index.html       # Main HTML template
│   └── manifest.json        # PWA manifest
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd gym-workout-generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   cd backend
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`

## Usage

1. **Select Workout Preferences**:
   - Choose workout type (Strength, Cardio, HIIT, Flexibility)
   - Select duration (15, 30, 45, or 60 minutes)
   - Pick difficulty level (Beginner, Intermediate, Advanced)
   - Target specific muscle groups (optional)

2. **Generate Workout**:
   - Click the "Generate Workout" button
   - View your personalized workout routine

3. **Install as PWA** (Optional):
   - On mobile: Use "Add to Home Screen" option in your browser
   - On desktop: Look for the install prompt in the address bar

## API Endpoints

### `POST /api/generate-workout`
Generates a random workout based on user preferences.

**Request Body**:
```json
{
  "workout_type": "strength",
  "duration": 30,
  "difficulty": "intermediate",
  "target_muscles": ["chest", "back"]
}
```

**Response**:
```json
{
  "workout_id": "abc123",
  "exercises": [
    {
      "name": "Push-ups",
      "sets": 3,
      "reps": 12,
      "rest": 60,
      "instructions": "..."
    }
  ],
  "estimated_duration": 30,
  "total_exercises": 6
}
```

## Development Workflow

This project follows Git best practices with feature branches:

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes and commit**:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

3. **Merge back to main**:
   ```bash
   git checkout main
   git merge feature/your-feature-name
   ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements

- User accounts and saved workouts
- Workout history tracking
- Video demonstrations for exercises
- Custom exercise creation
- Social sharing features
- Integration with fitness tracking apps

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Exercise data compiled from various fitness resources
- Built with modern web technologies for optimal performance
- Designed with user experience and accessibility in mind

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Training!** 💪
