# Shared Python Utility Module (`shared_utils`)

[![CI](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A standardized, lightweight, and thoroughly tested shared Python utility library designed for use across internal services and team repositories.

---

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
  - [1. `slugify`](#1-slugify)
  - [2. `truncate_words`](#2-truncate_words)
  - [3. `camel_to_snake` & `snake_to_camel`](#3-camel_to_snake--snake_to_camel)
- [Running Tests](#running-tests)
- [Contribution & Branching Strategy](#contribution--branching-strategy)
- [License](#license)

---

## Overview

As our engineering team grows, common helper functions often get re-implemented in multiple services. This package consolidates frequently used utility functions into a single shared, versioned repository with strict test coverage, type annotations, and clean git history.

### Key Highlights
- **Zero External Runtime Dependencies:** Uses only Python's standard library.
- **Type Annotated:** Fully compatible with `mypy` and modern IDE autocomplete.
- **100% Test Coverage:** Unit tested with edge cases and Unicode support.
- **PEP 517/621 Compliant:** Modern packaging configuration via `pyproject.toml`.

---

## Directory Structure

```text
.
├── .gitignore                    # Python git ignore rules
├── pyproject.toml                # Project packaging and metadata
├── setup.py                      # Compatibility installation script
├── README.md                     # Documentation and usage guide
├── shared_utils/                 # Source package directory
│   ├── __init__.py               # Package exports and version metadata
│   └── string_utils.py           # Core string helper functions
└── tests/                        # Automated unit test suite
    ├── __init__.py
    └── test_string_utils.py      # Test cases for string utilities
```

---

## Installation

### Editable / Local Development Mode

Clone the repository and install in editable mode with development dependencies:

```bash
git clone <REPO_URL>
cd <REPO_NAME>
pip install -e ".[dev]"
```

### Direct Installation

Install directly into your Python environment:

```bash
pip install .
```

---

## Usage Guide

Import the desired utility functions directly from `shared_utils`:

```python
from shared_utils import slugify, truncate_words, camel_to_snake, snake_to_camel
```

### 1. `slugify`

Transforms arbitrary strings into clean, URL-safe slugs with Unicode normalization and custom separator support.

```python
from shared_utils import slugify

# Basic slugification
slug = slugify("Hello World! Welcome to Team Utilities.")
print(slug)
# Output: 'hello-world-welcome-to-team-utilities'

# Custom separator
slug_custom = slugify("Category / Sub Category", separator="_")
print(slug_custom)
# Output: 'category_sub_category'

# Accented characters
slug_accents = slugify("Café au Lait")
print(slug_accents)
# Output: 'cafe-au-lait'

# Preserving Unicode characters
slug_unicode = slugify("Café au Lait", allow_unicode=True)
print(slug_unicode)
# Output: 'café-au-lait'
```

### 2. `truncate_words`

Truncates a string after a specified word limit, appending a customizable indicator.

```python
from shared_utils import truncate_words

description = "The quick brown fox jumps over the lazy sleeping dog in the forest"
print(truncate_words(description, max_words=5))
# Output: 'The quick brown fox jumps...'

print(truncate_words(description, max_words=3, suffix=" [read more]"))
# Output: 'The quick brown [read more]'
```

### 3. `camel_to_snake` & `snake_to_camel`

Bidirectional case conversion for API payloads and internal object models.

```python
from shared_utils import camel_to_snake, snake_to_camel

# CamelCase to snake_case
print(camel_to_snake("userProfileData"))
# Output: 'user_profile_data'

print(camel_to_snake("HTTPResponseCode"))
# Output: 'http_response_code'

# snake_case to camelCase / PascalCase
print(snake_to_camel("user_profile_data"))
# Output: 'userProfileData'

print(snake_to_camel("user_profile_data", capitalize_first=True))
# Output: 'UserProfileData'
```

---

## Running Tests

Run the test suite using `unittest` (standard library, no extra dependencies):

```bash
python -m unittest discover -s tests -v
```

Or using `pytest`:

```bash
pytest
```

To run with coverage reporting:

```bash
pytest --cov=shared_utils tests/
```

---

## Contribution & Branching Strategy

To maintain a clean and reliable codebase, all team members follow our Pull Request workflow:

1. **Branch Naming Convention**:
   - `feature/<feature-name>` for new capabilities
   - `bugfix/<issue-description>` for bug fixes
   - `docs/<description>` for documentation updates

2. **Commit Message Format**:
   Follow Conventional Commits:
   - `feat: add slugify utility with unicode normalization`
   - `test: add unit tests for string utility functions`
   - `docs: update README with usage examples and PR guidelines`

3. **Pull Request Workflow**:
   ```bash
   # 1. Switch to main and pull latest changes
   git checkout main
   git pull origin main

   # 2. Create a feature branch
   git checkout -b feature/string-utils

   # 3. Commit changes
   git add .
   git commit -m "feat: implement initial string utility module"

   # 4. Push to remote
   git push origin feature/string-utils

   # 5. Open Pull Request on GitHub to merge feature/string-utils into main
   # 6. Address review feedback and merge
   ```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
