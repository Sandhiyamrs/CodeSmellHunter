import ast


class MagicNumberDetector:
    def __init__(self, config):
        self.ignore = config["IGNORE_MAGIC_NUMBERS"]

    def detect(self, tree, file_path):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                if node.value not in self.ignore:
                    issues.append({
                        "type": "Magic Number",
                        "file": file_path,
                        "value": node.value,
                        "line": node.lineno,
                    })
        return issues

