from pathlib import Path


def find_python_files(path):
    """
    Recursively find all Python files in a directory or return single file.
    """
    path = Path(path)

    if path.is_file() and path.suffix == ".py":
        return [path]

    if path.is_dir():
        return list(path.rglob("*.py"))

    return []


def read_file_safe(filepath):
    """
    Read file content safely (avoids crashing on encoding issues).
    """
    try:
        return filepath.read_text(encoding="utf-8")
    except Exception:
        return ""


def is_test_file(filepath):
    """
    Identify test files to optionally skip.
    """
    return "test" in filepath.name.lower()
