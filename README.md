# Fruit Ninja AI

A computer vision-based Fruit Ninja game developed using Python, OpenCV, and MediaPipe. The game uses real-time hand tracking to allow players to slice fruits using finger movements captured through a webcam.

## Features

### Current Features

* Real-time hand tracking using MediaPipe
* Webcam-based gameplay
* Fruit slicing through gesture detection
* Multiple fruit types:

  * Apple
  * Banana
  * Mango
  * Orange
  * Watermelon
* Real-time score tracking

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

## Installation

Clone the repository:

```bash
git clone https://github.com/codewithtrisha09/Fruit_Ninja.git
cd Fruit_Ninja
```

Install dependencies:

```bash
pip install opencv-python mediapipe numpy
```

Run the game:

```bash
python hand.py
```

## Controls

Move your hand in front of the webcam and use your index finger to slice fruits.

To close the game:

```text
Ctrl + Q
```

## Planned Updates

The following features are currently under development:

### Bomb System

* Bombs will appear randomly among fruits.
* Hitting a bomb counts as a penalty.
* If a bomb is hit more than three times, the game ends.

### High Score Storage

* Persistent high-score tracking.
* Automatic saving of best scores.
* High-score display on startup.

### Miss Counter

* Missing a fruit counts as one strike.
* Missing more than three fruits results in a game over.

### Additional Improvements

* Sound effects
* Combo scoring system
* Difficulty levels
* Improved animations
* Pause and restart functionality
* Game-over screen
* Leaderboard support

## Project Goals

This project was developed to explore:

* Computer Vision
* Hand Gesture Recognition
* Real-Time Image Processing
* Interactive Game Development

## Author

Trisha Shetty

GitHub: https://github.com/codewithtrisha09
