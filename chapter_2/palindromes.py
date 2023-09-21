"""Find palindromes in a dictonary file."""
import load_dictionary
word_list = load_dictionary.load('words.txt')
palindromes = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palindromes.append(word)

print(f"\nNumber of palindromes found = {len(palindromes)}")
print(*palindromes, sep='\n')
