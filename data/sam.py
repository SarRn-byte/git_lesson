class MinMaxWordFinder:
    def __init__(self):
        self.text = []

    def add_sentence(self, add):
        for i in add.split():
            self.text.append((len(i), i))


def shortest_words(self):
    return sorted([j[1] for j in self.text if j[0] == sorted([i[0] for i in self.text])[0]])


def longest_words(self):
    return sorted(set([j[1] for j in self.text if j[0] == sorted([i[0] for i in self.text])[-1]]))
