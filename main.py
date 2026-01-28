# 1
s = "banana"
unique = ""
for ch in s:
    if ch not in unique:
        unique += ch
print(unique)


# 2
s = "Hello123@#"
letters = digits = others = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        others += 1
print(letters, digits, others)


# 3
s = "python is awesome"
lengths = []
for word in s.split():
    lengths.append(len(word))
print(lengths)


# 4
s = "data science machine learning"
longest = ""
for word in s.split():
    if len(word) > len(longest):
        longest = word
print(longest)


# 5
s = "comprehension"
result = ""
for ch in s:
    if ch not in "aeiou":
        result += ch
print(result)
