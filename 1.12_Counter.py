from collections import Counter


words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
        ]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts['into'])

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes', 'into']

a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)

d = a - b
print(d)



