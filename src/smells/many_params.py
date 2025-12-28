import ast


class ManyParamsDetector:
    def __init__(self, config):
        self.max_params = config["MAX_PARAMETERS"]

    def detect(self, tree, file_path):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                param_count = len(node.args.args)
                if param_count > self.max_params:
                    issues.append({
                        "type": "Too Many Parameters",
                        "file": file_path,
                        "function": node.name,
                        "count": param_count,
                    })
        return issues

