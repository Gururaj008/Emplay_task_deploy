Emplay Assignment for Internship opportunity
Demo Script Localization
By - Gururaj H C

ABOUT THE PROJECT
This project aims to demonstrate the process of localizing a demo script by translating its content to a user-specified language and replacing names with those from a selected country and is based on a real-world scenario where sales representatives need to adapt their pitch scripts for different regions or locales. 
STEPS INVOLVED
•	Chose to go with LLM( ChatGPT3.5 Turbo 16K ) to carry out the given task
•	Registered with OPENAI and got myself an API key
•	Created a virtual environment in VSCode
•	Imported the necessary libraries
•	Using docx2python module from docx2python library to extract text from Word document
•	Divided the entire text into 5 slices for optimum results
•	Written prompt for ChatGPT and asked the model to identify the names in the given slice and replace it with native names from the chosen country
•	Written prompt for ChatGPT and asked the model to translate the language in the text to the one chosen by the user
•	Repeated the above steps for all the 5 slices
•	Stored the result in a single variable
•	Wrote the results into a docx file
•	Provided user with an option to download the ‘localized demo script.docx’ file
