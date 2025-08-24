# Task 1: 

user = input('Enter a sentence: ')


print('The length of your sentence is: ',len(user))
print(f"Hint for the Smallest character (ASCII value): {ord(min(user))}")
print(f"Hint for the Largest character (ASCII value): {ord(max(user))}")

print('----------------------------')
guess_smallest_character = input('Guess the smallest characters based on these ASCII hints: ')
guess_largest_character = input('Guess the largest characters based on these ASCII hints: ')

print('----------------------------')
if guess_smallest_character == min(user):
    print('Correct!. It is ', min(user))
else:
    print('Incorrect. The answer is actually: ', min(user))

if guess_largest_character == max(user):
    print('Correct!. It is ', max(user))
else:
    print('Incorrect. The answer is actually: ', max(user))

#------------------------------------------------------------------------------------------------------------------------

# Task 2:
word  = 'Anywhere'
middle_character = word[len(word) //2] 

print(f'First character: {word[0]}')
print(f'Middle character: {middle_character}')
print(f'Last character: {word[-1]}')

for i in word[::2]: # printing every second character in the str
    print(i)

swapped_word = word[-1] + word[1:-1] + word[0] # swapping letters in word
print('String in word is updated to: ', swapped_word)

#------------------------------------------------------------------------------------------------------------------------

# Task 6:
word1 = "tiger"
word2 = "zebra"

print("word1 == word2:", word1 == word2)
print("word1 < word2:", word1 < word2)
print("word1 > word2:", word1 > word2)

if word1 == word2:
    print('Both strings are equal')

if word1 < word2:
    print(f'The word {word1} comes alphabetically first')
elif word1 > word2:
    print(f'The word {word2} comes alphabetically first')
else:
    print("The strings are identical in position.")

#------------------------------------------------------------------------------------------------------------------------

# Task 7:

text = 'Greeting my friends'
count_consonants = 0
count_vowels = 0 

# looping to print only vowels
print('The vowels are: ') 
for i in text:
    if i in 'aeiouAEIOU': 
        print(i,end=' ')
print()


# looping to find only consonants count
for j in text: 
    if j.isalpha() and j not in 'aeiou':
        count_consonants +=1
print('Consonants count: ', count_consonants) 

#-------------------------
print('-------------------------')
# count and print vowels and consonants in reversed order

    # Vowel:
print('The vowels are: ') 
for i in text:
    if i in 'aeiouAEIOU': 
        print(i,end=' ')
        count_vowels += 1
print()
print('Vowel counts: ', count_vowels)

    # Consonants:
count_consonants_part2 = 0
print('Consonants are: ')
for j in text: 
    if j.isalpha() and j not in 'aeiou':
        print(j, end=' ')
        count_consonants_part2 +=1
print()
print('Consonants count: ', count_consonants_part2) 


#------------------------------------------------------------------------------------------------------------------------

# Task 8:

user = input('Input any string (no space) or number: ')

if user.isalpha():
    print("Alphabet Only.")
elif user.isdigit():
    print("Numbers Only.")
elif user.isalnum():
    print("Mix of Letters and Numbers.")
else:
    print('Input again. No space')


#------------------------------------------------------------------------------------------------------------------------

# Task 10:

sentence = 'Hello this is me'
uppercase_sentence = sentence.upper()
print(uppercase_sentence)

splitted_sentence = uppercase_sentence.split()
abbreviation = ''.join([i[0] for i in splitted_sentence])
print('Abbreviation: ',abbreviation)

# convert this abbreviation to lowercase:
lowercase_abbreviation = abbreviation.lower()
print('Lowercase abbreviation: ', lowercase_abbreviation)

#------------------------------------------------------------------------------------------------------------------------
# END







