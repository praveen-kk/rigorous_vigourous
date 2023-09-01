import re
import collections


class resd_unique_words:
    #constructor
    def __init__(self, file):
        self.file = file
    def find_unique_word(self):
        text_file = open(file, 'r')
        text = text_file.read()

        text = text.lower()
        words = text.split()
        words = [word.strip('.,!,()[]') for word in words]
        words = [word.replace("'s", "") for word in words]
        unique = []
        for word in words:
            if word not in unique:
                unique.append(word)
        return unique


file = 'word_list'
# unique_words = resd_unique_words
print(resd_unique_words.find_unique_word(file))

# if __name__ == '__main__':
#     main()
#     print(resd_unique_words.find_unique_word(file))
# #     print(unique_words.find_unique_word())
