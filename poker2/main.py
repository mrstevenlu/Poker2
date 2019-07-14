# -*- coding: UTF-8 -*-

# author by : Steven Lu

from machine.std_machine import create_deck,\
    shuffled_deck,\
    record_deck

from dealer.mike import deal_to_a_player,deal_to_multi_players

# 拿出一副新牌
first_deck = []
create_deck(first_deck)
record_deck(first_deck, "deck-001.txt")

shuffled_deck(first_deck)
record_deck(first_deck, "deck-002.txt")
'''
# 发牌
player1_deck = []
deal_to_a_player(first_deck, 5, player1_deck)
record_deck(player1_deck, "player1_deck.txt")

player2_deck = []
deal_to_a_player(first_deck, 10, player2_deck)
record_deck(player2_deck, "player2_deck.txt")
'''

Steven_deck=[]
Vivian_deck=[]
Monica_deck=[]
Jimmy_deck=[]

deal_to_multi_players(first_deck,Steven_deck,Vivian_deck,Monica_deck)
record_deck(Steven_deck,"Steven_deck.txt")
record_deck(Vivian_deck,"Vivian_deck.txt")
record_deck(Monica_deck,"Monica_deck.txt")
record_deck(Jimmy_deck,"Jimmy_deck.txt")
