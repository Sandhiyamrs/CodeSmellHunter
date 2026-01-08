import ast
from pathlib import Path

class Analyzer:
    def __init__(self, smells):
        self.smells = smells

    def analyze(self, path):
        findings = []
        for file in Path(path).rglob("*.py"):
            tree = ast.parse(file.read_text())
            for smell in self.smells:
                findings.extend(smell.detect(tree, str(file)))
        return findings
