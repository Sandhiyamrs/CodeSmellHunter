import ast


class LargeClassDetector:
    def __init__(self, config):
        self.max_methods = config["MAX_CLASS_METHODS"]

    def detect(self, tree, file_path):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [n for n in node.body if isinstance(n, ast.FunctionDef)]
                if len(methods) > self.max_methods:
                    issues.append({
                        "type": "Large Class",
                        "file": file_path,
                        "class": node.name,
                        "method_count": len(methods),
                    })
        return issues

