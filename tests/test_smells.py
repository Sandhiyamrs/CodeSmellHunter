import ast
from codesmellhunter.smells.long_method import LongMethod

def test_long_method():
    code = "def a():\n" + "\n".join([" pass"] * 50)
    tree = ast.parse(code)
    smell = LongMethod(40)
    assert len(smell.detect(tree, "test.py")) == 1
