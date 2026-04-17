import os
import shutil

dir_name = "BMLP_Wahid-Ivan-Saputra"
os.makedirs(dir_name, exist_ok=True)

# Files to move/rename from root to the submission folder
files_to_copy = {
    "model_clustering": "model_clustering.h5",
    "decision_tree_model.h5": "decision_tree_model.h5",
    "data_clustering.csv": "data_clustering.csv"
}

print("Organizing files for submission...")
for src, dst in files_to_copy.items():
    if os.path.exists(src):
        shutil.copy(src, os.path.join(dir_name, dst))
        print(f"  [OK] Copied {src} to {dst}")
    else:
        print(f"  [!!] Warning: {src} not found. Running the notebooks will generate this file.")

print("\nFolder 'BMLP_Wahid-Ivan-Saputra' check:")
for f in os.listdir(dir_name):
    print(f" - {f}")

print("\nReady for submission. Don't forget to ZIP the folder!")
