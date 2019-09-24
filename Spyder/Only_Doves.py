#!/usr/bin/env python
# coding: utf-8

# In[46]:


#import import_ipynb
from Creature_Forest_Base import *
import seaborn as sns


# In[73]:


creature_list = []
for i in range(1):
    creature_list.append(Dove())

generation_count = [0]
population_count = [len(creature_list)]

num_generations = 20

for i in range(1,num_generations):
    creature_list = run_generation(creature_list, carrying_capacity=1000)
    population = len(creature_list)
    population_count.append(population)
    generation_count.append(i)

print(generation_count)
print(population_count)

pal = sns.color_palette("Set2")
plt.stackplot(generation_count, population_count, labels = ['Doves'], colors = pal, alpha=0.5)
plt.grid()
plt.legend(loc = 'upper left')
plt.show()

