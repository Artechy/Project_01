"""
projekt01.py: first project for Engeto - Online Python Akademy

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
    "bob": 123,
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

separator = 45 * "-"


user_name = input(f"Hello! Enter your username: ")
user_password = input(f"Now enter your password: ")
print(separator)

if user_name in registered_users:                                           # controls if entered user name is matching any key in dict
    if user_password == str(registered_users[user_name]):                   # controls if entered user password is matching key value
        print(f"Welcome to the application, {user_name}.")
        print(f"We have 3 different texts to be analyzed.")
        print(separator)
    else:
        print("Unregistered user, terminating the program...")
        exit()
else:
    print("Unregistered user, terminating the program...")
    exit()


selected_text = input("Enter a number btw. 1 and 3 to select text: ")
print(separator)

if selected_text.isdigit() and 1 <= int(selected_text) <= 3:                        # controls if input is only numbers 1-3
    pass
else:
    print("Enter only numbers btw. 1 and 3! Terminating the program...")
    exit()

cleaned_text_01 = TEXTS[0].replace(",", " ").replace(".", " ").split()              # cleaning all the texts from all dots and commas, splitting single words in the list
cleaned_text_02 = TEXTS[1].replace(",", " ").replace(".", " ").split()
cleaned_text_03 = TEXTS[2].replace(",", " ").replace(".", " ").split()

words_count = 0                                                                     # variables for counting words and numbers   
starts_with_upper_case = 0
only_upper_cases = 0
only_lower_cases = 0
number_count = 0                                                                                 
number_sum = 0


if selected_text == "1":                                                            # user choose text number 1
    
    for search_text in cleaned_text_01:                                             # for loop rides cleaned text in the list word by word

        if search_text.isascii():                                                   # searching all words in text
            words_count = words_count + 1                                           # counting all words
        
        if search_text[0].isupper() and not search_text.isupper():                  # searching words that starts with upper case
            starts_with_upper_case = starts_with_upper_case +1                      # counting words that starts with upper case

        if search_text.isupper():                                                   # searching words that contains only upper cases
            only_upper_cases = only_upper_cases +1                                  # counting words that contains only upper cases

        if search_text.islower():                                                   # searching words that contains only lower cases
            only_lower_cases = only_lower_cases + 1                                 # counting words that contains only lower cases

        if search_text.isdigit():                                                   # searching all digits in text
            number_count = number_count + 1                                         # counting all digits in text
            number_sum = number_sum + int(search_text)                              # summation of all digits in text


if selected_text == "2":                                                            # user choose text number 2
    
    for search_text in cleaned_text_02:                                             # for loop rides cleaned text in the list word by word
        
        if search_text.isascii():                                                   # searching all words in text
            words_count = words_count + 1                                           # counting all words
        
        if search_text[0].isupper() and not search_text.isupper():                  # searching words that starts with upper case
            starts_with_upper_case = starts_with_upper_case +1                      # counting words that starts with upper case

        if search_text.isupper():                                                   # searching words that contains only upper cases
            only_upper_cases = only_upper_cases +1                                  # counting words that contains only upper cases

        if search_text.islower():                                                   # searching words that contains only lower cases
            only_lower_cases = only_lower_cases + 1                                 # counting words that contains only lower cases

        if search_text.isdigit():                                                   # searching all digits in text
            number_count = number_count + 1                                         # counting all digits in text
            number_sum = number_sum + int(search_text)                              # summation of all digits in text


if selected_text == "3":                                                            # user choose text number 3
    
    for search_text in cleaned_text_03:                                             # for loop rides cleaned text in the list word by word

        if search_text.isascii():                                                   # searching all words in text
            words_count = words_count + 1                                           # counting all words
        
        if search_text[0].isupper() and not search_text.isupper():                  # searching words that starts with upper case
            starts_with_upper_case = starts_with_upper_case +1                      # counting words that starts with upper case

        if search_text.isupper():                                                   # searching words that contains only upper cases
            only_upper_cases = only_upper_cases +1                                  # counting words that contains only upper cases

        if search_text.islower():                                                   # searching words that contains only lower cases
            only_lower_cases = only_lower_cases + 1                                 # counting words that contains only lower cases

        if search_text.isdigit():                                                   # searching all digits in text
            number_count = number_count + 1                                         # counting all digits in text
            number_sum = number_sum + int(search_text)                              # summation of all digits in text


print(f"There are {words_count} words in the selected text.")                       # prints all results
print(f"There are {starts_with_upper_case} titlecase words.")
print(f"There are {only_upper_cases} uppercase words.")
print(f"There are {only_lower_cases} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"The sum of all the numbers {number_sum}")
print(separator)


words_length = {}                                                                           # create empty dictionary for words length (key) and stars (values) for table below

if selected_text == "1":                                                                    # user choose text 1

    for count_letters in cleaned_text_01:                                                   # for loop rides list word by word

        words_length.setdefault(len(count_letters), "")                                     # putting every length of word (if already not exists) in dictionary as key with empty value

        if len(count_letters) in words_length:                                              # if the key (word length) already exist in dictionary
            
            words_length[len(count_letters)] = words_length[len(count_letters)] + "*"       # add "*" as value to the key with same word length


if selected_text == "2":                                                                    # user choose text 2

    for count_letters in cleaned_text_02:                                                   # for loop rides list word by word

        words_length.setdefault(len(count_letters), "")                                     # putting every length of word (if already not exists) in dictionary as key with empty value

        if len(count_letters) in words_length:                                              # if the key (word length) already exist in dictionary
            
            words_length[len(count_letters)] = words_length[len(count_letters)] + "*"       # add "*" as value to the key with same word length


if selected_text == "3":                                                                    # user choose text 3

    for count_letters in cleaned_text_03:                                                   # for loop rides list word by word

        words_length.setdefault(len(count_letters), "")                                     # putting every length of word (if already not exists) in dictionary as key with empty value

        if len(count_letters) in words_length:                                              # if the key (word length) already exist in dictionary
            
            words_length[len(count_letters)] = words_length[len(count_letters)] + "*"       # add "*" as value to the key with same word length


print(f"{'LEN|':<10}{'OCCURRENCES':<20}{'|NR.'}")                   # prints table header
print(separator)

for sorted_keys in sorted(words_length):                            # sorting keys in filled dictionary for printing in table

    stars = words_length[sorted_keys]                               # values of keys (stars => * )
    stars_count = len(words_length[sorted_keys])                    # length of stars (sum of stars)
    
    print(f"{sorted_keys:<10}{stars:<20} {stars_count}")            # printing the table
