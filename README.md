# Smart Code Reviewer

A simple, smart, automated code review tool powered by OpenAI's GPT-4o-mini. This application helps developers improve their code quality by providing AI-driven feedback on code changes and GitHub Pull Requests.

## Features

- **Manual Code Review**: Compare old and new code snippets to get detailed feedback.
- **GitHub Integration**: Directly analyze GitHub Pull Requests by providing the PR URL.
- **Structured Feedback**: Returns structured code review outputs using LangChain's structured output capabilities.
- **Web Interface**: Includes a simple, user-friendly HTML interface for interacting with the reviewer.
- **API-First**: Exposes REST endpoints for easy integration into other workflows.

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **AI/LLM**: [LangChain](https://langchain.com/) + OpenAI GPT-4o-mini
- **HTTP Client**: [httpx](https://www.python-httpx.org/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)

## Prerequisites

- Python 3.11 or higher
- OpenAI API Key

## Installation

1. **Clone the repository**

   ```bash
   git clone git@github.com:BadrTarek/smart_code_reviewer.git
   cd smart_code_reviewer
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # On Linux/Mac:
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**

   Create a `.env` file in the root directory and add your OpenAI API Key:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Running the Application

Start the server directly using Python:

```bash
python src/app.py
```

The application will start at `http://0.0.0.0:8000`.

### Using the Web Interface

Open your browser and navigate to:
`http://localhost:8000`

You can use the UI to:
- Paste old and new code versions for review.
- Enter a GitHub Pull Request URL to review the entire PR diff.

### API Endpoints

#### 1. Review Code Snippets

**Endpoint**: `POST /api/review`

**Request Body**:
```json
{
  "old_code": "def add(a, b): return a + b",
  "new_code": "def add(a: int, b: int) -> int: return a + b"
}
```

#### 2. Review GitHub Pull Request

**Endpoint**: `POST /api/review/github`

**Request Body**:
```json
{
  "github_url": "https://github.com/owner/repo/pull/123"
}
```

## Project Structure

```
smart_code_reviewer/
├── src/
│   ├── app.py                 # Main FastAPI application entry point
│   ├── services/              # Business logic services
│   │   ├── smart_code_reviewer_service.py # LLM integration
│   │   └── github_service.py              # GitHub API interactions
│   ├── models/                # Pydantic data models
│   ├── prompts/               # LLM system prompts
│   └── static/                # HTML frontend files
├── requirements.txt           # Project dependencies
└── .env                       # Environment variables (not committed)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT](LICENSE)

