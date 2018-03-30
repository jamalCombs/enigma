import random
import time

class Enemies(object):
        """Enemies content -- statistics and attacks"""

        def __init__(self):

            return None

        # selects enemy damage at random, with min and max
        def predators(self):
            bat = random.randint(0, 300.0)
            hawk = random.randint(0, 500.0)

            return bat, hawk

        # selects an enemy at random and returns a string of attack and damage
        def ability_by_random(self):
            predator = self.predators()
            rand_enemey_attack = random.choice(predator)

            if rand_enemey_attack == predator[0]:
                    print('Bat: Vampiric Strike Damage >>> {0}').format(rand_enemey_attack)

            elif rand_enemey_attack == predator[1]:
                    print('Hawk-eagle: Beastlaw Damage >>> {0}').format(rand_enemey_attack)

            else:
                    print('Enemy did not attack.')

        # receives raw input to choose predator
        def choose_predator(self):
            the_predator = ''
            while the_predator != '1' and the_predator != '2':
                    print('Which predator will you attack? (1 or 2)')
                    the_predator = raw_input()

            return the_predator

        # inspects predator attack and damage
        def check_predator(self, predator):
            chosen_predator = predator
            chosen_predator = self.ability_by_random()

            return chosen_predator

print "Enemies module compiled with no errors!"
