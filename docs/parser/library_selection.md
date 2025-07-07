# Markdown Link Parsing Library Selection

This document outlines the evaluation and selection of a Markdown parsing library for the `404 Reaper` project. The goal was to identify a tool capable of accurately and reliably extracting all relevant links from Markdown files; including file links (`[text file](file.md`), image links (`![image file](image.png)`), and section links (`#heading`); with a focus on **scalability and correctness**.

---

## Evaluated Libraries

The following libraries were considered:

+ [`re`](#re)
+ [`mistune`](#mistune)
+ [`markdown` / `markdown2`(with `BeautifulSoup`)](#markdown--markdown2-with-beautifulsoup)
+ [`commonmark` (Selected)](#commonmark-selected)

### `re`

**Status:** Eliminated

**Reason for Rejection:**

+ Regex cannot reliably parse Markdown due to its complexity (e.g., nested brackets, escaped characters, inline images, and multiline links).
+ Impossible to maintain over time as Markdown features expand.
+ Would require building a parser manually from scratch; which defeats the purpose of using a library.

### `mistune`

**Status:** Eliminated

**Reason for Rejection:**

+ Lightweight and fast, but lacks strict conformance to the Markdown spec (CommonMark).
+ Requires additional logic or plugins to extract all link types (e.g., image links, heading anchors).
+ Tokenization model is fast but not as structured as an abstract syntax tree (AST).
+ Good for rendering or speed-critical environments, but not ideal when correctness and future extensibility are more important than speed.

### `markdown` / `markdown2` (with `BeautifulSoup`)

**Status:** Eliminated

**Reason for Rejection:**

+ These libraries render Markdown to HTML, requiring a second pass through an HTML parser (e.g., `BeautifulSoup`) to extract links.
+ Indirect and inefficient.
+ Inaccurate parsing of non-standard Markdown or advanced syntax.
+ HTML parsers are not aware of Markdown semantics and cannot differentiate between link types easily.

### `commonmark` (Selected)

**Why It Was Chosen:**

+ Fully compliant with the [CommonMark specification](https://commonmark.org/), ensuring long-term accuracy.
+ Converts Markdown into a structured **abstract syntax tree (AST)**, making it easy to traverse and extract all link-related nodes (e.g., `link`, `image`, `heading`).
+ Handles:
    + Standard links: `[label](file.md)`
    + Section links: `[Section](#heading)`
    + Image links: `![alt text](img.png)`
    + Escaped characters, nesting, and other edge cases
+ Minimal but focused library. No bloated features or renderers.
+ Easier to upgrade in future if additional Markdown features (tables, code refs, embedded HTML) need to be parsed.
+ Future-proof for CI use, large-scale scans, and extension (e.g., GitHub-style anchors or section heading validation).

While slightly slower than lightweight alternatives like `mistune`, its correctness, standards compliance, and structured parsing make it the best fit for a robust and scalable documentation link validation tool.
