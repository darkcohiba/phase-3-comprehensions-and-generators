#!/usr/bin/env python3
import pyautogui

pyautogui.moveRel(0, 50, duration = 1)
pyautogui.moveRel(0, -150, duration = 1)

def repeat_movement(num):
    i = 0
    while i < num:
        pyautogui.moveRel(0, 50, duration = 1)
        pyautogui.moveRel(0, -150, duration = 10)
        i += 1

def return_evens(num_list):
    pass

def make_exclamation(sentence_list):
    pass



