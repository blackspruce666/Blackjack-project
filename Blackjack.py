import random
print("BLACKJACK!")
print("Blackjack payout is 3:2")

def make_deck():
    i = 1
    j = 1
    k = 1
    l = 1
    deck = []
    while (i < 14):
        if i == 1 :
            deck.append(["A", "of hearts"])
        elif i == 11:
            deck.append(["J", "of hearts"])
        elif i == 12:
            deck.append(["Q", "of hearts"])
        elif i == 13:
            deck.append(["K", "of hearts"])
        else:
            deck.append([i, "of hearts"])
        i += 1

    while (j < 14):
        if j == 1 :
            deck.append(["A", "of diamonds"])
        elif j == 11:
            deck.append(["J", "of diamonds"])
        elif j == 12:
            deck.append(["Q", "of diamonds"])
        elif j == 13:
            deck.append(["K", "of diamonds"])
        else:
            deck.append([j, "of diamonds"])
        j += 1

        while (k < 14):
            if k == 1:
                deck.append(["A", "of clubs"])
            elif k == 11:
                deck.append(["J", "of clubs"])
            elif k == 12:
                deck.append(["Q", "of clubs"])
            elif k == 13:
                deck.append(["K", "of clubs"])
            else:
                deck.append([k, "of clubs"])
            k += 1

            while (l < 14):
                if l == 1:
                    deck.append(["A", "of spades"])
                elif l == 11:
                    deck.append(["J", "of spades"])
                elif l == 12:
                    deck.append(["Q", "of spades"])
                elif l == 13:
                    deck.append(["K", "of spades"])
                else:
                    deck.append([l, "of spades"])
                l += 1

    return deck
def shuffle(deck):
    random.shuffle(deck)
    return deck

def draw_card(deck):
    card = deck.pop(0)
    return card


def main():
    deck1 = make_deck()
    hand = []
    #shuffle(deck1)

    hand.append(draw_card(deck1))
    hand.append(draw_card(deck1))
    print(f"Your hand: {hand}")
    for card in deck1:
        print(card[0], card[1])


if __name__ == "__main__":
    main()