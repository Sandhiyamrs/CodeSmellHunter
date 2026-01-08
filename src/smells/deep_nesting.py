import ast
from .base import CodeSmell

class DeepNesting(CodeSmell):
    name = "Deep Nesting"
    severity = "MEDIUM"

    def __init__(self, max_depth=4):
        self.max_depth = max_depth

    def detect(self, tree, filename):
        results = []

        def visit(node, depth=0):
            if depth > self.max_depth:
                results.append({
                    "file": filename,
                    "smell": self.name,
                    "line": node.lineno,
                    "message": f"Nesting depth {depth}",
                    "severity": self.severity
                })
            for child in ast.iter_child_nodes(node):
                visit(child, depth + 1)

        visit(tree)
        return results

