from pathlib import Path
from typing import Union, List, Optional, Iterable

EXCLUDED_SUFFIXES = (".bin", ".img")

def get_human_readable_files(
        path: Union[str, Path],
        target_extensions: Optional[Iterable[str]] = None
    ) -> List[Path]:
    """
    Return a list of human-readable files under the given path.

    Only includes:
    + Regular files (no directories).
    + Non-hidden files (no dotfiles or files in hidden folders like '.git').
    + Files with extensions not in EXCLUDED_SUFFIXES.

    :param path: A string or pathlib.Path object representing the path to search.
    :param target_extensions: Optional iterable of file extensions to include (e.g., {".md", ".txt"}).
    :return: List of pathlib.Path objects.
    :raises FileNotFoundError: If the given path does not exist.
    :raises ValueError: If `path` is not a str or pathlib.Path.
    """

    if not isinstance(path, (str, Path)):
        raise ValueError("Expected str or pathlib.Path for `path`.")
    
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")

    # Normalize extensions for case-insensitive matching.
    excluded = {ext.lower() for ext in EXCLUDED_SUFFIXES}
    allowed = {ext.lower() for ext in target_extensions} if target_extensions else None

    # Get human-readable files.
    files = [
        item for item in path.rglob("*")
        if item.is_file()
        and not any(part.startswith('.') for part in item.parts)
        and item.suffix.lower() not in excluded
        and (allowed is None or item.suffix.lower() in allowed)
    ]

    return files
