#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import import_ipynb
from Creature_Forest_Base import *
import seaborn as sns


# In[101]:


"""
Geese have a chance of infiltrating a hawk population if they reach a critical size
"""



creature_list = []
for i in range(1):
    creature_list.append(Hawk())

generation_count = [0]
dove_population  = []
hawk_population  = []
goose_population = []
population_quotient = []
dove_population.append(sum(creature.name == 'Dove' for creature in creature_list))
hawk_population.append(sum(creature.name == 'Hawk' for creature in creature_list))
goose_population.append(sum(creature.name == 'Goose' for creature in creature_list))

num_generations = 100

for i in range(1,num_generations):
    if i == 15:
        creature_list.extend([Goose() for j in range(10)])
    geese_per_gen = 0
    dove_per_gen = 0
    hawk_per_gen = 0
    creature_list = run_generation(creature_list, carrying_capacity=1000)
    for creature in creature_list:
        if creature.name == 'Dove':
            dove_per_gen += 1
        elif creature.name == 'Hawk':
            hawk_per_gen += 1
        elif creature.name == 'Goose':
            geese_per_gen += 1
    dove_population.append(dove_per_gen)
    hawk_population.append(hawk_per_gen)
    goose_population.append(geese_per_gen)
    if hawk_population[i] != 0:
        population_quotient.append(round(dove_population[i]/hawk_population[i],2))
    generation_count.append(i)

#print(generation_count)
#print(dove_population)
#print(hawk_population)
#print(population_quotient)

print(hawk_population)
print(goose_population)

pal = sns.color_palette("twilight")
plt.stackplot(generation_count,goose_population,hawk_population, labels = ['Geese', 'Hawks'], colors = pal, alpha=1)
plt.grid()
plt.legend(loc = 'upper left')
plt.show()

