"""
Return copy-paste-ready output in Markdown format.

## Main Function

`generate_markdown_output(index_file_unreferenced_links: List, broken_links: Dict)`.

:param index_file_unreferenced_links: A list of human-readable files not referenced
    in the main index file but exist in the index file's directory. Example:
    
    ["./assembly/instructions/mov.md", "./projects/README.md", "./resources/output.png"]

:param broken_links: A dictionary with the filename as the key and a list of broken links
    in the file as the value. Example:

    {
        "SUMMARY.md": [
            "Line 13: scripts/setup.sh",
            "Line 52: assembly/mov.md"
        ],

        "./projects/README.md": [
            "Line 10: ../resources/image.png"
        ]
    }
"""

from typing import List, Dict, Optional
import os

def generate_markdown_report(
        unreferenced_files: List[str],
        broken_links: Optional[Dict] = None,
        *,
        main_index_file: str = "SUMMARY.md"
    ):

    markdown_output = []

    # Unreferenced files in main index file.
    markdown_output.append(
        md_heading(f"Unreferenced files in {main_index_file}", 2)
    )

    if len(unreferenced_files) == 0:
        markdown_output.append("**None**\n")

    else:
        for file in unreferenced_files:
            markdown_output.append(
                md_list_item_link(os.path.basename(file), file)
            )

    return "".join(markdown_output)

def md_link(text: str, target: str) -> str:
    return f"[{text}]({target})"

def md_heading(text: str, level: int = 2) -> str:
    return f"\n{'#' * level} {text}\n\n"

def md_list_item(text: str) -> str:
    return f"+ {text}\n"

def md_list_item_link(text: str, target: str) -> str:
    return md_list_item(md_link(text, target))
