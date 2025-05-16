class MagicDictionary:

    def __init__(self):
        # Create an empty space in memory so that will be populated later
        self.words = set()

    def build_dic(self, dictionary):
        # Populate the empty set using words provided by user
        for word in dictionary:
            self.words.add(word)

    def search(self, search_term):
        # Check for all words with the same length as search term.
        count = 0
        for word in self.words:
            if len(word) == len(search_term):
                # Compare characters in both words and see whether there's exactly one letter that is different.
                for char in range(len(word)):
                    if word[char] != search_term[char]:
                        count += 1
                    if count > 1:
                        break
                if count == 1:
                    return True
        return False


magic = MagicDictionary()
magic.build_dic(["Hello", "Make"])
magic.search("nice")

print(magic.search("Nike"))
print(magic.search("Pello"))
print(magic.search("Dake"))
