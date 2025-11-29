import httpx
import re
from fastapi import HTTPException

class GithubService:
    def __init__(self):
        """Initialize the GithubService."""
        pass

    async def get_pr_diff(self, github_url: str) -> str:
        # Extract owner, repo, and pull number from URL
        pattern = r"github\.com/([^/]+)/([^/]+)/pull/(\d+)"
        match = re.search(pattern, github_url)
        
        if not match:
            raise HTTPException(status_code=400, detail="Invalid GitHub Pull Request URL")
            
        owner, repo, pull_number = match.groups()
        
        api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"
        headers = {
            "Accept": "application/vnd.github.v3.diff",
            "User-Agent": "Smart-Code-Reviewer"
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(api_url, headers=headers, follow_redirects=True)
                response.raise_for_status()
                print(response.text)
                return response.text
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    raise HTTPException(status_code=404, detail="Pull Request not found or repository is private")
                raise HTTPException(status_code=e.response.status_code, detail=f"GitHub API error: {e.response.text}")
            except httpx.RequestError as e:
                raise HTTPException(status_code=500, detail=f"Failed to connect to GitHub: {str(e)}")

    async def close(self):
        """Close any open resources."""
        pass

