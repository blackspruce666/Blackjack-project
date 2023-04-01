import random
import Money

print("BLACKJACK!")
print("Blackjack payout is 3:2")


def make_deck():
    i = 1
    j = 1
    k = 1
    l = 1
    deck = []


    while (i < 14):
        if i == 1:
            deck.append(["A", "of hearts", 11])
        elif i == 11:
            deck.append(["J", "of hearts", 10])
        elif i == 12:
            deck.append(["Q", "of hearts", 10])
        elif i == 13:
            deck.append(["K", "of hearts", 10])
        else:
            deck.append([i, "of hearts", i])
        i += 1


    while (j < 14):
        if j == 1:
            deck.append(["A", "of diamonds", 11])
        elif j == 11:
            deck.append(["J", "of diamonds", 10])
        elif j == 12:
            deck.append(["Q", "of diamonds", 10])
        elif j == 13:
            deck.append(["K", "of diamonds", 10])
        else:
            deck.append([j, "of diamonds", j])
        j += 1

    while (k < 14):
        if k == 1:
            deck.append(["A", "of clubs", 11])
        elif k == 11:
            deck.append(["J", "of clubs", 10])
        elif k == 12:
            deck.append(["Q", "of clubs", 10])
        elif k == 13:
            deck.append(["K", "of clubs", 10])
        else:
            deck.append([k, "of clubs", k])
        k += 1

    while (l < 14):
        if l == 1:
            deck.append(["A", "of spades", 11])
        elif l == 11:
            deck.append(["J", "of spades", 10])
        elif l == 12:
            deck.append(["Q", "of spades", 10])
        elif l == 13:
            deck.append(["K", "of spades", 10])
        else:
            deck.append([l, "of spades", l])
        l += 1

    return deck


def shuffle(deck):
    random.shuffle(deck)
    return deck


def draw_card(deck):
    card = deck.pop(0)
    return card


def score_hand(hand):
    score = []
    a = 11
    for card in hand:
        score.append(card[2])

    while sum(score) > 21 and a in list:
        for i in score:
            if i == 11:
                i = 1
    return sum(score)


def display_1_dealer(hand):
    print()
    print(f"DEALER'S SHOWN CARD:")
    print(f"{hand[0][0]} {hand[0][1]}")
    return hand


def display_cards_player(hand):
    print()
    print(f'YOUR CARDS:')
    for x in hand:
        print(f"{x[0]} {x[1]}")
    return hand


def hit_or_stand(hand, deck):
    while True:
        print()
        hos = input("Hit or stand? (hit/stand):    ")
        if hos.lower() == "hit":
            hand.append(draw_card(deck))
            display_cards_player(hand)

        elif hos.lower() == "stand":
            return hand


def main():
    #make and shuffle deck
    deck1 = make_deck()
    shuffle(deck1)

    #initialize hands as empty lists
    hand = []
    dealer_hand = []

    #deal cards to player and dealer
    hand.append(draw_card(deck1))
    dealer_hand.append(draw_card(deck1))
    hand.append(draw_card(deck1))
    dealer_hand.append(draw_card(deck1))

    display_1_dealer(dealer_hand)

    display_cards_player(hand)

    hand = hit_or_stand(hand, deck1)

    player_score = score_hand(hand)

    if player_score == 21:
        print("WINNER WINNER CHICKEN DINNER")









if __name__ == "__main__":
    main()