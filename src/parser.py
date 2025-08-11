"""
Parses a Markdown file and extracts all relevant links.

Currently supports:
    - Links to other files: [File](file.md)
    - Image links:          ![Image](image.png)
    - Section links:        [Section](#section)

The primary function, `extract_links_from_file()`, returns a list of tuples
with the following structure:

    (link_text, link_target)

Example:
    [("Registers", "assembly/registers.md"), ("no alt text", "img/cpu.png")]
"""

from markdown_it import MarkdownIt
from pathlib import Path
from typing import Union, List, Tuple

def extract_links_from_file(file: Union[str, Path]) -> List[Tuple[str, str]]:
    """
    Extract and return links from the given file.
    
    :param file: A string or pathlib.Path object representing the file to extract links from.
    :return: A list of tuples with this format: (link_text, link).
    :raises ValueError: If `file` is not str or pathlib.Path.
    """

    if not isinstance(file, (str, Path)):
        raise ValueError("Expected str or pathlib.Path for `file`.")

    #  Read markdown content from file as UTF-8 text.
    file = Path(file)
    file_contents = read_file(file)

    # Extract links from markdown text.
    links = extract_links_from_text(file_contents)

    return links

def read_file(file: Path) -> str:
    """
    Read the given file and return its contents.

    :param file: A pathlib.Path object representing the file to read.
    :return: A string containing the contents of the given file.
    :raises FileNotFoundError: If `file` does not exist.
    """

    if not file.is_file():
        raise FileNotFoundError(f"File not found: {file}")

    return file.read_text(encoding = "utf-8")

def extract_links_from_text(text: str) -> List[Tuple[str, str]]:
    """
    Extract links from the given text.

    :param text: A markdown-style string.
    :return: A list of tuples with this format: (link_text, link).
    """

    md = MarkdownIt()
    tokens = md.parse(text)
    links = []

    for token in tokens:
        if token.type != "inline":
            continue

        children_iter = iter(token.children)
        for child in children_iter:
            # Get section links and links to text files.
            if child.type == "link_open":
                link_target = child.attrGet("href")
                if not link_target: continue
                
                text_token = next(children_iter, None)
                link_text = (
                    text_token.content.strip()
                    if text_token
                    and text_token.type == "text"
                    else "no link text"
                )

                links.append((link_text, link_target))

            # Get image links.
            elif child.type == "image":
                src = child.attrGet("src")
                alt = child.attrGet("alt") or "no alt text"

                links.append((alt, src))

    return links
