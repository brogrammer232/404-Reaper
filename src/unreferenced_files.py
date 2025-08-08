"""
Get human-readable files not referenced in the given file, but exist within the
file's directory (including child directories).

The main function, `get_missing_files()` returns a list of links to
human-readable files that exist in the directory but are not referenced in
the given file.

Assumptions about the given file:
    + Contains less than or an equal number of links as
        the number of human-readable files in the directory.
    + Does not contain any broken links.
    + Does not contain duplicate links (multiple links pointing to the same file).

Future prospects:
    + Have an option of searching only the file's directory or including
    children directories.
"""

from scanner import get_human_readable_files
from parser import extract_links_from_file
from typing import Union, List
from pathlib import Path

def get_unreferenced_files(index_file: Union[str, Path], recursive: bool = True) -> List[str]:

    index_file = Path(index_file)
    target_directory = index_file.parent

    # Get human-readable files in the repo.
    human_readable_files = get_human_readable_files(target_directory)
    
    ## Convert paths to string, express relative to the target directory,
    ## and remove the index file.
    human_readable_files = [
            "./" + str(file.relative_to(target_directory))
            for file in human_readable_files
            if file.name != index_file.name
        ]

    # Extract links from the given index file.
    referenced_links = [
            normalize_link_target(link)
            for link in extract_links_from_file(index_file)
        ]

    # Get missing files.
    missing_files = list(set(human_readable_files) - set(referenced_links))

    missing_files_num = len(missing_files)
    print(f"{missing_files_num} files missing in `{index_file.name}`.")
    
    return missing_files

def normalize_link_target(link_tuple):
    """
    This function returns a string of the link target.
    It ensures that the link target starts with "./".
    """

    target = link_tuple[-1]
    return target if target.startswith("./") else f"./{target}"
