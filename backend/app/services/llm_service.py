import anthropic
from app.config import settings
from app.models.blueprint import ProjectAnswers, ChapterResult
from app.prompts.chapters import CHAPTER_PROMPTS, CHAPTER_TITLES


client = anthropic.Anthropic(api_key=settings.anthropic_api_key)


def generate_chapter(chapter_index: int, answers: ProjectAnswers) -> ChapterResult:
    prompt_fn = CHAPTER_PROMPTS[chapter_index]
    prompt = prompt_fn(answers)

    message = client.messages.create(
        model=settings.model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    content = message.content[0].text

    return ChapterResult(
        chapter_number=chapter_index + 1,
        title=CHAPTER_TITLES[chapter_index],
        content=content,
    )


def generate_all_chapters(answers: ProjectAnswers) -> list[ChapterResult]:
    chapters = []
    for i in range(len(CHAPTER_PROMPTS)):
        print(f"Generating Chapter {i + 1}: {CHAPTER_TITLES[i]}...")
        chapter = generate_chapter(i, answers)
        chapters.append(chapter)
    return chapters
