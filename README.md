# Four-Letter-English-Word-Generator

## Overview
The Four-Letter English Word Generator is a Python program that generates all possible combinations of four-letter sequences using the English alphabet and identifies those that are valid English words. The program reads from a file containing English words and then uses nested loops to create four-letter combinations, subsequently checking each combination against the word list.

## Prerequisites
- Python 3.x

## How to Run
1. Clone this repository.
2. Make sure that the text file "wordlist.txt" containing English words is in the project directory.
3. Run the `main.py` script, and when prompted, enter the name of the text file.

## Features
- Generates all possible four-letter combinations from the English alphabet.
- Identifies and outputs the valid English words from the generated sequences.
- Displays the total number of four-letter combinations and the number of valid English words identified.
- Outputs the first 10 and last 10 valid English words from the list of identified words.

## Functions
- `getWords(filename)`: Reads words from a file and returns them as a list.
- `fourLetterSequences(words)`: Generates four-letter sequences and identifies the valid English words.
- `displayfourLetterWords(words, sequences)`: Displays the number of valid words identified and shows the first 10 and last 10 of them.
- `main()`: The main function that ties all other functions together.

## Author
Farjad Tariq

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


