import json
import os


class ReportGenerator:
    def generate(self, smells, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(smells, f, indent=4)

