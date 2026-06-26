![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)

# Fruit Ninja AI

An AI-powered gesture-controlled gaming application that transforms real-time hand movements into interactive gameplay using computer vision and hand-tracking technologies. By leveraging MediaPipe and OpenCV, the system enables users to slice virtual fruits through natural hand gestures, creating an immersive touchless gaming experience.

## Overview

Fruit Ninja AI showcases the integration of computer vision, real-time image processing, and human-computer interaction in game development. The application tracks hand landmarks through a webcam feed and maps finger movements to in-game actions, allowing players to interact with the game without traditional input devices.

The project demonstrates how modern AI-based vision systems can be applied to create intuitive and engaging user experiences.

---

## Key Features

### Real-Time Hand Tracking
- Accurate hand landmark detection using MediaPipe Hands
- Low-latency gesture processing for smooth gameplay
- Robust tracking under varying hand positions

### Gesture-Based Fruit Slicing
- Converts finger movements into virtual slicing actions
- Natural and intuitive gameplay without keyboards or controllers
- Real-time collision detection between gestures and fruits

### Dynamic Gameplay
- Multiple fruit categories including apples, bananas, oranges, mangoes, and watermelons
- Randomized fruit spawning for varied gameplay sessions
- Continuous score tracking and performance feedback

### Webcam-Powered Interaction
- Live video stream processing using OpenCV
- Seamless integration between computer vision and game mechanics
- Fully touchless gaming experience

---

## Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Hand Tracking | MediaPipe |
| Numerical Computing | NumPy |

---

## Installation

### Prerequisites

- Python 3.7+
- Webcam-enabled device
- Internet connection (for initial MediaPipe model setup)

### Setup

Clone the repository:

```bash
git clone https://github.com/codewithtrisha09/Fruit_Ninja.git
cd Fruit_Ninja
```

Install dependencies:

```bash
pip install opencv-python mediapipe numpy
```

Run the application:

```bash
python hand.py
```

---

## How It Works

1. The webcam captures live video frames.
2. MediaPipe detects and tracks hand landmarks in real time.
3. Fingertip coordinates are extracted from detected hand landmarks.
4. Movement trajectories are interpreted as slicing gestures.
5. Collision detection determines whether fruits have been successfully sliced.
6. Scores are updated and displayed dynamically during gameplay.

---

## System Architecture

### Hand Tracking Module
Responsible for detecting hands and extracting landmark coordinates using MediaPipe's hand pose estimation framework.

### Gesture Recognition Engine
Processes fingertip movement patterns and translates them into slicing actions.

### Game Engine
Handles fruit spawning, collision detection, scoring logic, and gameplay mechanics.

### Rendering System
Combines webcam frames with game elements and visual overlays for real-time display.

---

## Future Enhancements

### Advanced Gameplay Features
- Bomb objects with penalty mechanics
- Combo-based scoring system
- Increasing difficulty levels
- Limited lives and game-over conditions

### Data Persistence
- High-score storage and retrieval
- Local leaderboard functionality
- Session statistics tracking

### User Experience Improvements
- Sound effects and background music
- Enhanced animations and visual effects
- Pause and resume functionality
- End-game performance analytics

### AI Enhancements
- Multi-hand gesture support
- Gesture classification using machine learning models
- Adaptive difficulty based on player performance

---

## Learning Outcomes

Through this project, the following concepts were explored and implemented:

- Real-time computer vision applications
- Hand landmark detection and tracking
- Gesture recognition systems
- Human-computer interaction (HCI)
- Game development fundamentals
- Real-time event processing and rendering

---

## System Requirements

- 4 GB RAM or higher
- Dual-core processor (1.5 GHz+)
- Webcam (built-in or external)
- Approximately 50 MB of available storage

---

## Contributing

Contributions, feature suggestions, and bug reports are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add feature"
```

4. Push to your branch and create a Pull Request

---

## Author

**Trisha Shetty**

GitHub: https://github.com/codewithtrisha09

If you find this project useful, consider starring the repository and sharing feedback through Issues.

---

*Built using Computer Vision, AI-powered Hand Tracking, and Real-Time Gesture Recognition.*
