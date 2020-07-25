class Trie:
  ALPHABETS = 26

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.children = [None] * self.ALPHABETS
    self.isEnd = False

  def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
    node = self
    for char in word:
      if not node.hasChar(char):
        node.put(char)
      node = node.get(char)
    node.isEnd = True

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    """
    node = self
    for char in word:
      if node.hasChar(char):
        node = node.get(char)
      else:
        return False

    return node.isEnd

  def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    node = self
    for char in prefix:
      if node.hasChar(char):
        node = node.get(char)
      else:
        return False

    return True

  def get(self, character):
    return self.children[ord(character) - 97]

  def put(self, character):
    self.children[ord(character) - 97] = Trie()

  def hasChar(self, character):
    return self.children[ord(character) - 97] is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)