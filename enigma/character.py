import random
import time

class Character():
        """ Character content -- appearance, attributes, and statistics

        Args:
            arg1 (str): Character's name
            arg2 (str): Character's age
            arg3 (str): Character's sex
            arg4 (str): Character's race
            arg5 (str): Character's role
            arg6 (str): Character's cult

        Returns:
            str: tuple of name, age, sex, race, role, cult
         """
        def __init__(self, name, age, sex, race, role, cult):
            self.name = name
            self.age = age
            self.sex = sex
            self.race = race
            self.role = role
            self.cult = cult

        # returns a string of character introduction
        def intro(self, description, name):
            character_name = name

            return character_name.title(), description.title()

        # returns a string of character armor set
        def armor(self, color, category):

            return color, category

        # returns maximum energy of character, which is vigor minus efficiency
        def vigor(self):
            vigor_amount = 500.0
            efficiency = self.vigor_efficiency()

            dive_vigor_cost = vigor_amount - efficiency[0]
            tornado_vigor_cost = vigor_amount - efficiency[1]

            return  dive_vigor_cost, tornado_vigor_cost

        # returns maximum of health of character
        def vitality(self):
            vitality = 1025

            return vitality

        # defines mana cost
        def vigor_efficiency(self):
            base = 0
            min_vigor_cost = 15.0
            max_vigor_cost = 30.0

            return   min_vigor_cost, max_vigor_cost

        # defines character abilities, and returns a list
        def abilities(self, ability_names = ['Dive Bomb', 'Tornado']):

            return ability_names

        # selects random damage output of abilities, with min and max
        def ability_damage(self):
            dive_damage = random.randint(0, 250)
            tornado_damage = random.randint(0, 500)

            return dive_damage, tornado_damage

        # creates a string graphic of dive ability
        def dive(self):
                dive = ['''
                 \        /
                \ \      / /
                 \        /
                  \      /
                   \    /
                    \  /  ''']

                for strings in dive:
                        print(strings)

        # creates a string graphic of tornado ability
        def torn(self):
                tornado = ['''
                (  (   )  )
                 (       )
                  (     )
                   (   )
                    ( )  ''' ]

                for strings in tornado:
                    print(strings)

        # displays character statistics to screen
        def character_stats(self):
            print_stats = self.random_ability()

            return print_stats

        # checks if character hits target
        def miss_target_check(self):
            target = random.randint(0, 1)
            if target == 0:
                return 'MISSED'
            else:
                return target

        # selects ability and returns damage at random
        def select_ability_by_random(self):
                ability = self.abilities()
                ability_choice = str(random.choice(ability))
                damage = self.ability_damage()
                vigor_efficiency = self.vigor_efficiency()
                total_vigor = self.vigor()

                print('ABILITY: ' + ability_choice)

                if ability_choice == 'Tornado':
                        print(self.torn())
                        print('damage >>> ' + str(damage[1]) + '\n' + '\nmana cost >>> - ' + str(vigor_efficiency[1]) + '%' + '\n' + 'vigor >>> ' + str(total_vigor[1]))

                elif ability_choice == 'Dive Bomb':
                        print(self.dive())
                        print('damage >>> ' + str(damage[0]) + '\n' + '\nmana cost >>> - ' + str(vigor_efficiency[0]) + '%' + '\n' + 'vigor >>> ' + str(total_vigor[0]))

                else:
                        print('ABILITY NOT SELECTED')

print "Character module compiled with no errors!"
