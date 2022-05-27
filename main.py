# READ FILE FUNCTION
def read_file_content(filename):
    with open(filename) as f:
        contents = f.read()
    return contents

word_bank = {}
word_bank_array = []
# COUNT WORDS FUNCTION
def count_words():
    text = read_file_content("./story.txt")
    word_bankItem = text.split()
    word_bank_array = word_bankItem
    for i in word_bank_array:
        counter = word_bank_array.count(i)
        word_bank[i] = counter
    return word_bank

print(count_words())
