# Markdown Link Parsing Library Selection

This document outlines the evaluation and selection of a Markdown parsing library for the `404 Reaper` project. The goal was to identify a tool capable of accurately and reliably extracting all relevant links from Markdown files; including file links (`[text file](file.md)`), image links (`![image file](image.png)`), and section links (`#heading`); with a focus on **scalability and correctness**.

---

## Evaluated Libraries

The following libraries were considered:

+ [`re`](#re)
+ [`mistune`](#mistune)
+ [`markdown` / `markdown2`(with `BeautifulSoup`)](#markdown--markdown2-with-beautifulsoup)
+ [`markdown-it-py` (Selected)](#markdown-it-py-selected)

---

### `re`

**Status:** Eliminated

**Reason for Rejection:**

+ Regex cannot reliably parse Markdown due to its complexity (e.g., nested brackets, escaped characters, inline images, and multiline links).
+ Impossible to maintain over time as Markdown features expand.
+ Would require building a parser manually from scratch; which defeats the purpose of using a library.

---

### `mistune`

**Status:** Eliminated

**Reason for Rejection:**

+ Lightweight and fast, but lacks strict conformance to the Markdown spec (CommonMark).
+ Requires additional logic or plugins to extract all link types (e.g., image links, heading anchors).
+ Tokenization model is fast but not as structured or spec-compliant as needed.
+ Good for rendering or speed-critical environments, but not ideal when correctness and long-term extensibility are priorities.

---

### `markdown` / `markdown2` (with `BeautifulSoup`)

**Status:** Eliminated

**Reason for Rejection:**

+ These libraries render Markdown to HTML, requiring a second pass through an HTML parser (e.g., `BeautifulSoup`) to extract links.
+ Indirect and inefficient.
+ Inaccurate parsing of non-standard Markdown or advanced syntax.
+ HTML parsers are not aware of Markdown semantics and cannot differentiate between link types easily.

---

### `markdown-it-py` (Selected)

**Why It Was Chosen:**

+ Fully compliant with the [CommonMark specification](https://commonmark.org/) and supports [GitHub-Flavored Markdown (GFM)](https://github.github.com/gfm/) via plugins.
+ Converts Markdown into a structured **token stream**, providing detailed access to every element (e.g., `link_open`, `text`, `image`, `heading_open`).
+ Handles:
    + Standard links: `[label](file.md)`
    + Section links: `[Section](#heading)`
    + Image links: `![alt text](img.png)`
    + Escaped characters, nesting, and other edge cases
+ Offers a **plugin system** for future extensions like tables, checkboxes, math, and more.
+ Actively maintained and widely adopted in modern tooling (e.g., Jupyter Book, MyST Parser).
+ Future-proof for CI use, GitHub-flavored Markdown parsing, and structured scanning at scale.

In summary, `markdown-it-py` provides the best balance of performance, accuracy, extensibility, and active development. It is the most robust and scalable choice for link extraction and validation in Markdown documentation repositories.
