# Creature-Forest
Simulation of agents competing for resources with different strategies.


These scripts can be run within any Python IDE, with the exception of ***Variable_Payoff_Simulator.ipynb***, which requires a Jupyter notebook due to ipywidgets.

**Modules Required:**

random
matplotlib.pyplot  
import_ipnyb (if using notebook)  

**Example Plot**

![Image1](https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/doves_hawks_geese.png)

All scripts part from ***Creature_Forest_Base*** and ***Variable_Payoff_Simulator.ipynb*** simulate the progression of a particular scenario. 

Each script offers full control of:  
* Starting population
* Environmental carrying capacity
* Number of generations
* Invading species
* Creature ageing rate

***Variable_Payoff_Simulator.ipynb*** can be used to visualise the relative expectance of two competing species as a function of population fraction:

![Image1](https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Annotation%202019-09-25%20181249.png){:height="50%" width="50%"}

Where:  
**a**: score for Species A when facing Species A  
**b**: score for Species B when facing Species A  
**c**: score for Species A when facing Species B  
**d**: score for Species B when facing Species B  

These values can be defined in **payoff_dict** below to simulate the progression of population growth and resource control between Species A and Species B. The equilibrium point (if present) of the preceding plot should indicate the long-term population fraction of Species A.

![Image1](https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/variable_plot.png?raw=true)

Note that increaing the ageing rate of the creatures reduces the predictability of the model.


