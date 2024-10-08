 Quesuion number 1
# CSV Text Extractor

This project is a Python script designed to extract text from a specific column in CSV files contained within a ZIP archive. The extracted text is then saved into a single output text file.

## Features

- Extracts CSV files from a ZIP archive.
- Reads a user-specified column from each CSV file.
- Collects all text data from that column.
- Saves the collected text to a single output text file.

## Requirements

- Python 3.x
- `pandas` library
- `zipfile` library (part of Python standard library)
- `os` library (part of Python standard library)


Question_1_task_3.1

# Top 30 Common Words Extractor

This Python script reads a text file, counts the frequency of words, identifies the top 30 most common words, and saves the results to a CSV file.

## Features

- Reads text from a specified file.
- Counts the frequency of each word in the text.
- Identifies the top 30 most common words.
- Saves the results to a CSV file with word counts.

## Requirements

- Python 3.x
- `collections` (part of Python standard library)
- `csv` (part of Python standard library)
- `re` (part of Python standard library)


question_1_task_3.2.py
   
# Token Frequency Analyzer

This repository contains a Python script for analyzing token frequencies in a text file using a pre-trained BERT tokenizer. The script reads a text file, tokenizes the content, counts the occurrences of each token, and retrieves the top 30 most common tokens.

## Features

- Read text from a specified file.
- Tokenize text using a pre-trained BERT model.
- Count the frequency of each token.
- Retrieve and display the top 30 most frequent tokens.
- token


question 2 chapter 1 and 1.1

Overview

This Python script processes a given string by separating digits and letters, converting specific characters to their ASCII codes, and then displaying the results. The script provides:

    Conversion of even digits to their ASCII codes.
    Conversion of uppercase letters to their ASCII codes.
    Output of the processed results along with predefined ASCII codes for even numbers and uppercase letters.

Functions
process_string(s)

Processes the input string s and returns two processed strings:

    Digits: Even digits are converted to their ASCII codes, while odd digits remain unchanged.
    Letters: Uppercase letters are converted to their ASCII codes, while lowercase letters remain unchanged.

Parameters:

    s (str): The input string to be processed.

Returns:

    processed_number (str): A string with even digits converted to ASCII codes and odd digits unchanged.
    processed_letters (str): A string with uppercase letters converted to ASCII codes and lowercase letters unchanged.

get_ascii_codes()

Generates and returns two dictionaries:

    ASCII codes for even digits: Mapping of even digits ('0', '2', '4', '6', '8') to their ASCII codes.
    ASCII codes for uppercase letters: Mapping of uppercase letters ('A' to 'Z') to their ASCII codes.

Returns:

    ascii_even_numbers (dict): A dictionary where keys are even digits and values are their ASCII codes.
    ascii_uppercase_letters (dict): A dictionary where keys are uppercase letters and values are their ASCII codes

Question 3

Encryption and Decryption in Python

This project contains Python functions for encrypting and decrypting text using a simple Caesar cipher. The key for encryption and decryption must be an integer.

## Getting Started

- **Getting Started**: Instructions on prerequisites and installation.
- **Usage**: How to use the `encrypt` and `decrypt` functions with an example.
- **Errors and Exceptions**: Information about error handling.
- **License**: Placeholder for the license information.

Question question_1_task_4.py


Disease and Drug Extraction and Comparison
Overview

This Python script extracts and compares diseases and drugs from a given text using two different Natural Language Processing (NLP) models:

    SpaCy: A popular NLP library.
    BioBERT: A pre-trained model specialized in biomedical text.

The script compares the results from these models to find common and unique entities and counts the most common entities identified by each model.
Features

    Extracts diseases and drugs from text using SpaCy and BioBERT models.
    Compares entities detected by both models.
    Provides counts of the most common entities identified.

Requirements

    Python 3.x
    spacy
    transformers
    torch
    collections

You can install the required Python packages using pip. Ensure you have the necessary models downloaded.
Installation

    Clone the repository (if applicable) or download the script.

    Install the required packages:

    bash

pip install spacy transformers torch

Download the SpaCy model:

    For SpaCy model 'en_ner_bc5cdr_md':

    bash

        python -m spacy download en_ner_bc5cdr_md

    Download the BioBERT model: The script will automatically download the BioBERT model when running if it's not already cached.

Usage

    Prepare your text file:
        Ensure you have a text file (e.g., outputtxt.txt) that contains the text from which you want to extract diseases and drugs.

    Update the file path:
        In the script, update the filePath variable to point to your text file location:

        python

    filePath = r'path\to\your\outputtxt.txt'

Run the script:

bash

python your_script_name.py

Replace your_script_name.py with the name of your Python script file.


## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git
