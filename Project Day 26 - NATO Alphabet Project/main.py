import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(new_dict)

def generate_output():
    word = input("Enter a word: ").upper()

    try:
        final_list = [new_dict[letter] for letter in word]  

    except KeyError:
        print("Sorry, only letters in the alphabet allowed!")
        generate_output()

    else:
        print(f"Your name using the NATO alphabet:\n{final_list}")

generate_output()
