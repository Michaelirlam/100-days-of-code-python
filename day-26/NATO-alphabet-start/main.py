import pandas

#TODO 1. Create a dictionary in this format:
nato = pandas.read_csv("./NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_data = pandas.DataFrame(nato)
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def nato_input():
    user_input = input("Type you word or sentence: ").upper()

    try:
        phonetics = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Invalid input, please use characters in the alphabet")
        nato_input()
    else:
        print(phonetics)
    
nato_input()