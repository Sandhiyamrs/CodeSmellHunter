import ast
from .base import CodeSmell

class LargeClass(CodeSmell):
    name = "Large Class"
    severity = "HIGH"

    def __init__(self, max_methods=10):
        self.max_methods = max_methods

    def detect(self, tree, filename):
        results = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [n for n in node.body if isinstance(n, ast.FunctionDef)]
                if len(methods) > self.max_methods:
                    results.append({
                        "file": filename,
                        "smell": self.name,
                        "line": node.lineno,
                        "message": f"Class '{node.name}' has {len(methods)} methods",
                        "severity": self.severity
                    })
        return results
