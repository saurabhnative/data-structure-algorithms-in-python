# python program for insert and search operations in tries
class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.get_node()

    @staticmethod
    def get_node():
        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    @staticmethod
    def _char_to_index(ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch) - ord('a')

    def insert(self, key):
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            # if current character is not present
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]

        # mark last node as leaf
        p_crawl.isEndOfWord = True

    def search(self, key):
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]

        return p_crawl is not None and p_crawl.isEndOfWord


# driver function
def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

        # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()