# Step 3: Testing, Deployment Preparation, and Data Conversion

**Student:** Yagiz Sen  
**Student ID:** 231ADB283  

## 1. Description of the Testing Process

At this stage of the project, the testing process was expanded to verify the main functionality of the AI File Analyzer Agent. The testing was performed using the `pytest` framework.

The main purpose of the testing process is to check whether the system can correctly read input files, process the extracted text, generate structured analysis results, and handle invalid input cases without crashing.

The testing process includes:

- functional testing of the main workflow,
- tool testing of the file-reading module,
- input validation testing,
- error handling testing,
- analysis output testing.

The file-reading tool was tested with different file conditions, including a valid `.txt` file, a missing file, an empty file, and a file with an unsupported extension. The analysis component was tested to check whether it returns expected output sections such as summary, word count, character count, sentence count, and conclusion.

The full workflow was also tested by reading the sample input file from the `data` folder and passing its content to the analysis module. This confirms that the main system components can work together.

The tests were executed using the following command:

```bash
python -m pytest
```

The test execution was successful, and all 9 tests passed.

## 2. Test Scenarios and Expected Results

| Test Scenario | Purpose | Expected Result | Actual Result |
|---|---|---|---|
| Read valid text file | To check whether the file-reading tool can read a correct `.txt` file | The file content is returned successfully | Passed |
| Missing file input | To check error handling when the file does not exist | `FileNotFoundError` is raised | Passed |
| Empty text file | To check validation of empty files | `ValueError` is raised | Passed |
| Unsupported file extension | To check whether the system rejects non-`.txt` files | `ValueError` is raised | Passed |
| Analysis returns summary | To check whether the analysis output includes a summary section | The output contains `Summary:` and the first sentence of the text | Passed |
| Analysis returns word count | To verify basic text statistics | The output contains the correct word count | Passed |
| Analysis returns character count | To verify that character counting is included | The output contains `Character count:` | Passed |
| Analysis returns sentence count | To verify sentence counting | The output contains the correct sentence count | Passed |
| Main workflow with sample file | To check whether file reading and text analysis work together | The output contains analysis result, summary, statistics, and conclusion | Passed |

## 3. Deployment Preparation

The system is prepared to run as a local command-line Python application. It does not require a web server or external deployment platform at this stage.

To run the system on another computer, the user should follow these steps:

1. Clone or download the GitHub repository.
2. Open the project folder in a terminal.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the main program:

```bash
python src/main.py
```

5. When the program asks for a file path, enter:

```text
data/sample.txt
```

The project includes a `requirements.txt` file, which lists the dependencies needed to run and test the system. The project also includes a `.env.example` file to show how an API key can be configured later if the OpenAI API is connected.

The current system can be deployed as a local command-line tool. This deployment strategy is suitable because the program is simple, file-based, and currently designed for local text analysis.

## 4. Data Conversion and Porting Explanation

The system currently uses local `.txt` files as input data. The user provides the path to a text file, and the file-reading tool reads the file content using UTF-8 encoding.

The data flow is:

```text
User file path → File-reading tool → Extracted text → Text analysis module → Structured terminal output
```

The input format is plain text. The system converts the file content into a Python string. This string is then passed to the analysis module.

Inside the analysis module, the text is processed to calculate:

- word count,
- character count,
- sentence count,
- short summary,
- simple conclusion.

The output is converted into a structured text result and displayed in the terminal. This keeps the data flow simple and consistent. The system preserves correctness by validating the file before processing it. It checks whether the file exists, whether it has the `.txt` extension, and whether it is empty.

At the current stage, no complex data porting is required because the system does not use databases, external file formats, or API response conversion. However, the structure is ready to support future OpenAI API integration, where extracted text could be sent to an AI model and the AI response could be converted into a structured result.

## 5. Current Step 3 Result

At the end of Step 3, the project includes:

- expanded test coverage,
- 9 successful automated tests,
- file-reading tool tests,
- analysis module tests,
- main workflow test,
- deployment preparation instructions,
- data conversion explanation,
- updated journal documentation.

The project is now more testable, more understandable, and closer to controlled deployment.