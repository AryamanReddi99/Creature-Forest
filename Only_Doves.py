#!/usr/bin/env python
# coding: utf-8

# In[5]:


import import_ipynb
import Creature_Forest_Base


# In[13]:


creature_list = []
for i in range(25):
    creature_list.append(Dove())

generation_count = []
population_count = []
for i in range(10):
    creature_list = run_generation(creature_list, 1000)
    population = len(creature_list)
    population_count.append(population)
    generation_count.append(i)

print(generation_count)
print(population_count)

plt.stackplot(generation_count, population_count, labels = ['Doves'])
plt.legend(loc = 'upper left')
plt.show()

