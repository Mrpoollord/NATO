import pandas

# Read the CSV data
# Make sure you have 'nato_phonetic_alphabet.csv' in the same folder
try:
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
except FileNotFoundError:
    print("Error: 'nato_phonetic_alphabet.csv' was not found.")
    # Create a fallback dictionary for testing purposes if file is missing
    data = pandas.DataFrame([
        {"letter": "A", "code": "Alfa"}, 
        {"letter": "B", "code": "Bravo"},
        {"letter": "C", "code": "Charlie"},
        {"letter": "D", "code": "Delta"},
        {"letter": "E", "code": "Echo"}
    ])

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# We use dictionary comprehension to iterate over the pandas DataFrame
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    
    try:
        # Create a list of the phonetic code words
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic() # Recursion: ask again if they enter a number/symbol
    else:
        print(output_list)

# Run the function
if __name__ == "__main__":
    generate_phonetic()

