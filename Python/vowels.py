text = "hello"
count = 0
for ch in text:
    if ch.lower() in "a e i o u":
        count += 1
        print("vowels:", count)
