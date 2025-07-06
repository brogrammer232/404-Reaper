from typing import Union
from pathlib import Path

EXCLUDED_SUFFIXES = (".bin",)

def get_human_readable_files(path: Union[str, Path]) -> list[Path]:
    """
    Return a list of human-readable files under the given path.

    Only includes:
    + Regular files (no directories).
    + Non-hidden files (no dotfiles or files in hidden folders).
    + Files with extensions not in the EXCLUDED_SUFFIXES list.

    :param path: A string or pathlib.Path object representing the root directory.
    :return: List of pathlib.Path objects.
    """

    # Type checking.
    if not isinstance(path, (str, Path)):
        raise ValueError("Expected str or pathlib.Path for `path`.")

    # Getting human-readable files.
    path = Path(path)

    files = [
        item for item in path.rglob("*")    # Get all files and directories.
        if item.is_file()                   # Remove all directories.
        and not any(part.startswith('.') for part in item.parts)    # Remove hidden files and files in hidden folders.
        and item.suffix not in EXCLUDED_SUFFIXES      # Remove files with unwanted extensions.
    ]

    return files
