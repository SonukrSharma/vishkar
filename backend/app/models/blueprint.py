from pydantic import BaseModel
from typing import Optional


class ProjectAnswers(BaseModel):
    app_name: str
    app_description: str
    target_users: str
    core_features: str
    tech_stack_backend: str
    tech_stack_frontend: str
    tech_stack_database: str
    user_roles: str
    expected_scale: str
    deployment_target: str


class BlueprintRequest(BaseModel):
    answers: ProjectAnswers


class ChapterResult(BaseModel):
    chapter_number: int
    title: str
    content: str


class BlueprintResult(BaseModel):
    app_name: str
    chapters: list[ChapterResult]
    doc_path: Optional[str] = None
