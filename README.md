# Creature-Forest
Simulation of agents competing for resources with different strategies.

## Usage
These scripts can be run within any Python IDE, with the exception of ***Variable_Payoff_Simulator.ipynb***, which requires a Jupyter notebook due to ipywidgets.

**Modules Required:**

random  
matplotlib.pyplot  
import_ipnyb (if using notebooks)  

Example Plot from ***Doves_Hawks_Coexistence.ipynb***

![Image1](https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/doves_hawks_geese.png)

Example Plot from ***Goose_Infiltration_Of_Hawks.ipynb***

![Image1](https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/download.png?raw=true)

Each script, apart from ***Creature_Forest_Base.ipynb*** and ***Variable_Payoff_Simulator.ipynb***, simulate the progression of a particular scenario. 

New agents are simple to add by extending the base class in ***Creature_Forest_Base.ipynb***. Each agent has a lifespan of 10.

Each script offers control over:  
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

See **Theory** for a visual  representation of how this affects decision flow.

Payoff values can be defined in **payoff_dict** below to simulate population growth and resource control between Species A and Species B. The equilibrium point (if present) of the preceding plot should indicate the long-term population fraction of Species A.

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

Consider Game Theory's most widely used game: the Prisoners Dilemma. The problem outlines a scenario where defection by both parties is a Nash Equilibirum - a stable state of the system whereby no agent can improve their score with a unilateral change of strategy. That payoff grid typically looks like this:

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/PD.png" width="300">

We can see how playing around with the payoff values may cause the decision flow between states to change, resulting in different equilibrium states; for example, in another GT problem known as Doves and Hawks:

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/HD.png" width="300">

In this case two arrows flip, so the equilibrium state of the system is when 50% of agents employ one strategy (playing Dove) and 50% the other (playing Hawk), as the equilibrium point of the expectance plot predicts.

A generalised payoff matrix can have one or several equilibria (which may or may not be true Nash Equilibria) depending on the interaction scores **(a, b, c ,d)** between strategies.

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/generalised.png" width="300">

## Further Reading

Prisoner's Dilemma:  https://www.investopedia.com/terms/p/prisoners-dilemma.asp  
Doves and Hawks:  https://www.youtube.com/watch?v=YNMkADpvO4w&ab_channel=Primer
