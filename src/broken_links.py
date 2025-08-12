"""
This module takes a list of links and returns a list of broken links.

+ Take a file.
+ Read the file.
+ Extract links.
+ Check for broken links.
+ Return a list of broken links or None.
"""

from parser import extract_links_from_file
from typing import Union
from pathlib import Path

def get_broken_links(file: Union[str, Path]) -> list[str]:

    if not isinstance(file, (str, Path)):
        raise ValueError("Expected str or pathlib.Path for `file`.")

    file = Path(file)

    if not file.is_file():
        raise FileNotFoundError(f"File does not exist or is a directory: {file}")

    # Extract links from the given markdown file.
    links = extract_links_from_file(file)

def get_broken_file_links(file_links: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """
    Go through "file links" and scan for broken links.
    Have a similar function for section links: `get_broken_section_links`.
    """
    pass
