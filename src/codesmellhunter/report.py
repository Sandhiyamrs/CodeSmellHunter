import json

def generate_report(results, output):
    with open(output, "w") as f:
        json.dump(results, f, indent=2)
