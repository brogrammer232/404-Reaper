from scanner import get_human_readable_files
from parser import get_links
from pathlib import Path

# Test scanner.
# repo_root = Path("./repo_clone")
# files = get_human_readable_files(repo_root)
# for file in files: print(file)

# Test parser.
test_file1 = Path("./repo_clone/SUMMARY.md")
test_file2 = Path("./test.md")
links = get_links(test_file1)

for link in links:
    print(link)
