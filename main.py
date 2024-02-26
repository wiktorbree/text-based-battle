import os
import sys
from character import Hero, Enemy
from weapon import short_bow, iron_sword, fists

def rematch():
    again = input('Try again? (yes/no): ')
    if again == 'yes':
        play()
    elif again == 'no':
        sys.exit()
    else:
        print('Wrong input!')
        again = input('Try again? (yes/no): ')

def play():
    hero = Hero(name='Hero', health=100)
    enemy = Enemy(name='Enemy', health=100, weapon=short_bow)

    os.system("clear")
    hero_weapon = input(f'Choose your weapon: 1. {iron_sword.name}, 2. {short_bow.name}, 3. {fists.name}: ')
    if hero_weapon == '1':
        hero.equip(iron_sword)
    elif hero_weapon == '2':
        hero.equip(short_bow)

    while True:
        os.system("clear")
        hero.attack(enemy)
        enemy.attack(hero)

        hero.health_bar.draw()
        enemy.health_bar.draw()

        if (hero.health == 0) and (enemy.health == 0):
            print('\33[93mDRAW!\033[0m')
            rematch()
        elif hero.health == 0:
            print('\033[91mYOU LOST!\033[0m')
            rematch()
        elif enemy.health == 0:
            print('\033[92mYOU WON!\033[0m')
            rematch()

        input()

play()