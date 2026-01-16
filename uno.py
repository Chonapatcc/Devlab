def get_input():
    return sort_by_color_and_number(input().strip().split(" "))

def sort_by_color_and_number(list_cards):
    color_order = {'R': 0, 'G': 1, 'B': 2, 'Y': 3}
    return sorted(list_cards, key=lambda card: (color_order[card[1]], int(card[0])))

def print_remain_cards(players_card, top_card):
    print("------------------")
    print("Current Card: {}".format(top_card))
    print("Table hands:")
    for i in range(4):
        print("Player {}: {}".format(i+1," ".join(players_card[i])))

    print("------------------")
        

players_card = [[]]*4
for i in range(4):
    players_card[i] = get_input()

top_card = input().strip()
is_play = True
while is_play:
    is_play = False
    for i in range(4):
        list_1 = [] # match color and number
        list_2 = [] # match number only
        list_3 = [] # match color only

        for card in players_card[i]:
            if card[0] == top_card[0] and card[1] == top_card[1]:
                list_1.append(card)
            elif card[0] == top_card[0]:
                list_2.append(card)
            elif card[1] == top_card[1]:
                list_3.append(card)
        
        if len(list_1) > 0:
            play_card = list_1[0]
            is_play = True
            print("Player <x> place <card> card to match <table> in both number and color".replace("<x>", str(i+1)).replace("<card>", play_card).replace("<table>", top_card))
        elif len(list_2) > 0:
            play_card = list_2[0]
            is_play = True
            print("Player <x> place <card> card to match <table> in number".replace("<x>", str(i+1)).replace("<card>", play_card).replace("<table>", top_card))
        elif len(list_3) > 0:
            play_card = list_3[0]
            is_play = True
            print("Player <x> place <card> card to match <table> in color".replace("<x>", str(i+1)).replace("<card>", play_card).replace("<table>", top_card))
        else:
            print("Player <x> does not have a card to place".replace("<x>", str(i+1)))
            is_play =False
            break

        top_card = play_card
        players_card[i].remove(play_card)
        print("Now the current card is <table>...".replace("<table>", top_card))

print_remain_cards(players_card, top_card)