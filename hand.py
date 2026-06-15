import cv2
import random
import math
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# --- Configuration ---
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)

FRUIT_FILES = [
    "fruits/watermelon.png",
    "fruits/apple.png",
    "fruits/orange.png",
    "fruits/banana.png",
    "fruits/mango.png",
]
FRUIT_COLORS = [(0, 200, 0), (0, 100, 255), (0, 165, 255), (0, 255, 255), (180, 105, 255)]

def load_fruits(paths, size=80):
    loaded = []
    for p in paths:
        img = cv2.imread(p, cv2.IMREAD_UNCHANGED)
        if img is not None:
            img = cv2.resize(img, (size, size))
            loaded.append(img)
    return loaded

fruit_imgs = load_fruits(FRUIT_FILES)
USE_IMAGES = len(fruit_imgs) > 0

# --- Helper Functions ---
def overlay_png(background, overlay, x, y):
    h, w = overlay.shape[:2]
    x1, y1 = x - w // 2, y - h // 2
    x2, y2 = x1 + w, y1 + h

    if x1 < 0 or y1 < 0 or x2 > background.shape[1] or y2 > background.shape[0]:
        return background

    if overlay.shape[2] == 4:
        alpha = overlay[:, :, 3] / 255.0
        for c in range(3):
            background[y1:y2, x1:x2, c] = (
                alpha * overlay[:, :, c] + (1 - alpha) * background[y1:y2, x1:x2, c]
            ).astype(np.uint8)
    else:
        background[y1:y2, x1:x2] = overlay
    return background

def overlay_sliced(background, overlay, x, y):
    h, w = overlay.shape[:2]
    background = overlay_png(background, overlay[:h // 2, :], x - 10, y - 15)
    background = overlay_png(background, overlay[h // 2:, :], x + 10, y + 15)
    return background

def new_fruit():
    return {
        "pos": [random.randint(100, 1100), random.randint(-100, 0)],
        "radius": 40,
        "speed": random.randint(5, 12),
        "img_index": random.randint(0, len(fruit_imgs) - 1) if USE_IMAGES else 0,
        "sliced": False,
        "slice_timer": 0,
    }

# --- Game Variables ---
score = 0
lives = 3
fruits = []
game_state = "start"

def reset_game():
    global score, lives, fruits
    score = 0
    lives = 3
    fruits = [new_fruit() for _ in range(6)]

# --- Main Loop ---
while True:
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1)

    if game_state == "start":
        cv2.putText(img, "FRUIT NINJA", (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)
        cv2.putText(img, "Press S To Start", (320, 380), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
        if cv2.waitKey(1) & 0xFF == ord("s"):
            reset_game()
            game_state = "playing"

    elif game_state == "playing":
        hands, img = detector.findHands(img)
        index_x, index_y = (hands[0]["lmList"][8][0], hands[0]["lmList"][8][1]) if hands else (None, None)
        
        if index_x:
            cv2.circle(img, (index_x, index_y), 12, (0, 255, 200), cv2.FILLED)

        for fruit in fruits:
            fx, fy = int(fruit["pos"][0]), int(fruit["pos"][1])
            if not fruit["sliced"]:
                fruit["pos"][1] += fruit["speed"]
                if fy > 720:
                    lives -= 1
                    fruit.update(new_fruit())
                    continue
                
                # Draw Fruit
                if USE_IMAGES: img = overlay_png(img, fruit_imgs[fruit["img_index"]], fx, fy)
                else: cv2.circle(img, (fx, fy), fruit["radius"], FRUIT_COLORS[fruit["img_index"] % 5], cv2.FILLED)

                if index_x and math.sqrt((fx - index_x)**2 + (fy - index_y)**2) < fruit["radius"]:
                    fruit["sliced"] = True
                    fruit["slice_timer"] = 10
                    score += 1
            else:
                # Slice Effect
                if USE_IMAGES: img = overlay_sliced(img, fruit_imgs[fruit["img_index"]], fx, fy)
                else:
                    cv2.circle(img, (fx - 15, fy - 15), 20, (255,0,0), cv2.FILLED)
                    cv2.circle(img, (fx + 15, fy + 15), 20, (255,0,0), cv2.FILLED)
                
                fruit["slice_timer"] -= 1
                if fruit["slice_timer"] <= 0: fruit.update(new_fruit())

        cv2.putText(img, f"Score: {score}", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
        cv2.putText(img, f"Lives: {lives}", (50, 140), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        
        if lives <= 0: game_state = "gameover"

    elif game_state == "gameover":
        cv2.putText(img, "GAME OVER", (250, 300), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
        cv2.putText(img, f"Final Score: {score}", (350, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
        cv2.putText(img, "Press R To Restart", (300, 500), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        if cv2.waitKey(1) & 0xFF == ord("r"):
            reset_game()
            game_state = "playing"

    cv2.imshow("Fruit Ninja 🍉", img)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()