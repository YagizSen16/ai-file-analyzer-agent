from file_reader import read_text_file
from ai_analyzer import analyze_text


def main():
    """
    Main program workflow for the AI File Analyzer Agent.
    """

    print("AI File Analyzer Agent")
    print("----------------------")

    file_path = input("Enter the path of the .txt file to analyze: ")

    try:
        file_content = read_text_file(file_path)
        analysis_result = analyze_text(file_content)

        print("\nAnalysis completed successfully.")
        print("-------------------------------")
        print(analysis_result)

    except FileNotFoundError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()