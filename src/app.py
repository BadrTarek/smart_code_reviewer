from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path


def get_html_content() -> str:
    """Read and return the HTML content from the static file."""
    html_path = Path(__file__).parent / "static" / "smart_code_reviewed_home.html"
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()


def execute() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI()

    @app.get("/", response_class=HTMLResponse)
    async def root():
        """Return the HTML page."""
        html_content = get_html_content()
        return html_content

    return app


app = execute()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

