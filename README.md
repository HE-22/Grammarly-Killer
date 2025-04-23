# AI Spell Check Tool

This project provides an advanced spell check and grammar correction tool powered by OpenAI's GPT models. It can handle heavily misspelled text, text without spaces, abbreviations, and even format code snippets.

## Features

*   Corrects spelling and grammar.
*   Handles input text with missing spaces between words.
*   Understands and corrects abbreviations.
*   Cleans up formatting for code snippets without changing logic.
*   Preserves original meaning and formatting (like newlines) where possible.
*   Includes a speed test script to measure processing time for various inputs.
*   Uses OpenAI's `gpt-4.1-nano` model by default (configurable).

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HE-22/Grammarly-Killer 
    cd Grammarly-Killer
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    # On Windows use: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    *   Create a file named `.env` in the project root directory.
    *   Add your OpenAI API key to the `.env` file:
        ```
        OPENAI_API_KEY='your_openai_api_key_here'
        ```

## Usage

### Spell Checking a String

Run the main script from the root directory, passing the input string as a command-line argument:

```bash
python src/main.py "yourtexthere tobecorrected"
```

Example:

```bash
python src/main.py "hellowrldthisisatest"
```

Output:

```
hello world this is a test
```

Optionally add to Alfred workflow (https://www.alfredapp.com/)