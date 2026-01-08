import ast
from .base import CodeSmell

class MagicNumbers(CodeSmell):
    name = "Magic Number"
    severity = "LOW"

    def detect(self, tree, filename):
        results = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                if node.value not in (0, 1):
                    results.append({
                        "file": filename,
                        "smell": self.name,
                        "line": node.lineno,
                        "message": f"Magic number {node.value}",
                        "severity": self.severity
                    })
        return results

