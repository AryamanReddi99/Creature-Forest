# Creature-Forest
Simulation of agents competing for resources with different strategies.

## Usage
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

![Image1](https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/variable_payoff.png?raw=true)

Where:  
**a**: score for Species A when facing Species A  
**b**: score for Species B when facing Species A  
**c**: score for Species A when facing Species B  
**d**: score for Species B when facing Species B  

These values can be defined in **payoff_dict** below to simulate the progression of population growth and resource control between Species A and Species B. The equilibrium point (if present) of the preceding plot should indicate the long-term population fraction of Species A.

```python
payoff_dict = {
    "a": 1,
    "b": 1.5,
    "c": 0.5,
    "d": 0
}
```

![Image1](https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/variable_plot.png?raw=true)

Note that increaing the ageing rate of the creatures reduces the predictability of the model.

## Theory

A variable payoff matrix allows us to visualise a generalised version of a famous game in Game Theory, the Prisoner's Dilemma. The classic problem outlines a scenario where defection by both parties results in a Nash Equilibirum - a stable state of the system whereby no agent can improve their score with a unilateral change of strategy. That payoff grid typically looks like this:

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/PD.png" width="300">

We can see how playing around with the payoff values may cause the decision flow between states to change, resulting in different equilibrium states; for example, another GT problem known as Doves and Hawks:

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/HD.png" width="300">

In this case the equilibrium state of the system is at 50% one strategy (playing Dove) and 50% the other strategy (playing Hawk), as the equilibrium point of the expectance plots predicts.

## Further Reading

Prisoner's Dilemma:  https://www.investopedia.com/terms/p/prisoners-dilemma.asp
Doves and Hawks:  https://www.youtube.com/watch?v=YNMkADpvO4w&ab_channel=Primer
