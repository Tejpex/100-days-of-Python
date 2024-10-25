import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Looping through dictionaries:
# for (key, value) in student_dict.items():
# Access row.student or row.score

# Keyword Method with pandas
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

processing = True
while processing:
    word_to_spell = input("What word do you want to spell out? ").upper()
    try:
        spelled_word = [nato_dict[letter] for letter in word_to_spell]
    except KeyError:
        print("Only letters in the English alphabet, please.")
    else:
        print(spelled_word)
        processing = False
