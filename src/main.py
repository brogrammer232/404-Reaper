from pathlib import Path
from scanner import get_human_readable_files

repo_root = Path("./repo_clone")

files = get_human_readable_files(repo_root)

for file in files: print(file)
