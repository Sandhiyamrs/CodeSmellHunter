from src.analyzer import CodeAnalyzer
from src.config import load_config


def test_analysis_runs():
    analyzer = CodeAnalyzer(load_config())
    results = analyzer.analyze("samples/bad_code.py")
    assert len(results) > 0

