n = int(input())
words = []
for i in range(n):
	words.append(input())

for i in range(n-1):
	word = input()
	if word in words:
		popIdx = words.index(word)
		words.pop(popIdx)
print(words[0])
