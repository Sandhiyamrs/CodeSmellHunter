import ast
from codesmellhunter.smells.many_params import ManyParameters


def test_many_parameters():
    code = "def f(a,b,c,d,e): pass"
    tree = ast.parse(code)

    smell = ManyParameters(4)
    issues = smell.detect(tree, "test.py")

    assert len(issues) == 1
