__author__ = "Jamal Combs"
__copyright__ = "Copyright 2018"

import random
import time
from character import Character
from enemies import Enemies

# create main character
def character():
    character = Character('Lio', '6-weeks old', 'Male', 'Conure', 'Explorer', 'Naked and of unknown origin.')

    character_name_intro = 'Lio: The Unclothed Enigma'
    character_description = 'Light-footed and graceful, the beautiful and deadly Lio is in his element while airborne.'
    character_intro = character.intro(character_name_intro, character_description)

    character_armor_color = 'Crimson'
    character_armor_type = 'Light'
    character_armor_set = character.armor(character_armor_color, character_armor_type)

    return (character, character_intro, character_armor_set)

# use this for initialization
def main():
        enemies = Enemies()
        main_character = character()[0]
        main_character_content = character()[1]
        main_character_armor = character()[2]

        # line spacer
        spacer = '----------------------------------------------'

        print(spacer)
        print('Character Intro: {0}'.format(main_character_content[0]))
        print(spacer)
        print('Character Intro: {0}'.format(main_character_content[1]))
        print(spacer)
        time.sleep(2)
        print('Character Details: {0} || {1} || {2} || {3} || {4} || {5}'.format(main_character.name,
        main_character.age, main_character.race, main_character.sex, main_character.role, main_character.cult))
        time.sleep(2)
        print(spacer)
        print('Armor: {0} || {1}'.format(main_character_armor[0], main_character_armor[1]))
        time.sleep(2)
        print(spacer)
        print('Predators Approaching...')
        time.sleep(2)
        print(spacer)
        print(main_character.select_ability_by_random())
        print(spacer)
        print('Arcane Power!')
        time.sleep(2)
        print(spacer)
        predator_picked = enemies.choose_predator()
        enemies.check_predator(predator_picked)

if __name__ == '__main__':
    character()
    main()
