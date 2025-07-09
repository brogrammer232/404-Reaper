"""
This module should take a markdown file and return a list of links in the file.

Return the following links:
    + Links to other files: '[File](file.md)'
    + Links to images: '![Image](image.png)'

Section links will come soon.

Algorithm:
    1. Read the file.
    2. Use `markdown-it-py` to extract the links.
    3. Return the links.
"""
from markdown_it import MarkdownIt
from pathlib import Path
from typing import Union

def get_links(file: Union[str, Path]) -> list[tuple]:
    """
    Extract and return links from the given file.

    Only includes:
    + Links to other text files.
    + Links to images.
    
    :param file: A string or pathlib.Path object representing the file to extract links from.
    :return: A list of tuples with this format: (link_text, link).
    """

    # Check parameter type.
    if not isinstance(file, (str, Path)):
        raise ValueError("Expected str or pathlib.Path for `file`.")

    # Get file contents.
    file = Path(file)
    file_contents = read_file(file)

    # Extract links.
    links = extract_links(file_contents)

    return links

def read_file(file: Path) -> str:
    """
    Read the given file and return its contents.

    :param file: A pathlib.Path object representing the file to read.
    :return: A string containing the contents of the given file.
    """

    # Error handling.
    if not file.is_file():
        raise FileNotFoundError("The given file doesn't exist.")

    return file.read_text(encoding = "utf-8")

def extract_links(text: str) -> list[tuple]:
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
            if child.type == "link_open":
                link = child.attrGet("href")
                
                text_token = next(children_iter, None)
                text = text_token.content if text_token and text_token.type == "text" else ""

                links.append((text, link))

            elif child.type == "image":
                src = child.attrGet("src")
                alt = child.attrGet("alt") or "no alt text"

                links.append((alt, src))

    return links
