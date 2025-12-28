
import argparse
from analyzer import CodeAnalyzer
from config import load_config
from report import ReportGenerator


def main():
    parser = argparse.ArgumentParser(description="CodeSmellHunter - Static Code Analysis Tool")
    parser.add_argument("file", help="Python source file to analyze")
    parser.add_argument("--output", default="output/report.json", help="Output report file")
    args = parser.parse_args()

    config = load_config()
    analyzer = CodeAnalyzer(config)
    smells = analyzer.analyze(args.file)

    report = ReportGenerator()
    report.generate(smells, args.output)

    print(f"Analysis complete. Found {len(smells)} issues.")
    print(f"Report saved to {args.output}")


if __name__ == "__main__":
    main()
