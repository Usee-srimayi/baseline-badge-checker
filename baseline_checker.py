baseline_features = {
    "fetch": True,
    ":has": False,
    "grid": True,
    "backdrop-filter": False
}
import os

def scan_code():
    used = set()
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith((".html", ".css", ".js")):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    content = f.read()
                    for feature in baseline_features:
                        if feature in content:
                            used.add(feature)
    return used
def calculate_score(used):
    safe = [f for f in used if baseline_features.get(f, False)]
    score = round(len(safe) / len(used) * 100, 2) if used else 100
    with open("baseline_score.txt", "w") as f:
        f.write(str(score))
    print(f"Baseline Compatibility: {score}%")
features_used = scan_code()
calculate_score(features_used)
