class TrieNode:
        def __init__(self, val=None):
            self.val = val
            self.children = {}
            self.isWordFinal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root

        for i in range(len(word)):
            char = word[i]
            if (char not in currentNode.children):
                currentNode.children[char] = TrieNode(char)

            currentNode = currentNode.children[char]

            if (i == len(word) - 1):
                currentNode.isWordFinal = True

    def search(self, word: str) -> bool:
        currentNode = self.root

        for i in range(len(word)):
            char = word[i]
            if (char not in currentNode.children):
                return False
            
            currentNode = currentNode.children[char]

            if (i == len(word) - 1):
                return currentNode.isWordFinal

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root

        for char in prefix:
            if (char not in currentNode.children):
                return False
            currentNode = currentNode.children[char]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)