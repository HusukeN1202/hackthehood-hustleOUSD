# Lab 6 - Husuke Nishioka

# hero.py

import random
from ability import Ability
from armor import  armor

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer

      current_health: Integer
    '''

    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.armors = []
    self.abilities = []
    
  def battle(self, opponent):
   self.opponent  = opponent
   print(f"{self.name} battles {opponent}!")
   winner  = random.choice([self, opponent])
   print(f"{winner} wins the battle!")
    
  def add_ability(self, Ability):
   self.abilities.append(Ability)
   print(f"{Ability} has been added.")
    
  def sum_of_attacks(self):
   total_damage = 0
   for ability in self.abilities:
      total_damage += Ability.attack()
   return total_damage                
    
  def add_armor (self, armor):
   self.armors.append(armor)
   print(f"{armor} has been added.")

  def sum_of_blocks(self):
   total_block = 0
   for armor in  self.abilities:
      total_block += armor.block()
   return total_block



       

   
       
       

'''if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    my_hero1  = Hero("Iron Man", 2000000)
    print(my_hero1.name)
    print(my_hero1.current_health)
    
    ability1 = Ability("Explosion", 300)
    ability2 = Ability("Stabbing", 150)
    ability3 = Ability("Web shooter", 50)
    ability4 = Ability("Punch", 20)
   
    add_ability(my_hero1, ability3)
    add_ability(my_hero1, ability4)
    add_ability(my_hero, ability1)
    add_ability(my_hero, ability2)'''

    


  

