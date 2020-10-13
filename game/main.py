import random
from stone import stone
from gun import gun
from water import water
from air import air
from paper import paper
from sponge import sponge
from human import human
from scissors import scissors
from fire import fire

state = True

while state:
    player_element = input()
    player_element.lower()
    pc_element = random.randint(1, 9)
    if player_element == "камень" or player_element == "stone":
        stone(pc_element)
    if player_element == "пистолет" or player_element == "gun": 
        gun(pc_element)
    if player_element == "вода" or player_element == "water":
        water(pc_element)
    if player_element == "воздух" or player_element == "air":
        air(pc_element)
    if player_element == "бумага" or player_element == "paper":
        paper(pc_element)
    if player_element == "губка" or player_element == "sponge":
        sponge(pc_element)
    if player_element == "человек" or player_element == "human":
        human(pc_element)
    if player_element == "ножницы" or player_element == "scissors":
        scissors(pc_element)
    if player_element == "огонь" or player_element == "fire":
        fire(pc_element)
    if player_element == "выход" or player_element == "exit":
    	break
