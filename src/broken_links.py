"""
This module takes a list of links and returns a list of broken links.

+ Take a file.
+ Read the file.
+ Extract links.
+ Check for broken links.
+ Return a list of broken links or None.
"""

from parser import extract_links_from_file
from pathlib import Path

def get_broken_links(file: str | Path) -> list[str]:

    file = Path(file)

    if not file.is_file():
        raise FileNotFoundError(f"File not found or is not a regular file: {file}")

    links = extract_links_from_file(file)

    broken_file_links = get_broken_file_links(links["file links"], file.parent.resolve())

    for link in broken_file_links: print(link)

def get_broken_file_links(
    file_links: list[tuple[str, str]],
    base_dir: Path
) -> list[tuple[str, str]]:
    """
    Filter `file_links` to only include broken links.
    """

    return [
        link for link in file_links
        if not (base_dir / link[-1]).resolve().exists()
    ]

def get_broken_section_links():
    pass
