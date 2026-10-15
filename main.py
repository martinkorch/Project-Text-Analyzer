# Import knihovny
import string

# Texty k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.''',
]

# Přihlášení uživatele + výběr textu
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "anna": "pass13",
}

username = input("Username: ")
password = input("Password: ")

if username in registered_users and registered_users[username] == password:
    print("----------------------------------------")
    print(f"Welcome to the app, {username}.")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("----------------------------------------")

    try:
        choice = int(input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))

    except ValueError:
        print("Invalid input. Terminating the program.")
        exit()

    if choice < 1 or choice > len(TEXTS):
        print("Invalid number, terminating the program.")
        exit()

    selected_text = TEXTS[choice - 1]

else:
    print("Unregistered user, terminating the program.")
    exit()

# Rozdělení textu podle mezer
words = selected_text.split()

# Očištění textu od čárek a teček
clean_words = []

for word in words:
    clean_word = word.strip(string.punctuation)
    clean_words.append(clean_word)

# Celkový počet slov
word_count = len(clean_words)
print("----------------------------------------")
print(f"There are {word_count} words in the selected text.")

# Počet slov začínajících velkých písmenem
titlecase_words = sum(word.istitle() for word in clean_words)

if titlecase_words == 1:
    print(f"There is {titlecase_words} titlecase word.")
else:
    print(f"There are {titlecase_words} titlecase words.")

# Počet slov psaných velkými písmeny
uppercase_words = sum(word.isupper() for word in clean_words)

if uppercase_words == 1:
    print(f"There is {uppercase_words} uppercase word.")
else:
    print(f"There are {uppercase_words} uppercase words.")

# Počet slov psaných malými písmemy
lowercase_words = sum(word.islower() for word in clean_words)

if lowercase_words == 1:
    print(f"There is {lowercase_words} lowercase word.")
else:
    print(f"There are {lowercase_words} lowercase words.")

# Počet + součet všech čísel
numbers = 0
numbers_sum = 0

for word in clean_words:
    if word.isdigit():
        numbers += 1
        numbers_sum += int(word)

if numbers == 1:
    print(f"There is {numbers} numeric string.")
else:
    print(f"There are {numbers} numeric strings.")

print(f"The sum of all the numbers {numbers_sum}.")
print("----------------------------------------")

# Četnost různých délek slov
word_lengths = {}

for word in clean_words:
    length = len(word)

    if length not in word_lengths:
        word_lengths[length] = 1
    else:
        word_lengths[length] += 1

# Graf
print("LEN | OCCURRENCES          | NR.")
print("----------------------------------------")

for length in sorted(word_lengths):
    print(f"{length:3} | {'*' * word_lengths[length]:20} | {word_lengths[length]}")

print("----------------------------------------")
