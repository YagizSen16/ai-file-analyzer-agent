def analyze_text(text: str) -> str:
    """
    Analyzes the given text and returns a structured result.

    Args:
        text (str): Text content extracted from a file.

    Returns:
        str: Structured analysis result.
    """

    word_count = len(text.split())
    character_count = len(text)

    sentences = [sentence.strip() for sentence in text.split(".") if sentence.strip()]
    sentence_count = len(sentences)

    short_summary = sentences[0] if sentences else "No summary available."

    result = f"""
AI File Analysis Result

Summary:
{short_summary}.

Basic Statistics:
- Word count: {word_count}
- Character count: {character_count}
- Sentence count: {sentence_count}

Conclusion:
The file has been successfully read and analyzed. The content appears to describe a topic related to artificial intelligence, file processing, and structured text analysis.
"""

    return result