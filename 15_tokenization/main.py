import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Dog ate Cat"
text1 = "Cat ate Dog"

print(enc.encode(text))
print(enc.encode(text1))

# print(len(enc.encode(text)))

print(enc.decode([49080, 28397, 19288]))
print(enc.decode([23546, 28397, 18018]))