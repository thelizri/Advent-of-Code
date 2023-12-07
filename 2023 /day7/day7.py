# Every hand is exactly one type. From strongest to weakest, they are:

#    Five of a kind, where all five cards have the same label: AAAAA
#    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#    High card, where all cards' labels are distinct: 23456

# Creating a dictionary for the specified characters with A as the highest value and 2 as the lowest
import functools

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_values = {card: value for value, card in enumerate(reversed(cards), 1)}

# Creating a dictionary for the different hand rankings in poker, each with a unique score

hand_rankings = {
    "five_kind": 8,  # Highest ranking
    "four_kind": 7,
    "house": 6,
    "three_kind": 5,
    "two_pair": 4,
    "one_pair": 3,
    "high_card": 2,  # Lowest ranking
}

text = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

text = open("day7.txt").read().splitlines()


def get_hand_ranking(card_hand, joker=False):
    count = {}
    for card in card_hand:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1

    if joker and "J" in count:
        max_key, max = "J", 0
        for key, value in count.items():
            if key == "J":
                continue
            if value >= max:
                max = value
                max_key = key
        if max_key != "J":
            count[max_key] += count["J"]
            del count["J"]

    if len(count) == 1:
        return hand_rankings["five_kind"]
    elif len(count) == 2:
        # Four of a Kind or Full House
        if 4 in count.values():
            return hand_rankings["four_kind"]
        else:
            return hand_rankings["house"]
    elif len(count) == 3:
        if 3 in count.values():
            return hand_rankings["three_kind"]
        else:
            return hand_rankings["two_pair"]
    elif len(count) == 4:
        return hand_rankings["one_pair"]
    else:
        return hand_rankings["high_card"]


def compare_hands(hand1, hand2):
    card_hand1, _, hand_rank1 = hand1
    card_hand2, _, hand_rank2 = hand2

    if hand_rank1 == hand_rank2:
        for c1, c2 in zip(card_hand1, card_hand2):
            v1, v2 = card_values[c1], card_values[c2]
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0
    elif hand_rank1 > hand_rank2:
        return 1
    else:
        return -1


def get_score(joker=False):
    all_hands = []

    for row in text:
        card_hand, bid = row.split()
        bid = int(bid)
        hand_rank = get_hand_ranking(card_hand, joker)
        all_hands.append((card_hand, bid, hand_rank))
    result = 0
    all_hands.sort(key=functools.cmp_to_key(compare_hands))

    for number, hand in enumerate(all_hands, 1):
        _, bid, _ = hand
        result += bid * number
    return result


print("Part 1:", get_score())

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
card_values = {card: value for value, card in enumerate(reversed(cards), 1)}

print("Part 2:", get_score(True))
