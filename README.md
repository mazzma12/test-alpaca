# test-alpaca 🦙
[![PyPI version](https://badge.fury.io/py/test-alpaca.svg)](https://badge.fury.io/py/test-alpaca/)
[![Python versions](https://img.shields.io/pypi/pyversions/test-alpaca.svg)](https://pypi.org/project/test-alpaca/)
[![Code Quality](https://github.com/mazzma12/test-alpaca/workflows/Code%20Quality/badge.svg)](https://github.com/mazzma12/test-alpaca/actions?query=workflow%3A"Code+Quality")
[![Documentation](https://github.com/mazzma12/test-alpaca/workflows/Documentation/badge.svg)](https://mazzma12.github.io/test-alpaca)

A fun CLI tool that displays messages with ASCII alpacas - like cowsay but with alpacas!

```
 ________________
< Safer, Together! >
 ----------------
        /|   /|
       ( :v:  )
        |(_)|
        --m--m--
```

## Features

- 🦙 **Three unique alpaca designs** - default, happy, and thinking
- 🌈 **Color support** - make your alpacas colorful
- 📏 **Customizable width** - control the speech bubble size
- 📁 **File input** - read messages from files
- 🔧 **Pipe support** - works with stdin
- 🛡️ **Special message** - built-in "Safer, Together!" message

## Installation

### From PyPI

```bash
pip install test-alpaca
```

### Using Docker

```bash
# Quick run with Docker
docker run --rm -it ghcr.io/mazzma12/test-alpaca:latest "Hello from Docker!"

# Build locally
docker build -t test-alpaca .
docker run --rm test-alpaca "Your message here"

# Using docker-compose
docker-compose up test-alpaca
```

### From Source

```bash
git clone https://github.com/mazzma12/test-alpaca.git
cd test-alpaca
uv sync --dev
uv run test_alpaca "Hello World!"
```

## Quick Start

```bash
# Basic usage
test_alpaca "Hello World!"

# Happy alpaca with color
test_alpaca --alpaca happy --color green "I'm happy!"

# Special CrowdSec message
test_alpaca --safer-together

# From file
test_alpaca --file message.txt

# From pipe
echo "Hello from pipe" | test_alpaca
```

## Usage

```bash
test_alpaca [OPTIONS] [MESSAGE]

Options:
  -a, --alpaca [default|happy|thinking]  Choose alpaca type
  -c, --color [red|green|blue|yellow|magenta|cyan|white]  Text color
  -w, --width INTEGER                    Maximum width of the speech bubble
  --safer-together                       Display the special "Safer, Together!" message
  -f, --file PATH                        Read message from file
  --version                              Show version and exit
  --help                                 Show this message and exit
```

## Examples

### Basic Examples

```bash
# Default alpaca
test_alpaca "Hello World!"

# Happy alpaca with green text
test_alpaca --alpaca happy --color green "Great job!"

# Thinking alpaca with custom width
test_alpaca --alpaca thinking --width 30 "Let me think about this..."
```

### Integration Examples

**Git hook (.git/hooks/post-commit):**
```bash
#!/bin/bash
test_alpaca --color cyan "Commit successful! 🎉"
```

**Build script:**
```bash
if npm test; then
    test_alpaca --alpaca happy --color green "All tests passed!"
else
    test_alpaca --color red "Tests failed!"
fi
```

**Daily motivation (.bashrc):**
```bash
test_alpaca --alpaca happy "Have a great day!"
```

## Development

### Prerequisites

- Python 3.11+
- [UV](https://github.com/astral-sh/uv) (recommended) or pip

### Setup

```bash
git clone https://github.com/mazzma12/test-alpaca.git
cd test-alpaca
uv sync --dev
```

### VS Code Development

This project includes a VS Code task for development setup. To run it:

1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Type "Tasks: Run Task"
3. Select "test-alpaca Development Setup"

This will automatically:
- Install dependencies with `uv sync --dev`
- Format code with `uv run ruff format .`
- Run linting with `uv run ruff check .`
- Execute tests with `uv run pytest -v`
- Build the package with `uv build`
- Test the CLI with `uv run test_alpaca --safer-together`

### Manual Commands

```bash
# Install dependencies
uv sync --dev

# Run tests
uv run pytest

# Linting and formatting
uv run ruff check .
uv run ruff format .

# Type checking
uv run pyright

# Build package
uv build

# Run locally
uv run test_alpaca "Test message"
```

### Docker Development

```bash
# Build development image
docker build -t test-alpaca:dev .

# Run with volume mount for development
docker run --rm -v $(pwd):/app test-alpaca:dev "Development test"

# Build production image
docker build -f Dockerfile.production -t test-alpaca:prod .
```

### Documentation

```bash
# Install docs dependencies
uv sync --group docs

# Serve documentation locally
uv run mkdocs serve

# Build documentation
uv run mkdocs build
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the classic `cowsay` utility
- ASCII art created with love for the alpaca community
- Built with modern Python tooling (uv, ruff, pytest, mkdocs)

## Links
- [Documentation](https://mazzma12.github.io/test-alpaca)
- [PyPI Package](https://pypi.org/project/test-alpaca/)
- [Source Code](https://github.com/mazzma12/test-alpaca)
- [Issue Tracker](https://github.com/mazzma12/test-alpaca/issues)
