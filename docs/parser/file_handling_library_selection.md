# File Handling Library Selection

This document outlines the evaluation and selection of a file path and reading approach for the `404 Reaper` project. The goal was to identify a clean, robust, and scalable way to handle filesystem paths and read file contents, especially Markdown files, without introducing unnecessary complexity or bugs.

---

## Evaluated Options

The following approaches were considered:

+ [`open()` with string paths](#open-with-string-paths)
+ [`pathlib` (Selected)](#pathlib-selected)

---

### `open()` with string paths

**Status:** Eliminated

**Reason for Rejection:**

+ Requires verbose boilerplate (`with open(path, "r") as f:`) for every file read.
+ Inconsistent with modern path manipulations using `pathlib` objects.
+ More error-prone when composing or resolving paths dynamically.
+ Introduces unnecessary cognitive overhead when converting between `str` and `Path` objects.
+ Lacks built-in helpers like `.read_text()` or `.read_bytes()`, leading to repeated low-level handling of files.

While functionally adequate and widely supported, `open()` is less expressive, less elegant, and harder to maintain in larger or cleaner codebases.

---

### `pathlib` (Selected)

**Why It Was Chosen:**

+ Fully integrates file path construction and file reading into one consistent API.
+ Improves code clarity with one-liner methods like `path.read_text(encoding="utf-8")`.
+ Reduces boilerplate and removes the need to manually open and close files.
+ Encourages a uniform code style, reducing bugs caused by mixing `str` paths and `Path` objects.
+ Safer and more readable for line-by-line use cases via `path.open()` when needed.

---
