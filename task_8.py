# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются
# слева направо и справа налево.

word1 = 'abccba'
word2 = 'abccBa'

print(word1 == word1[::-1])
print(word2 == word2[::-1])
