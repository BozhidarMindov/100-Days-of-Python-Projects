
with open("./Input/Letters/starting_letter.txt") as letter_text:
    letter = letter_text.read()

with open("./Input/Names/invited_names.txt") as names_text:
    names_list = names_text.readlines()
    for name in names_list:
        stripped_name = name.strip()
        complete_letter = letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as new_letter:
            new_letter.write(complete_letter)

