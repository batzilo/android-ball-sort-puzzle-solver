"""A trie data structure for the Android Bubble Sort Puzzle Solver."""


class TrieNode:
    """A trie node class."""

    def __init__(self, char):
        """Create a trie node."""
        self.char = char
        self.children = {}
        self.eow = False


class Trie:
    """A trie class."""

    def __init__(self):
        """Create a trie."""
        self.root = TrieNode(None)

    def add(self, word):
        """Add a word to the trie."""
        t = self.root
        for c in word:
            if c not in t.children:
                t.children[c] = TrieNode(c)
            t = t.children[c]
        t.eow = True

    def contains(self, word):
        """Check if a word is in the trie."""
        t = self.root
        for c in word:
            if c not in t.children:
                return False
            t = t.children[c]
        return t.eow
