from src.file_reader import read_text_file
from src.ai_analyzer import analyze_text


def test_main_workflow_with_sample_file():
    file_content = read_text_file("data/sample.txt")
    result = analyze_text(file_content)

    assert "AI File Analysis Result" in result
    assert "Summary:" in result
    assert "Basic Statistics:" in result
    assert "Conclusion:" in result