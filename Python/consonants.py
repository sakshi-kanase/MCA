text = "hello worlds"
vowels = 0
consonants = 0
blanks = 0
for ch in text:
    if ch.lower() in "a e i o u":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch == "":
        blanks += 1

print("vowels:",vowels)
print("consonants:",consonants)
print("blanks:",blanks)
