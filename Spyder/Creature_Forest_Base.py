#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import matplotlib.pyplot as plt
# In[4]:


class Bird:
    """
    Base constructor class for birds
    """
    def __init__(self, food=0):
        self.food=food
    def interact(self,opponent):
        return None    #Birds need a specific class species to interact
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


# In[5]:


#Define specific creature classes

class Dove(Bird):
    """
    Non-confrontational, shares with opponent
    """
    def __init__(self, food=0):
        self.name = 'Dove'
        self.food = food
    def interact(self, opponent):
        if opponent is None:
            self.food = 2
        elif opponent.name == 'Dove':
            self.food = 1
        elif opponent.name == 'Hawk':
            self.food = 0.5
        elif opponent.name == 'Goose':
            self.food = 1
        elif opponent.name == 'Crow':
            self.food = 0.5

class Hawk(Bird):
    """
    Aggresive, fights for food
    """
    def __init__(self, food = 0):
        self.name = 'Hawk'
        self.food = food
    def interact(self, opponent):
        if opponent is None:
            self.food = 2
        elif opponent.name == 'Dove':
            self.food = 1.5
        elif opponent.name == 'Hawk':
            self.food = 0
        elif opponent.name == 'Goose':
            self.food = 0
        elif opponent.name == 'Crow':
            self.food = 1.5

class Goose(Bird):
    """
    Nice to doves, fights with aggressors.
    """
    def __init__(self, food=0):
        self.name = 'Goose'
        self.food = food
    def interact(self,opponent):
        if opponent is None:
            self.food = 2
        elif opponent.name == 'Dove':
            self.food = 1
        elif opponent.name == 'Hawk':
            self.food = 0
        elif opponent.name == 'Goose':
            self.food = 1
        elif opponent.name == 'Crow':
            self.food = 1

class Crow(Bird):
    """
    Puts up an aggresive display, reverts to dove if challenged
    """
    def __init__(self, food=0):
        self.name = 'Crow'
        self.food = food
    def interact(self, opponent):
        if opponent is None:
            self.food = 2
        elif opponent.name == 'Dove':
            self.food = 1.5
        elif opponent.name == 'Hawk':
            self.food = 0.5
        elif opponent.name == 'Goose':
            self.food = 1
        elif opponent.name == 'Crow':
            self.food = 1


# In[14]:


def run_generation(creature_list, carrying_capacity):
    #assign creatures to resource list
    resources_used = 0
    resources = [[] for _ in range(carrying_capacity//2)]
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
    creature_list_food_collected = []    #creature list after foraging
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
            creature_list_food_collected.append(creature_b)
        creature_a.interact(creature_b)
        creature_list_food_collected.append(creature_a)
        
    #determine survival & reproduction
    creature_list = []       #creatures at end of day
    for creature in creature_list_food_collected:
        if creature.survive() == False:
            #print(creature.name, 'died')
            next
        else:
            #print('creature survived')
            creature_list.append(creature)
            if creature.reproduce() == True:
                #print(creature.name, 'reproduced')
                creature_type = type(creature)
                creature_list.append(creature_type())
    for creature in creature_list:
        creature.food = 0      #new day
    random.shuffle(creature_list) 
    return(creature_list)


# In[30]:


#Define agents for customisable payoff matrix

class A:
    """
    Base class for species A
    """
    def __init__(self,age=0,points=0,largest_payoff=0):
        self.name = "A"
        self.age = age
        self.points = points
        self.largest_payoff = largest_payoff
    def interact(self, opponent, payoff_dict):
        self.largest_payoff = max(payoff_dict.values())
        if opponent is None:
            self.points = self.largest_payoff
        elif opponent.name == 'A':
            self.points = payoff_dict.get("a")
        elif opponent.name == 'B':
            self.points = payoff_dict.get("c")
    def dont_starve(self):
        death_chance = random.uniform(0,self.largest_payoff/2)
        if self.points < death_chance:
            return False #death
        else:
            return True  #survival
    def reproduce(self):
        non_reproduction_chance = random.uniform(0,self.largest_payoff/2)
        if (self.points-(self.largest_payoff/2)) < non_reproduction_chance:
            return False
        else:
            return True
    def mortality(self):
        death_chance = random.uniform(0,10)
        if self.age > death_chance:
            return False    #death
        else:
            return True     #survive

class B:
    """
    Base class for species A
    """
    def __init__(self,age=0,points=0,largest_payoff=0):
        self.name = "B"
        self.age = age
        self.points = points
        self.largest_payoff = largest_payoff
    def interact(self, opponent, payoff_dict):
        self.largest_payoff = max(payoff_dict.values())
        if opponent is None:
            self.points = self.largest_payoff
        elif opponent.name == 'A':
            self.points = payoff_dict.get("b")
        elif opponent.name == 'B':
            self.points = payoff_dict.get("d")
    def dont_starve(self):
        death_chance = random.uniform(0,self.largest_payoff/2)
        if self.points < death_chance:
            return False #death
        else:
            return True  #survival
    def reproduce(self):
        non_reproduction_chance = random.uniform(0,self.largest_payoff/2)
        if (self.points-(self.largest_payoff/2)) < non_reproduction_chance:
            return False
        else:
            return True
    def mortality(self):
        death_chance = random.uniform(0,10)
        if self.age > death_chance:
            return False      #death
        else:
            return True       #survive


# In[39]:


def run__generalised_generation(creature_list, carrying_capacity, payoff_dict, ageing_rate):
    #assign creatures to resource list
    resources_used = 0
    resources = [[] for _ in range(carrying_capacity//2)]
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
    creature_list_points_collected = []    #creature list after foraging
    for resource in resources:
        num_creatures = len(resource)
        if num_creatures == 0:
            continue
        creature_a = resource[0]
        if num_creatures == 1:
            creature_b = None  
        else: 
            creature_b = resource[1]
            creature_b.interact(creature_a, payoff_dict)
            creature_list_points_collected.append(creature_b)
        creature_a.interact(creature_b, payoff_dict)
        creature_list_points_collected.append(creature_a)
        
    #determine survival & reproduction
    creature_list = []       #creatures at end of day
    for creature in creature_list_points_collected:
        if creature.dont_starve() == False:
            next
        elif creature.mortality() == False:
            next
        else:
            #print('creature survived')
            creature_list.append(creature)
            if creature.reproduce() == True:
                #print(creature.name, 'reproduced')
                creature_type = type(creature)
                creature_list.append(creature_type())
    for creature in creature_list:
        creature.points = 0      # new day
        creature.age += ageing_rate    # age by one day
    random.shuffle(creature_list) 
    return(creature_list)

