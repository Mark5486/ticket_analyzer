
# Ticket Analyzer

A simple Python project that analyzes support tickets.

## Features

- Detects urgent tickets.
- Classifies tickets as bugs, questions, or features.
- Removes English and Arabic punctuation when cleaning words.
- Summarizes ticket priorities.
- Builds a readable report.

## Requirements

- Python 3.14 or compatible version.
- No external packages are required for the application itself.

## Run the project

Activate the virtual environment if needed, then run:

```powershell
python -m src.cli "Server is down!!" "How do I login?" "Please add dark mode"
```

## Example output

```text
1. Server is down!! - urgent - bug
2. How do I login? - normal - question
3. Please add dark mode - normal - feature
Summary:
urgent: 1
normal: 2
```

## Run tests

```powershell
python -m pytest
```

## Project structure

- `src/models.py`: Ticket models and enums.
- `src/analyzer.py`: Ticket analysis and reporting.
- `src/cli.py`: Command-line interface.
- `tests/`: Automated tests.
