import ast


class DeepNestingDetector(ast.NodeVisitor):
    def __init__(self, config):
        self.max_depth = config["MAX_NESTING_DEPTH"]
        self.issues = []
        self.file_path = None

    def detect(self, tree, file_path):
        self.file_path = file_path
        self.visit(tree)
        return self.issues

    def generic_visit(self, node, depth=0):
        if depth > self.max_depth:
            self.issues.append({
                "type": "Deep Nesting",
                "file": self.file_path,
                "line": getattr(node, "lineno", None),
                "depth": depth,
            })
        for child in ast.iter_child_nodes(node):
            self.generic_visit(child, depth + 1)

