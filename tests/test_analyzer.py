from codesmellhunter.analyzer import Analyzer
from codesmellhunter.loader import load_smells
from codesmellhunter.config import load_config


def test_analyzer_runs(tmp_path):
    file = tmp_path / "test.py"
    file.write_text("def a(x,y,z,q,w): return x+y")

    analyzer = Analyzer(load_smells(load_config()))
    result = analyzer.analyze(tmp_path)

    assert "issues" in result
    assert isinstance(result["issues"], list)
