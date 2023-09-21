def pig_latin(word):
    vowels = ['a','e','i','o','u']
    if word[0].lower() in vowels:
        return word + "way"
    return word[1:] + word[0] + "ay"

words = ["task","nix","oven","unexpected","hello"]
for word in words:
    print(pig_latin(word))
