"""Find all word-pair palingrams in a dictionary file."""
import time
import load_dictionary

word_list = load_dictionary.load('words.txt')

# find word-pair palingrams
def find_palingrams():
    """Find dictionary plaingrams"""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word,rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i],word))

    return pali_list

start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()

# sort palingrams on first word
plaingrams_sorted = sorted(palingrams)

# display list of palingrams
for first, second in plaingrams_sorted:
    print(f"{first} {second}")
print(f"\nNumber of plaingrams = {len(plaingrams_sorted)}")

print(f"Runtime for tyhis program was {end_time - start_time} seconds.")
