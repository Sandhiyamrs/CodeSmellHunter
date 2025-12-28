
import ast


class LongMethodDetector:
    def __init__(self, config):
        self.max_length = config["MAX_METHOD_LENGTH"]

    def detect(self, tree, file_path):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                length = len(node.body)
                if length > self.max_length:
                    issues.append({
                        "type": "Long Method",
                        "file": file_path,
                        "function": node.name,
                        "lines": length,
                    })
        return issues
