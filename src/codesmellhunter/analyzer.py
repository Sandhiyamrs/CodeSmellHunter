from codesmellhunter.metrics import CodeMetrics
from codesmellhunter.utils import find_python_files, read_file_safe
import ast


class Analyzer:
    def __init__(self, smells):
        self.smells = smells

    def analyze(self, path):
        results = []
        metrics_summary = {}

        for file in find_python_files(path):
            source = read_file_safe(file)
            if not source:
                continue

            tree = ast.parse(source)

            metrics = CodeMetrics().analyze(source)
            metrics_summary[str(file)] = metrics

            for smell in self.smells:
                results.extend(smell.detect(tree, str(file)))

        return {
            "issues": results,
            "metrics": metrics_summary
        }
