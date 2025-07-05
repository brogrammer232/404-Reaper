# 404 Reaper

> **Random Quote:** It's not what we do once in a while that shapes our lives. It's what we do consistently.

**404 Reaper** is a tool that tracks down broken links and missing files in your documentation. Built for fast-growing repositories, it keeps your index files sharp and your references intact.

This tool follows the principle of minimal friction. It doesn't try to be overly smart or take control away from the user; it simply gives you the information and options you need to keep your docs clean and functional.

## Key Topics

+ [Project Goal](#project-goal)
+ [Features](#features)
    - [Core Functionality](#core-functionality)
        - [Sample Output](#sample-output)
    - [Future Features](#future-features)
+ [File Handling Rules](#file-handling-rules)
    - [Index Files](#index-files)
    - [Link Format](#link-format)
    - [File Types Scanned](#file-types-scanned)

---

## Project Goal

As repositories grow, manually maintaining index files and checking for broken links becomes tedious, time-consuming, and error-prone. This tool automates that process by:

+ Verifying that `SUMMARY.md` contains links to all other files (except binary files).
+ Generating copy-paste-ready entries for missing links.
+ Scanning all relevant files for broken internal links.
+ Offering cleanup options for broken links.

---

## Features

### Core Functionality

+ **Detect missing files in `SUMMARY.md`**: Scan the repository for files not listed in `SUMMARY.md`. Output results in markdown format, ready to paste into the index.

+ **Check for broken links**: In all `.md` files, check for links that point to non-existent files.

+ **Optional fixing**: Optionally remove broken links using a flag:
    - Delete the entire line containing the link, or
    - Remove only the link syntax, preserving the visible text.

+ **Generate structured reports**:
    + Output summary to terminal (e.g., number of issues found).
    + Write a full report to a `report.md` file, categorized by:
        - Missing files in `SUMMARY.md`.
        - Broken links (categorize by file).

#### Sample Output

```markdown
## Missing Files in SUMMARY.md

+ [mov.md](assembly/instructions/mov.md)
+ [setup.sh](scripts/setup.sh)

## Broken Links

### SUMMARY.md

+ Line 12: `[file.md](obsolete/file.md)`

### notes/registers.md

+ Line 5: `[Stack Info](stack/overview.md)`
```

### Future Features

+ Check for broken section links (e.g., `#heading-one`).
+ GitHub remote repo scanning.
+ Auto-sorting index entries.
+ GitHub Action for CI-based link validation.

---

## File Handling Rules

### Index Files

+ `SUMMARY.md` (main index): Will contain links to all human-readable files in the repository such as `.md`, `.asm`, `.c` and `.sh`. It will not contain links to binary files. Located in root.
+ Other notes files: May contain links to any files that are appropriate in the context (complementary notes or images).

### Link Format

+ Only `[Title](relative/path/to/file.ext)` format is supported for text files. The variation for image files is supported as well.
+ All links are relative to the current file's directory.
+ Section links (`#heading`) are ignored for now.

### File Types Scanned

+ Human-readable files only (e.g., `.md`, `.asm`, `.c`, `.sh`, `txt`).
+ Binary/object files are ignored.
