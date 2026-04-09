from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.models.blueprint import BlueprintRequest, BlueprintResult
from app.services.llm_service import generate_all_chapters
from app.services.doc_service import build_document

router = APIRouter(prefix="/blueprint", tags=["blueprint"])


@router.get("/questions")
def get_questions():
    """Returns the list of questions to ask the user before generating a blueprint."""
    return {
        "questions": [
            {"id": "app_name", "label": "What is the name of your application?"},
            {"id": "app_description", "label": "Describe your application in 2-3 sentences. What does it do?"},
            {"id": "target_users", "label": "Who are the target users of this application?"},
            {"id": "core_features", "label": "List the core features (MVP) you want to build. Separate with commas."},
            {"id": "tech_stack_backend", "label": "What backend technology will you use? (e.g. FastAPI, Spring Boot, Django, Node.js)"},
            {"id": "tech_stack_frontend", "label": "What frontend technology will you use? (e.g. Angular, React, Vue, Next.js)"},
            {"id": "tech_stack_database", "label": "What database will you use? (e.g. MongoDB, PostgreSQL, MySQL)"},
            {"id": "user_roles", "label": "What user roles will your application have? (e.g. Admin, User, Guest)"},
            {"id": "expected_scale", "label": "What is the expected scale? (e.g. 100 users, 10,000 users, enterprise)"},
            {"id": "deployment_target", "label": "Where do you plan to deploy? (e.g. Azure, AWS, Vercel, Railway)"},
        ]
    }


@router.post("/generate")
def generate_blueprint(request: BlueprintRequest):
    """Generates a full 10-chapter blueprint document from the provided answers."""
    try:
        chapters = generate_all_chapters(request.answers)

        result = BlueprintResult(
            app_name=request.answers.app_name,
            chapters=chapters,
        )

        answers_dict = request.answers.model_dump()
        doc_path = build_document(result, answers_dict)
        result.doc_path = doc_path

        return {
            "success": True,
            "message": "Blueprint generated successfully",
            "app_name": result.app_name,
            "chapters_generated": len(result.chapters),
            "doc_path": doc_path,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/download/{filename}")
def download_blueprint(filename: str):
    """Downloads a generated blueprint document."""
    filepath = f"generated_blueprints/{filename}"
    return FileResponse(
        path=filepath,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
