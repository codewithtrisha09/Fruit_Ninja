import cv2
import random
import math
import numpy as np
from cvzone.HandTrackingModule import HandDetector

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

def load_fruits(paths, size=80):
    loaded = []
    for p in paths:
        img = cv2.imread(p, cv2.IMREAD_UNCHANGED)  # keep alpha channel
        if img is not None:
            img = cv2.resize(img, (size, size))
            loaded.append(img)
    return loaded

fruit_imgs = load_fruits(FRUIT_FILES)

USE_IMAGES = len(fruit_imgs) > 0

def overlay_png(background, overlay, x, y):
    
    h, w = overlay.shape[:2]
    x1, y1 = x - w // 2, y - h // 2
    x2, y2 = x1 + w, y1 + h

    # Clamp to frame bounds
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
    half1 = overlay[:h // 2, :]
    half2 = overlay[h // 2:, :]

   
    background = overlay_png(background, half1, x - 10, y - 15)
    background = overlay_png(background, half2, x + 10, y + 15)
    return background


score = 0
fruits = []

def new_fruit():
    return {
        "pos": [random.randint(100, 1100), random.randint(-100, 0)],
        "radius": 40,
        "speed": random.randint(5, 12),
        "img_index": random.randint(0, len(fruit_imgs) - 1) if USE_IMAGES else 0,
        "sliced": False,
        "slice_timer": 0,
    }

for _ in range(6):
    fruits.append(new_fruit())

FRUIT_COLORS = [(0,200,0),(0,100,255),(0,165,255),(0,255,255),(180,105,255)]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    index_x, index_y = None, None
    prev_x, prev_y = None, None

    if hands:
        lmList = hands[0]["lmList"]
        index_x, index_y = lmList[8][0], lmList[8][1]

        cv2.circle(img, (index_x, index_y), 12, (0, 255, 200), cv2.FILLED)
        cv2.circle(img, (index_x, index_y), 16, (255, 255, 255), 2)

    for fruit in fruits:
        fx, fy = int(fruit["pos"][0]), int(fruit["pos"][1])
        r = fruit["radius"]

        if not fruit["sliced"]:
            fruit["pos"][1] += fruit["speed"]

            if fy > 750:
                fruit.update(new_fruit())
                continue

            if USE_IMAGES:
                img = overlay_png(img, fruit_imgs[fruit["img_index"]], fx, fy)
            else:
                color = FRUIT_COLORS[fruit["img_index"] % len(FRUIT_COLORS)]
                cv2.circle(img, (fx, fy), r, color, cv2.FILLED)

          
            if index_x is not None:
                dist = math.sqrt((fx - index_x) ** 2 + (fy - index_y) ** 2)
                if dist < r:
                    fruit["sliced"] = True
                    fruit["slice_timer"] = 10
                    score += 1

        else:
           
            if USE_IMAGES:
                img = overlay_sliced(img, fruit_imgs[fruit["img_index"]], fx, fy)
            else:
                color = FRUIT_COLORS[fruit["img_index"] % len(FRUIT_COLORS)]
                cv2.circle(img, (fx - 15, fy - 15), r // 2, color, cv2.FILLED)
                cv2.circle(img, (fx + 15, fy + 15), r // 2, color, cv2.FILLED)

           
            for _ in range(4):
                ex = fx + random.randint(-40, 40)
                ey = fy + random.randint(-40, 40)
                cv2.line(img, (fx, fy), (ex, ey), (0, 0, 200), 2)

            fruit["slice_timer"] -= 1
            if fruit["slice_timer"] <= 0:
                fruit.update(new_fruit())

  
    cv2.putText(img, f"Score: {score}", (50, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    cv2.imshow("Fruit Ninja 🍉", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()