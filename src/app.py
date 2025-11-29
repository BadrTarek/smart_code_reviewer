from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pathlib import Path
from dotenv import load_dotenv
from models.review_code_request import ReviewCodeRequest
from models.github_pr_request import GithubPRRequest
from services.smart_code_reviewer_service import SmartCodeReviewerService
from services.github_service import GithubService

DOTENV_PATH = Path(__file__).parent.parent / ".env"
load_dotenv(DOTENV_PATH)


def get_html_content() -> str:
    """Read and return the HTML content from the static file."""
    html_path = Path(__file__).parent / "static" / "smart_code_reviewed_home.html"
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()


def execute() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI()
    reviewer_service = SmartCodeReviewerService()
    github_service = GithubService()

    @app.get("/", response_class=HTMLResponse)
    async def root():
        """Return the HTML page."""
        html_content = get_html_content()
        return html_content

    @app.post("/api/review")
    async def review_code(request: ReviewCodeRequest):
        try:
            result = reviewer_service.review_code(request.old_code, request.new_code)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.post("/api/review/github")
    async def review_github_pr(request: GithubPRRequest):
        try:
            diff = await github_service.get_pr_diff(request.github_url)
            result = reviewer_service.review_pr_diff(diff)
            return result
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return app


app = execute()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
