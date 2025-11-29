

from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class _Issue(BaseModel):
    category: Literal["critical", "warning", "info"] = Field(description="Category of the issue")
    title: str = Field(description="Short summary of the issue")
    lineNumber: Optional[int] = Field(None, description="Line number in the new code where the issue is located")
    snippet: Optional[str] = Field(None, description="The problematic code line(s)")
    description: str = Field(description="Detailed explanation of the issue")
    remediation: str = Field(description="Actionable advice on how to fix the issue")

class CodeReviewerOutputSchema(BaseModel):
    score: int = Field(description="Quality score from 0 to 100")
    totalIssues: int = Field(description="Total number of issues found")
    criticalCount: int = Field(description="Count of critical issues")
    warningCount: int = Field(description="Count of warning issues")
    suggestionCount: int = Field(description="Count of suggestion/info issues")
    issues: List[_Issue] = Field(description="List of identified issues")
    positiveFindings: List[str] = Field(description="List of positive findings")
