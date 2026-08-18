# WAVE – NeuroSymbolic Requirement Converter

WAVE is a prototype implementation of a hybrid neurosymbolic pipeline for converting natural language requirements into Controlled Natural Language (CNL) and Temporal Logic specifications.

The project combines Large Language Model (LLM)-based semantic analysis with deterministic symbolic processing to produce structured and formal representations.

## Project Overview

Natural language requirements can be ambiguous and difficult to use directly for formal verification. WAVE addresses this by introducing an intermediate semantic representation and a Controlled Natural Language stage.

The forward conversion pipeline is:

Natural Language → Semantic Analysis → AST → Semantic Verification → CNL → Temporal Logic

The prototype also supports reverse conversion:

Temporal Logic → CNL → English

## Main Features

- Natural Language requirement validation
- LLM-based semantic analysis
- Abstract Syntax Tree (AST) representation
- Deterministic semantic verification
- Controlled Natural Language generation
- Temporal Logic generation
- Reverse conversion from Temporal Logic to CNL and English
- Interactive Flask-based web interface
- Handling of invalid or unsupported requirements

## System Architecture

WAVE follows a hybrid neurosymbolic architecture.

### Neural Component

An LLM is used for semantic analysis of natural language requirements, identifying relevant entities, actions, temporal relationships, and logical structure.

### Symbolic Component

Deterministic symbolic processing verifies the extracted semantic representation and generates the corresponding Controlled Natural Language and Temporal Logic representations.

## Conversion Pipeline

### Forward Conversion

```text
Natural Language
       ↓
Requirement Validation
       ↓
LLM Semantic Analysis
       ↓
Abstract Syntax Tree (AST)
       ↓
Semantic Verification
       ↓
Controlled Natural Language
       ↓
Temporal Logic
```

### Reverse Conversion

```text
Temporal Logic
       ↓
Controlled Natural Language
       ↓
Readable English
```

## Technologies

- Python
- OpenAI Python SDK
- GPT-4o-mini
- Flask
- HTML
- CSS
- JavaScript

## Project Structure

```text
WAVE/
│
├── app.py
├── converter.py
├── untitled25.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    ├── script.js
    └── images/
        └── wave_logo.png
```

### Main Files

**`app.py`**  
Provides the Flask application and handles requests from the web interface.

**`converter.py`**  
Contains the conversion functionality used by the Flask application, including the forward and reverse conversion processes.

**`untitled25.py`**  
Contains the final research/prototype implementation developed during the project, including semantic analysis, AST processing, deterministic generation, and reverse conversion.

**`templates/index.html`**  
Provides the main web interface.

**`static/style.css`**  
Contains the styling for the web interface.

**`static/script.js`**  
Contains client-side interface functionality.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/NeuroSymbolic-Requirement-Converter.git
cd NeuroSymbolic-Requirement-Converter

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## OpenAI API Configuration

The application requires an OpenAI API key for the LLM-based semantic analysis.

The API key should not be stored directly in the source code.

Set the `OPENAI_API_KEY` environment variable before running the application.

### Windows PowerShell

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

### Windows Command Prompt

```cmd
set OPENAI_API_KEY=your_api_key_here
```

## Running the Application

After installing the dependencies and configuring the OpenAI API key, run:

bash
```
python app.py
```

## Example

### Forward Conversion

Example input:

```text
The backup generator activates whenever the primary power supply fails.
```

The system processes the requirement and produces:

- Controlled Natural Language
- Temporal Logic
- Confidence information

### Reverse Conversion

A Temporal Logic specification can also be provided to generate:

- Controlled Natural Language
- Readable English

## Supported Temporal Logic

The prototype supports a selected set of temporal and logical operators, including:

- Always
- Eventually
- Next
- Until
- Release
- Weak Until
- Not
- And
- Or
- Implies
- Within

The exact supported patterns depend on the deterministic rules implemented in the prototype.

## Limitations

The current prototype has several limitations:

- Semantic analysis depends on the underlying LLM.
- Only a selected set of temporal and logical operators is supported.
- Numerical and quantitative constraints have limited support.
- External model-checking tools are not directly integrated.
- Reverse-generated English may contain grammatically awkward or unnatural sentence structures.
- The prototype is intended as a research demonstration rather than a complete industrial verification solution.

## Future Work

Potential future improvements include:

- Expanding support for temporal and logical operators
- Improving numerical and quantitative constraint handling
- Improving the linguistic quality of reverse conversion
- Integrating external formal verification and model-checking tools
- Evaluating the system with larger and more diverse requirement datasets
- Conducting evaluation with domain experts

## Research Context

This prototype was developed as part of an MSc dissertation in Data Science and Statistical Learning at the University of Limerick.

**Title:**  
*Neurosymbolic Computation for High Assurance Systems*

## Author

**Sangam SharanaBasava Sunkanur**

MSc Data Science and Statistical Learning  
University of Limerick
