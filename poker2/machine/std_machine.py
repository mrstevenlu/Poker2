# -*- coding: UTF-8 -*-

# author by : Steven Lu

import random
import os
import codecs


def create_deck(new_deck):
    '推出一副新牌'
    print('\n 新牌')
    jokers = ('♞', '♘')

    marks = ('♠', '♥', '♦', '♣')

    nums = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    for c in jokers:
        new_deck.append(c)

    for cn in nums:
        for cm in marks:
            card = cm + cn
            new_deck.append(card)
    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'
    print('\n 洗牌完毕')
    random.shuffle(deck_to_be_shuffled)
    return


def record_deck(deck_to_be_record, filename):
    '记录一副牌'
    print('\n 记录扑克牌')
    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close
    return
