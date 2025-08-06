"""
Get human-readable files existing in the repository, but not referenced
in `SUMMARY.md`.
"""

from scanner import get_human_readable_files
from parser import extract_links_from_file

# Get human-readable files in the repo.
repo_root = "./test_repo"
human_readable_files = get_human_readable_files(repo_root)

human_readable_files = [
        "./" + str(file.relative_to(repo_root)) # Express the path relative to the repository's root.
        for file in human_readable_files[:]
        if file.name != "SUMMARY.md"            # Remove `SUMMARY.md`.
    ]

# for file in human_readable_files: print(file)
# print()

# Get links from `SUMMARY.md`.
summary_file = "./test_repo/SUMMARY.md"
referenced_links = extract_links_from_file(summary_file)
link_targets = [
        link[-1] if link[-1].startswith("./") else f"./{link[-1]}"
        for link in referenced_links
    ]

# for link in link_targets: print(link)

# Get missing files.

human_readable_files_num = len(human_readable_files)
referenced_files_num = len(link_targets)
missing_files_number = human_readable_files_num - referenced_files_num

print(f"{missing_files_number} files missing in `SUMMARY.md`.")

missing_files = human_readable_files - link_targets

for file in missing_files: print(file)
