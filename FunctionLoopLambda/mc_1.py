#🧩 Mini Challenge 1: Function with Loop

#Create a function count_vowels(word) that takes a word and counts how many vowels (a, e, i, o, u) are in it.


name = "sndfuahsdasduawdbaodjasdhiwda;skpckpaskdaikdq"

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count=0

vowel_counter = len(list(filter(lambda x:x in vowels,name)))
print(vowel_counter)