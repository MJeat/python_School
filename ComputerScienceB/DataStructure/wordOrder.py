
n = int(input())


# To count words
word_count = {}
order = []

for _ in range(n):
    word = input().strip()
    if word not in word_count:
        word_count[word] = 0
        order.append(word)
    word_count[word] += 1

print(len(order))  # Number of words
print(' '.join(str(word_count[word]) for word in order))  # Counts in order of first appearance









