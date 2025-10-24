# Use this website: https://regexr.com/ to test regular expressions


import re

def example1():
    text = r"woodchuck, Woodchuck, woodChucks, Woodchucks"
    regex = r"[wW]oodchucks?"

    # /b: word break
    # [] allows you to have logical OR inside a character class
    # ?: makes the previous character optional. In this case, the "s" is optional to search. 
        #  You can place ? like this: [wW]oodch?ucks. This would make the "h" optional to search. 

    search = re.findall(regex, text)
    print(search)

def example2():
    
    text = r"We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable rights, that among these are Life, Liberty, and the pursuit of Happiness. Lifespan, lifee"
    regex = r"[A-Za-z]+," # Finding words that end with a comma

    search = re.findall(regex, text)
    print("Finding words that end with a comma", search)

def example3():
    
    text = r"We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable rights, that among these are Life, Liberty, and the pursuit of Happiness. Lifespan, lifee"
    regex = r"[A-Z]" # Finding uppercase letters

    search = re.findall(regex, text)
    print("Finding uppercase letters", search)

def example4():
    text = """
        In Phnom Penh, students rush to universities every morning. Some carry laptops, others notebooks. At cafes, you can find coffee, fresh pastries, and friendly conversations. 
        On the streets, motorbikes zoom past, while vendors sell noodles, fruits, and local snacks. 
        Tourists visit the Royal Palace, the National Museum, and riverside parks. 
        Many students are learning Python, cybersecurity, mathematics, and literature. 
        Email addresses like student1@university.edu or visitor123@gmail.com are used for contact. 
        Phone numbers often look like 012345678 or 098765432. 
        The city is full of energy, creativity, and ambition, reflecting the hopes of a bright generation.
        """

    # 1. Extract all words that start with a capital letter.
    regex1 = r"\b[A-Z][a-zA-Z]+\b"
    search1 = re.findall(regex1, text)
    print("1. Words starting with capital:", search1)

    # 2. Extract all email addresses
    regex2 = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    search2 = re.findall(regex2, text)
    print("2. Emails:", search2)

    # 3. Find first occurrence of "students"
    first_occurrence = text.find("students")
    print("3. First occurrence of 'students':", first_occurrence)

    # 4. Check if Python exists
    if re.search(r"\bPython\b", text):
        print("4. Python course detected!")

    # 5. Split into words ignoring punctuation
    words = re.findall(r"\b\w+\b", text)
    print("5. Words (ignoring punctuation):", words)

    # 6. Replace phone numbers with [PHONE]
    replaced_phones = re.sub(r"\b\d{9}\b", "[PHONE]", text)
    print("6. Text with phones replaced:\n", replaced_phones)

    # 7. Replace email addresses with [EMAIL]
    replaced_emails = re.sub(regex2, "[EMAIL]", replaced_phones)
    print("7. Text with emails replaced:\n", replaced_emails)

    # 8. Count "students" using findall + len
    students_count = len(re.findall(r"\bstudents\b", text))
    print("8. 'students' count:", students_count)

    # 9. Extract all words longer than 8 characters
    long_words = [w for w in words if len(w) > 8]
    print("9. Words longer than 8 characters:", long_words)

def example5():
    text = "this is a test 123."

    regex = re.findall(r"[tT]est",text)
    regex_split = re.split(r"[tT]est",text)
    regex_hex = re.findall(r"\x61",text)
    finding_dot = re.findall(r"\.$",text) # Use \ to escape special characters like "."

    print(regex_split)
    print(regex)
    # print(regex.start())
    # print(regex.end())
    # print(regex.span()) # This is a tuple
    print(regex_hex)
    print(finding_dot)

    # Replace 
    print("line1\rline2") # \r is carriage return. line2 will overwrite line1, but only it has the same or more characters than line1
    print("line12\rline2") # line2 will overwrite line1, but only it rewrite what it has the same or more characters than line1

#example4()
example4()