"""
mcp-repo-context: Codebase search and structural context.
Allowed: file listing, symbol search, grep, file read.
Forbidden: writes, deletes, git mutations.
"""
import os
import subprocess

REPO_ROOT = os.environ.get("REPO_ROOT", "/home/arnieai/soberfuture")


def list_files(path: str = "", extensions: list[str] | None = None) -> list[str]:
    target = os.path.join(REPO_ROOT, path)
    results = []
    for root, _, files in os.walk(target):
        for f in files:
            if extensions is None or any(f.endswith(e) for e in extensions):
                results.append(os.path.join(root, f).replace(REPO_ROOT, ""))
    return results


def grep(pattern: str, path: str = "") -> str:
    target = os.path.join(REPO_ROOT, path)
    result = subprocess.run(
        ["grep", "-rn", "--include=*.py", "--include=*.ts", "--include=*.md", pattern, target],
        capture_output=True, text=True
    )
    return result.stdout[:4000]


def read_file(relative_path: str) -> str:
    full = os.path.join(REPO_ROOT, relative_path.lstrip("/"))
    with open(full, "r", encoding="utf-8") as f:
        return f.read()


def health():
    return {"status": "ok", "service": "mcp-repo-context"}
