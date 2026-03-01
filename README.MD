# 🛸 Drone Counting Hackathon

Build a high-performance computer vision system that counts the number of drones in each frame of a video. Your task is to submit a **Python script** that processes a provided video and outputs a **CSV file** containing drone counts per frame.

The competition rewards both **precision** and **speed**.

---

# 📦 Submission Requirements

## 1. Deliverable

You must submit:

* A **Python script** (`main.py`)
* A generated **CSV file** as output
* A link to your **GitHub repository** (submitted via the official form)

### Output Format

Your program must output a CSV file with:

* **Single row**
* Each value represents the number of drones detected in that frame
* Values separated by commas
* No header

### Example

If a video has 5 frames and your predictions are:

```
0,1,1,2,0
```

Your CSV should contain exactly:

```
0,1,1,2,0
```

No extra whitespace. No additional rows.

---

# 🎯 Challenge Levels

There are **3 levels of difficulty**, each contributing to your final grade:

| Level   | Weight | Description                                                                                                                                      |
| ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Level 1 | 20%    | Up to **1 drone**, simple concrete background                                                                                                    |
| Level 2 | 30%    | Up to **2 drones**, simple concrete background                                                                                                   |
| Level 3 | 50%    | Up to **2 drones**, complex background with reflections, occlusions, and objects that may obscure drones (obscured drones must still be counted) |

Each level is graded independently.

---

# 🧮 Scoring Breakdown

Each level is graded out of **100 points**, composed of:

* **50 points — Precision**
* **50 points — Speed**

---

## 📊 Precision Scoring (50 points)

Each frame earns points based on prediction accuracy.

### Frames with 0 drones

| Guess | Points |
| ----- | ------ |
| 0     | 1.0    |
| 1     | 0.25   |
| ≥2    | 0      |

### Frames with 1 drone

| Guess | Points |
| ----- | ------ |
| 0     | 0      |
| 1     | 1.0    |
| 2     | 0.25   |

### Frames with 2 drones

| Guess | Points |
| ----- | ------ |
| 0     | 0      |
| 1     | 0.5    |
| 2     | 1.0    |

---

### Precision Score Formula

$\text{Precision Score} = 50 \times \left(\frac{\text{Total Points Earned}}{\text{Number of Frames}}\right)$

---

## ⚡ Speed Scoring (50 points)

Execution time matters.

For each level:

$\text{Speed Score} = 50 \times (\text{Percentile Rank of Time})$

* Fastest submission → near 50 points
* Median speed → ~25 points
* Slowest → near 0 points

Execution time will be measured in a controlled grading environment.

---

# 🛠 Technical Requirements

## Execution Expectations

Your script must:

* Run from command line
* Accept a video file as input
* Produce the required CSV file
* Complete without manual intervention

Example execution:

```bash
python main.py input_video.mp4 output.csv
```

---

# 📚 Sample Submission

A sample submission using **OpenCV + YOLO** is provided as reference.

You are free to implement any method, including:

* Classical CV (background subtraction, contour detection)
* Deep learning (CNNs, object detection, transformers)
* Hybrid pipelines
* Tracking + temporal smoothing
* Ensemble methods

---

# ✅ Approved Libraries

You may use the following libraries without additional approval:

### Core

* `numpy`
* `pandas`
* `scipy`
* `matplotlib`
* `opencv-python`
* `scikit-image`

### Machine Learning

* `scikit-learn`
* `xgboost`
* `lightgbm`

### Deep Learning

* `torch`
* `torchvision`
* `torchaudio`
* `tensorflow`
* `keras`

### Detection Frameworks

* `ultralytics`
* `detectron2`
* `mmcv`
* `mmdet`

### Utilities

* `tqdm`
* `argparse`
* `pathlib`
* `time`
* `logging`

---

## 📌 Using Other Libraries

If you plan to use a library **not listed above** and not included in the Python standard library:

* Message the Discord channel: **[appropriate forum]**
* Or email: **[appropriate email]**

This ensures our graders can properly install and evaluate your submission.

---

# 🚀 Strategy Considerations

Level 3 introduces:

* Reflections
* Background clutter
* Partial occlusions
* Distractors

Obscured drones **must still be counted**.

Robust solutions may involve:

* Object tracking across frames
* Temporal smoothing
* Confidence threshold calibration
* Domain adaptation techniques
* Ensemble detection
* Post-processing heuristics

Balance **model complexity** with **inference speed**.

---

# 📅 Deadline

**Submissions Due: March 25**

Late submissions will not be accepted.

---

# 📤 How to Submit

1. Push your solution to GitHub.
2. Ensure your repository includes:

   * `main.py`
   * `requirements.txt`
   * README with execution instructions
3. Submit your GitHub link using this form:

👉 **[submission form link]**

---

# 🏆 Winning Criteria

Highest total weighted score across all three levels wins.

Your final score is:

[
0.20 \times L1 + 0.30 \times L2 + 0.50 \times L3
]

Where each level is scored out of 100.

---

# 🔍 Evaluation Notes

* Code must be reproducible.
* Non-deterministic solutions must fix random seeds.
* Hard-coded frame counts will result in disqualification.
* Scripts that crash or exceed time limits receive zero for speed.

---

Good luck. Optimize carefully. Precision and performance both matter.

