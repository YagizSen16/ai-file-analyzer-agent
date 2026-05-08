from pathlib import Path


def read_text_file(file_path: str) -> str:
    """
    Reads a text file and returns its content.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: Content of the text file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or not a .txt file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("Only .txt files are supported.")

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError("The file is empty.")

    return content