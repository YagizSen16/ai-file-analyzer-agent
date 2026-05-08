Step 1: Planned System Description and Initial Design

Yagiz Sen 231ADB283 


1. Short Description of the Planned System and Its Goal

The planned system is an AI-assisted file analysis application developed in Python. The system will allow a user to provide a text file as input, read the content of the file, analyze the information using an AI model, and return a structured result to the user.

The main goal of the system is to help users quickly understand the content of text-based documents without reading the entire file manually. The system will generate a short summary, identify key points, extract important keywords, and provide a simple conclusion about the file content.

This system is useful for students, developers, or general users who need to analyze notes, reports, simple documents, or text files in a faster and more organized way.

2. AI or Agent-Based Approach

The system will use an AI-assisted agent-based approach. The user will provide a file and a request, and the system will process the input step by step. First, the system will read the uploaded text file using a file-reading tool. Then, the extracted text will be sent to an AI model for analysis.

The AI component will be responsible for understanding the text, summarizing the content, identifying key ideas, and generating a clear response. The tool component will be responsible for reading and preparing the file content before it is analyzed by the AI model.

The planned workflow is:

User input → File reading tool → Text extraction → AI analysis → Structured output

This approach is agent-based because the system does not only generate a response directly. It also uses an external tool during execution to complete the task.

3. Tools Used in the System

The following tools are planned to be used in the system:

Tool	Purpose
Python	Main programming language for implementing the system logic
OpenAI API / AI model	To analyze, summarize, and interpret the text content
File handling modules	To read text files provided by the user
dotenv	To store and manage API keys securely through environment variables
Git and GitHub	To manage version control and store the project repository
requirements.txt	To list project dependencies for installation
Command-line interface	To allow the user to run the program and provide input

4. Preliminary Programming Concepts Required

The following programming concepts will be required during the development of the system:
Concept	How It Will Be Used
Variables and data types	To store user input, file content, and AI responses
Functions	To separate the system into reusable parts such as reading files and analyzing text
File handling	To open, read, and process .txt files
Conditional statements	To check whether the file exists, whether input is valid, and whether errors occur
Error handling	To manage problems such as missing files, empty files, or API connection errors
API usage	To send extracted text to the AI model and receive a response
Modular programming	To organize the code into separate files or functions
Environment variables	To keep API keys outside the source code
Git version control	To track project progress through commits
Basic testing	To check whether the main workflow and file-reading functionality work correctly

