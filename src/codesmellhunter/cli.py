import argparse
from codesmellhunter.config import load_config
from codesmellhunter.loader import load_smells
from codesmellhunter.analyzer import Analyzer
from codesmellhunter.report import generate_report

def main():
    parser = argparse.ArgumentParser("CodeSmellHunter")
    parser.add_argument("path")
    parser.add_argument("--output", default="output/report.json")
    args = parser.parse_args()

    config = load_config()
    smells = load_smells(config)
    analyzer = Analyzer(smells)

    results = analyzer.analyze(args.path)
    generate_report(results, args.output)
    print(f"✔ Scan complete. {len(results)} issues found.")

if __name__ == "__main__":
    main()
