import ast
from .base import CodeSmell

class DuplicateCode(CodeSmell):
    name = "Duplicate Code"
    severity = "HIGH"

    def detect(self, tree, filename):
        seen = {}
        results = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                body = ast.dump(node)
                if body in seen:
                    results.append({
                        "file": filename,
                        "smell": self.name,
                        "line": node.lineno,
                        "message": f"Duplicate of function at line {seen[body]}",
                        "severity": self.severity
                    })
                else:
                    seen[body] = node.lineno
        return results
