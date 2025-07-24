user_input_text = list(input("Enter text : "))
user_input_letter = input("Enter letter : ")

letter_frequency = 0

for letter in user_input_text:
    if user_input_letter == letter:
        letter_frequency +=1

print(letter_frequency)