import ast


def get_node_name(node):
    if isinstance(node, ast.FunctionDef):
        return node.name
    if isinstance(node, ast.ClassDef):
        return node.name
    return "unknown"

