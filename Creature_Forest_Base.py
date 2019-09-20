#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt

class Dove:
    def __init__(self,food = 0):
        self.name = 'Dove'
        self.food = food
    
    def interact(self, opponent):
        if opponent is None:
            self.food = 2
        elif opponent.name == 'Dove':
            self.food = 1
        elif opponent.name == 'Hawk':
            self.food = 0.5
    def survive(self):
        death_chance = random.random()
        if self.food < death_chance:
            return False #death
        else:
            return True  #survival
    def reproduce(self):
        non_reproduction_chance = random.random()
        if (self.food - 1) < non_reproduction_chance:
            return False
        else:
            return True


# In[2]:


def run_generation(creature_list, carrying_capacity):
    #assign creatures to resource list
    resources_used = 0
    resources = [[] for _ in range(carrying_capacity)]
    for creature in creature_list:
        while resources_used < carrying_capacity:
            resource_index = random.randint(0,(carrying_capacity/2)-1)
            resource = resources[resource_index]
            if len(resource) < 2:
                resources[resource_index].append(creature)
                resources_used+=1
                break
            else:
                next
    #allow creatures to interact
    #repopulate creature_list
    creature_list = []
    for resource in resources:
        num_creatures = len(resource)
        if num_creatures == 0:
            continue
        creature_a = resource[0]
        if num_creatures == 1:
            creature_b = None  
        else: 
            creature_b = resource[1]
            creature_b.interact(creature_a)
            creature_list.append(creature_b)
        creature_a.interact(creature_b)
        creature_list.append(creature_a)
        
    #determine survival & reproduction
    for i in range(len(creature_list)):
        creature = creature_list[i]
        if creature.survive() == False:
            #print(creature.name, 'died')
            creature_list.remove(creature)
        else:
            #print('creature survived')
            if creature.reproduce() == True:
                #print(creature.name, 'reproduced')
                creature_type = type(creature)
                creature_list.append(creature_type())
            creature.food = 0
    random.shuffle(creature_list) 
    return(creature_list)
    

