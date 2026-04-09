import time
import anthropic
from app.config import settings
from app.models.blueprint import ProjectAnswers, ChapterResult
from app.prompts.chapters import CHAPTER_PROMPTS, CHAPTER_TITLES


client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds


def generate_chapter(chapter_index: int, answers: ProjectAnswers) -> ChapterResult:
    prompt_fn = CHAPTER_PROMPTS[chapter_index]
    prompt = prompt_fn(answers)

    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            message = client.messages.create(
                model=settings.model,
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}],
            )
            return ChapterResult(
                chapter_number=chapter_index + 1,
                title=CHAPTER_TITLES[chapter_index],
                content=message.content[0].text,
            )
        except anthropic.RateLimitError as e:
            last_error = e
            wait = RETRY_DELAY * attempt
            print(f"  Rate limited — retrying in {wait}s (attempt {attempt}/{MAX_RETRIES})")
            time.sleep(wait)
        except anthropic.APIError as e:
            last_error = e
            print(f"  API error on attempt {attempt}/{MAX_RETRIES}: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

    raise RuntimeError(
        f"Failed to generate Chapter {chapter_index + 1} after {MAX_RETRIES} attempts: {last_error}"
    )


def generate_all_chapters(
    answers: ProjectAnswers,
    progress_callback=None,
) -> list[ChapterResult]:
    chapters = []
    total = len(CHAPTER_PROMPTS)

    for i in range(total):
        print(f"[{i + 1}/{total}] Generating: {CHAPTER_TITLES[i]}...")
        chapter = generate_chapter(i, answers)
        chapters.append(chapter)

        if progress_callback:
            progress_callback(
                chapter_number=i + 1,
                title=CHAPTER_TITLES[i],
                total=total,
            )

    return chapters
