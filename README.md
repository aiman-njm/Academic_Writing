# Academic Writing Analyzer API

This project provides a simple Flask backend that interacts with OpenAI's GPT-4o
model to analyze student writing.

## Setup

1. Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and add your OpenAI API key:

```bash
cp .env.example .env
# Edit .env and set OPENAI_API_KEY
```

3. Run the application:

```bash
python app.py
```

The server will start on `http://localhost:5000`.

## Usage

Send a POST request to `/analyze` with JSON containing a `text` field. The
response will include grammar issues, structure issues, an overall comment, and
up to three recommended study modules.
