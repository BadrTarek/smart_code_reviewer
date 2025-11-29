from pydantic import BaseModel

class GithubPRRequest(BaseModel):
    github_url: str

