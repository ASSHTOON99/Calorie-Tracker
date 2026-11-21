# Camera Macro Tracker
A Python project that captures a food or meal from a camera, identifies items and portion estimates, and computes nutritional macros (calories, protein, carbs, fiber, and fats).

## Planned Pipeline
1. `src/camera.py`: Capture a frame from the camera.
2. `src/detector.py`: Identify food item(s) and estimate portion weight in grams.
3. `src/nutrition.py`: Look up and scale macros (`calories_kcal`, `protein_g`, `carbs_g`, `fiber_g`, `fat_g`).
4. `src/main.py`: Run the pipeline and print/log results.
