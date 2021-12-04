class Card(object):
    def __init__(self):
        self.fields = []
        self.bingo = False
        self.winning_call = -1
        for i in range (0, 5):
            self.fields.append([])
            for j in range(0, 5):
                self.fields[i].append(Field())

class Field(object):
    def __init__(self):
        self.number = -1
        self.marked = False

def check_for_bingo(card):
    for i in range(0, 5):
        bingo = True
        for j in range(0, 5):
            bingo &= card.fields[i][j].marked
        if bingo:
            return True
    for j in range(0, 5):
        bingo = True
        for i in range(0, 5):
            bingo &= card.fields[i][j].marked
        if bingo:
            return True

cards = []
calls = []
cards = []

with open('input.txt', 'r+') as file:
    lines = file.readlines()
    calls = list(map(lambda i: int(i), str.split(lines[0], ",")))
    c = 2
    while c < len(lines):
        card = Card()
        for i in range(0, 5):
            for j in range(0, 5):
                card.fields[i][j].number = int(lines[c+i][0+j*3:3+j*3])
        cards.append(card)
        c += 6

winners = []

for call in calls:
    for card in cards:
        for row in card.fields:
            for field in row:
                if field.number == call:
                    field.marked = True
        card.bingo = check_for_bingo(card)
        if card.bingo:
            card.winning_call = call
            winners.append(card)
    cards = list(filter(lambda c: not c.bingo, cards))

s = 0
for row in winners[len(winners)-1].fields:
    for field in row:
        if not field.marked:
            s += field.number

print(s * winners[len(winners)-1].winning_call)