# Напишите программу, которая принимает текст и выводит два слова:
# наиболее часто встречающееся и самое длинное.

text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

set_words = set(text.split())
dictionary = [(text.count(x), x) for x in set_words]
most_common_word = max(d)[1]
print(most_common_word)

longer_word = sorted(text.split(), key=len)[-1]
print(longer_word)
