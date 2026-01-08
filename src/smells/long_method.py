import ast
from .base import CodeSmell

class LongMethod(CodeSmell):
    name = "Long Method"
    severity = "HIGH"

    def __init__(self, max_lines=40):
        self.max_lines = max_lines

    def detect(self, tree, filename):
        results = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                length = node.end_lineno - node.lineno
                if length > self.max_lines:
                    results.append({
                        "file": filename,
                        "smell": self.name,
                        "line": node.lineno,
                        "message": f"Function '{node.name}' has {length} lines",
                        "severity": self.severity
                    })
        return results
