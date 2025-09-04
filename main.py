"""
main.py: first project for Engeto - Online Python Akademy

author: Artjom Malyšev
email: artommalysev@gmail.com
"""

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
    garpike and stingray are also present.'''
]

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

separator = 45 * "-"


user_name = input("Hello! Enter your username: ")
user_password = input("Now enter your password: ")
print(separator)


# control if entered user name is matching any key in dict
if user_name in registered_users:
    # control if entered user password is matching key value
    if user_password == registered_users[user_name]:                   
        print(f"Welcome to the application, {user_name}.")
        print("We have 3 different texts to be analyzed.")
        print(separator)
    else:
        print("Unregistered user, terminating the program...")
        exit()
else:
    print("Unregistered user, terminating the program...")
    exit()


selected_text = input("Enter a number btw. 1 and 3 to select text: ")
print(separator)


# control if input is only numbers 1-3
if  selected_text.isdigit() and 1 <= int(selected_text) <= 3:
    pass
else:
    print("Enter only numbers btw. 1 and 3! Terminating the program...")
    exit()


# cleaning choosen text from all dots and commas, splitting single words in the list
cleaned_text = TEXTS[int(selected_text) - 1].replace(",", " ").replace(".", " ").split()


# variables for counting words and numbers
words_count = 0
starts_with_upper_case = 0
only_upper_cases = 0
only_lower_cases = 0
number_count = 0                                                                                 
number_sum = 0


# for loop rides cleaned text in the list word by word
for search_text in cleaned_text:
    
    # counting all words
    words_count += 1
    
    # searching words that starts with upper case and counting them
    if search_text[0].isupper() and not search_text.isupper():
            starts_with_upper_case += 1

    # searching words that contains only upper cases and counting them
    if search_text.isupper():
            only_upper_cases += 1

    # searching words that contains only lower cases and counting them
    if search_text.islower():
            only_lower_cases += 1

    # searching all digits in text, counting them and summation
    if search_text.isdigit():
            number_count += 1
            number_sum += int(search_text)


# prints all results
print(f"There are {words_count} words in the selected text.")
print(f"There are {starts_with_upper_case} titlecase words.")
print(f"There are {only_upper_cases} uppercase words.")
print(f"There are {only_lower_cases} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"The sum of all the numbers {number_sum}")
print(separator)


# create empty dictionary for words length (key) and stars (values) for table below
words_length = {}


# for loop rides list word by word
for count_letters in cleaned_text:

    # putting every length of word (if already not exists) in dictionary as key with empty value
    words_length.setdefault(len(count_letters), "")

    # if the key (word_length) already exist in dictionary
    if len(count_letters) in words_length:

        # add "*" as value to the key with same word length
        words_length[len(count_letters)] += "*"


# prints table header
print(f"{'LEN':<10} {'OCCURRENCES':<20} {'NR.'}")
print(separator)


# sorting keys in filled dictionary for printing in table
for sorted_keys in sorted(words_length):

    # values of keys (stars => * )
    stars = words_length[sorted_keys]

    # length of stars (sum of stars)
    stars_count = len(words_length[sorted_keys])
    
    # printing the table
    print(f"{sorted_keys:<10} {stars:<20} {stars_count}")

