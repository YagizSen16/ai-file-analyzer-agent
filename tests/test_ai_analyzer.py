from src.ai_analyzer import analyze_text


def test_analyze_text_returns_summary():
    text = "Artificial intelligence helps users analyze files. It can summarize long documents."

    result = analyze_text(text)

    assert "Summary:" in result
    assert "Artificial intelligence helps users analyze files." in result


def test_analyze_text_returns_word_count():
    text = "AI helps file analysis."

    result = analyze_text(text)

    assert "Word count: 4" in result


def test_analyze_text_returns_character_count():
    text = "AI test."

    result = analyze_text(text)

    assert "Character count:" in result


def test_analyze_text_returns_sentence_count():
    text = "First sentence. Second sentence."

    result = analyze_text(text)

    assert "Sentence count: 2" in result