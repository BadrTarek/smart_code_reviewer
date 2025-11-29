from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from pathlib import Path

from models.code_reviewer_output_schema import CodeReviewerOutputSchema


class SmartCodeReviewerService:
    
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.prompt_path = Path(__file__).parent.parent / "prompts" / "code_review_prompt.md"
        with open(self.prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
        self.structured_llm = self.llm.with_structured_output(CodeReviewerOutputSchema)

    def review_code(self, old_code: str, new_code: str) -> CodeReviewerOutputSchema:
        formatted_content = f"Old Code:\n{old_code}\n\nNew Code:\n{new_code}"
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=formatted_content)
        ]
        response = self.structured_llm.invoke(messages)
        return response

    def review_pr_diff(self, diff: str) -> CodeReviewerOutputSchema:
        formatted_content = f"Git Diff:\n{diff}"
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=formatted_content)
        ]
        response = self.structured_llm.invoke(messages)
        return response
