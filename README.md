# Ticket Analyzer

A simple Python project that analyzes support tickets using rule-based text analysis and Pydantic validation.

## Features

- Detects urgent tickets.
- Classifies tickets as bugs, questions, or features.
- Removes English and Arabic punctuation when cleaning words.
- Summarizes ticket priorities.
- Builds a readable report.
- Validates ticket data using Pydantic.
- Creates ticket objects from JSON strings.
- Rejects invalid ticket data with validation errors.

## Requirements

- Python 3.14 or a compatible version.
- Dependencies listed in `requirements.txt`.

## Installation

Activate the virtual environment, then install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

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

- `src/models.py`: Pydantic ticket and user models, plus enums.
- `src/analyzer.py`: Ticket analysis, classification, validation, and reporting.
- `src/cli.py`: Command-line interface.
- `tests/`: Automated tests.
- `requirements.txt`: Project dependencies.
