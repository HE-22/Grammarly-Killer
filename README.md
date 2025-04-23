# AI Spell Check Tool

![auto-correct-ai](https://github.com/user-attachments/assets/6282a823-bd6e-4e11-b73f-6d594d5983c7)


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
    *   To change from template to real, copy the template file:
        ```bash
        cp .env.template .env
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

## Optional 
* Add to Alfred workflow (https://www.alfredapp.com/)
* This way, you can trigger it to run on your highlighted text and auto-paste over the old writing.

<img width="583" alt="image" src="https://github.com/user-attachments/assets/77ad5394-75f6-4037-9d7e-ca2285710ff8" />

