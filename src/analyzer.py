
import ast
from smells.long_method import LongMethodDetector
from smells.deep_nesting import DeepNestingDetector
from smells.many_params import ManyParamsDetector
from smells.magic_numbers import MagicNumberDetector
from smells.large_class import LargeClassDetector


class CodeAnalyzer:
    def __init__(self, config):
        self.config = config
        self.detectors = [
            LongMethodDetector(config),
            DeepNestingDetector(config),
            ManyParamsDetector(config),
            MagicNumberDetector(config),
            LargeClassDetector(config),
        ]

    def analyze(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())

        results = []
        for detector in self.detectors:
            results.extend(detector.detect(tree, file_path))

        return results
