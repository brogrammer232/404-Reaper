"""
Identify human-readable files that exist in a directory but are not linked in a given index file.

This module provides functionality to compare the set of human-readable files within
an index file's directory (and optionally its subdirectories) against the links
listed in that index file.

Definitions and assumptions:
- A "human-readable file" is defined by the `scanner.get_human_readable_files` function.
- The index file contains only valid links (no broken or duplicate links).
- The index file contains fewer or an equal number of links compared to the number
  of human-readable files in the directory.

Main function:
- `get_unreferenced_files(index_file, recursive=True)`: Returns a list of files that are
  present in the directory but not referenced in the index file.

Future enhancements:
- Option to restrict searches to the index file's immediate directory (non-recursive mode).
"""

from scanner import get_human_readable_files
from parser import extract_links_from_file
from typing import Union, List
from pathlib import Path

def get_unreferenced_files(index_file: Union[str, Path], recursive: bool = True) -> List[str]:
    """
    Return a list of human-readable files that exist in the index file's directory (and optionally its subidirectories) but are not referenced in the index file.

    Link targets are normalized to always start with "./" for comparison.

    :param index_file: Path to the Markdown index file to check.
    :param recursive: Whether to search subdirectories of the index file's directory.
        (Currently unused; preserved for future functionality.)
    :return: A list of unreferenced file paths as strings, relative to the index file's directory.
    :raises ValueError: If `index_file` is not a string or Path.
    """

    # Check parameter type.
    if not isinstance(index_file, (str, Path)):
        raise ValueError("Expected str or pathlib.Path for `index_file`.")

    index_file = Path(index_file)
    target_directory = index_file.parent

    # Collect all human-readable files (excluding the index file),
    # convert them to relative strings, and ensure they have a "./" prefix.
    human_readable_files = [
            normalize_link_target(str(file.relative_to(target_directory)))
            for file in get_human_readable_files(target_directory)
            if file.name != index_file.name
        ]

    # Extract link targets from the index file and normalize them.
    referenced_links = [
            normalize_link_target(link[-1])
            for link in extract_links_from_file(index_file)
        ]

    # Get files that exist locally but are not referenced in the index file.
    unreferenced_files = list(set(human_readable_files) - set(referenced_links))

    unreferenced_files_num = len(unreferenced_files)
    print(f"{unreferenced_files_num} files missing in `{index_file.name}`.")
    
    return unreferenced_files

def normalize_link_target(link: str) -> str:
    """
    Ensure a relative link target is prefixed with "./" for consistency.

    :param link: The link target string to normalize.
    :return: The normalized link target, guaranteed to start with "./".
    """

    return link if link.startswith("./") else f"./{link}"
