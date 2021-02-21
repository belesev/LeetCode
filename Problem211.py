# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
# word may contain dots '.' where dots can be matched with any letter.

class TreeNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = set()

    def append_child(self, child_node):
        self.children.add(child_node)

    def has_child(self, c):
        for child in self.children:
            if child.letter == c:
                return child
        return None

class WordDictionary:

    def __init__(self):
        self.__head = TreeNode(None)
        self.__eow = '-'

    def addWord(self, word: str) -> None:
        node = self.__head
        for c in word:
            tmp = node.has_child(c)
            if tmp:
                node = tmp
            else:
                new_node = TreeNode(c)
                node.append_child(new_node)
                node = new_node
        # special mark symbol meaning end of the word
        node.append_child(TreeNode(self.__eow))

    def search(self, word: str) -> bool:
        return self.__search(word, self.__head)

    def __search(self, word: str, node) -> bool:
        if not len(word):
            return node.has_child(self.__eow)

        look_for = word[0]
        if look_for != '.':
            tmp = node.has_child(look_for)
            if not tmp:
                return False
            return self.__search(word[1:], tmp)
        else:
            for child in node.children:
                tmp_result = self.__search(word[1:], child)
                if tmp_result:
                    return True
            return False
