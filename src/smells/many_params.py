import ast
from .base import CodeSmell

class ManyParameters(CodeSmell):
    name = "Too Many Parameters"
    severity = "MEDIUM"

    def __init__(self, max_params=4):
        self.max_params = max_params

    def detect(self, tree, filename):
        results = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                count = len(node.args.args)
                if count > self.max_params:
                    results.append({
                        "file": filename,
                        "smell": self.name,
                        "line": node.lineno,
                        "message": f"{count} parameters",
                        "severity": self.severity
                    })
        return results
