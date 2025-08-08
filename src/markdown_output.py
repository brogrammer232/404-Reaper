"""
Output copy-paste-ready output in Markdown format, either in a file,
or on the terminal.

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

from typing import List, Dict

def generate_markdown_output(index_file_unreferenced_links: List, broken_links: Dict):
