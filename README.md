# Fruit Ninja AI

A gesture-recognition-based interactive game leveraging computer vision and hand-tracking technologies. This application captures real-time hand movements via webcam and translates hand gestures into game interactions, enabling gesture-driven fruit-slicing gameplay.

## Overview

Fruit Ninja AI demonstrates the practical application of computer vision in interactive entertainment. The system employs MediaPipe for accurate hand detection and OpenCV for image processing, creating a responsive, real-time user experience that bridges the gap between physical gesture and digital gameplay.

## Core Features

- **Real-Time Hand Tracking**: Precise hand detection and position tracking using MediaPipe's hand pose estimation
- **Gesture-Based Interaction**: Finger-based gesture recognition for fruit slicing mechanics
- **Dynamic Fruit Variety**: Support for multiple fruit types including apples, bananas, mangoes, oranges, and watermelons
- **Live Score Tracking**: Real-time score calculation and display during gameplay
- **Webcam Integration**: Seamless webcam input handling for gesture capture

## Technical Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| Computer Vision | OpenCV |
| Hand Detection | MediaPipe |
| Numerical Computing | NumPy |

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Functional webcam
- Stable internet connection (for MediaPipe model downloads)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/codewithtrisha09/Fruit_Ninja.git
cd Fruit_Ninja
```

2. Install required dependencies:
```bash
pip install opencv-python mediapipe numpy
```

3. Launch the application:
```bash
python hand.py
```

## Usage

- **Gameplay**: Position your hand in front of the webcam. Use your index finger to perform slicing gestures across fruits.
- **Exit Game**: Press `Ctrl + Q` to terminate the application.

## Planned Enhancements

### Game Mechanics
- **Bomb Detection System**: Random bomb spawning with collision penalties. Three bomb hits trigger game over.
- **Miss Tracking**: Three missed fruits result in game termination.
- **Combo Scoring**: Bonus points for consecutive fruit slices without misses.

### Persistence & Leaderboard
- Persistent high-score storage and retrieval
- Automatic score saving upon game completion
- Leaderboard functionality with ranked scoring

### User Experience
- Audio feedback system with sound effects
- Progressive difficulty scaling
- Pause and resume functionality
- Game-over screen with score summary
- Enhanced animation and visual effects

## Project Objectives

This project was developed to explore and implement:

- Computer vision techniques and real-time image processing
- Hand gesture recognition and pose estimation
- Interactive applications leveraging human-computer interaction
- Game development principles and mechanics

## Architecture

The application consists of:

- **Hand Detection Module**: Leverages MediaPipe for keypoint extraction and hand state inference
- **Game Engine**: Manages fruit spawning, collision detection, and scoring logic
- **Rendering Pipeline**: Handles webcam frame capture and game state visualization
- **Input Processing**: Translates hand coordinates into game commands

## System Requirements

- Minimum 4GB RAM
- 1.5 GHz processor or faster
- 50MB disk space
- Standard USB webcam or built-in laptop camera

## Contributing

Contributions are welcome. Please follow standard Git workflows:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit changes with descriptive messages
4. Push to the branch and submit a pull request

## Author

**Trisha Shetty**

GitHub: [@codewithtrisha09](https://github.com/codewithtrisha09)

For questions or feedback, please open an issue on the repository.

---

**Last Updated**: June 2026
