

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word:\n").upper()

output_list = [phonetic_dictionary[letter] for letter in word]
print(output_list)
