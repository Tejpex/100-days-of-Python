
with open("./Input/Names/invited_names.txt") as name_file:
    names_in_file = name_file.readlines()
    names = [name.strip('\n') for name in names_in_file]

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for name in names:
    with open(f"./Output/ReadyToSend/letter_to_{name}", mode="w") as new_letter:
        new_text = letter.replace("[name]", name)
        new_letter.write(new_text)
