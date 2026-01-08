import ast


class CodeMetrics:
    def __init__(self):
        self.loc = 0
        self.functions = 0
        self.classes = 0
        self.complexity = 0

    def analyze(self, source_code):
        """
        Analyze raw source code and compute metrics.
        """
        self.loc = len([
            line for line in source_code.splitlines()
            if line.strip() and not line.strip().startswith("#")
        ])

        tree = ast.parse(source_code)
        self._walk(tree)

        return {
            "loc": self.loc,
            "functions": self.functions,
            "classes": self.classes,
            "cyclomatic_complexity": self.complexity
        }

    def _walk(self, node):
        """
        Walk AST to calculate metrics.
        """
        if isinstance(node, ast.FunctionDef):
            self.functions += 1

        if isinstance(node, ast.ClassDef):
            self.classes += 1

        if isinstance(node, (
            ast.If,
            ast.For,
            ast.While,
            ast.And,
            ast.Or,
            ast.ExceptHandler
        )):
            self.complexity += 1

        for child in ast.iter_child_nodes(node):
            self._walk(child)
