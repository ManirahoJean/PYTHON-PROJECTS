# 5.4 using loop

programming_words = {
    'string': 'series of characters',
    'comment': 'notes in the program that can not be executed',
    'print': 'display the output of the program',
    'list': 'collection of items',
    'dictionary': 'collection of key values'
}
for key, value in programming_words.items():
    print(f"\nPython word: {key.title()}")
    print(f"Meaning: {value}")
