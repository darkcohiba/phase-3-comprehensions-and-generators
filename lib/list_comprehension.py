#!/usr/bin/env python3
# import pyautogui

# pyautogui.moveRel(0, 50, duration = 1)
# pyautogui.moveRel(0, -150, duration = 1)

# def repeat_movement(num):
#     i = 0
#     while i < num:
#         pyautogui.moveRel(0, 50, duration = 1)
#         pyautogui.moveRel(0, 150, duration = 10)
#         pyautogui.moveTo(10, 10, 50)
#         i += 1


def return_evens(num_list):
    seq= []
    for i in num_list:
        if i % 2 == 0:
            seq.append(i)
    return seq



def make_exclamation(sentence_list):
    exclamation_list = []
    for i in sentence_list:
        exclamation_list.append(i + "!")
    return exclamation_list




