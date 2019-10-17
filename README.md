# Creature-Forest
Strategy interaction in a virtual biological ecosystem.

## Purpose
This repository aims to observe the interaction and long-term success of various strategies by allowing them to compete in a virtual ecosystem. Agent obtain points by foraging in the environment, and can use these points to survive and propagate their strategy. We can use Game Theory to predict the long-term success of these iterated interactions.  

Considering animals in a closed ecosystem competing for common resources is a useful analogue for visualising these simulations. However, the analysis of evolving strategies has countless applications in finance, politics, sociology, and more.

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Multiple/download%20(4).png?raw=true" width="1000" height="400">   


***Multiple strategies***


## Usage
These scripts are best run in Jupyter notebooks, but will also work in any normal Python IDE, with the exception of **Variable_Payoff.ipynb**

**Modules Required:**

random  
numpy  
pandas  
copy  
matplotlib.pyplot  
import_ipnyb (if using notebooks)  

## Hard-coded strategies

**Creature_Forest_Base.ipynb** currently defines 4 hard-coded strategies:

1. Dove
   * Shares resources with others
2. Hawk
   * Is aggresive, steals resources from others
   * Fights to the death when meeting other hawks
3. Goose
   * Shares with doves
   * Fights to the death with hawks
4. Crow
   * Steals from doves
   * Backs down when confronted by hawks & geese

New agents can be added by extending the base class in **Creature_Forest_Base.ipynb**. Each agent has a lifespan of 10 cycles. The function `run_simulation()` runs the generations and outputs a dataframe of agent populations. Hostile interactions result in death as all energy obtained is used up during the altercation. Increasing the ageing rate decreases the predictability of the model. 

`run_simulation()` offers the following parameters as arguments:  
* Starting population
* Environmental carrying capacity
* Number of generations
* Invading species
* Variable payoff scores
* Creature ageing rates
* Gene mutation rates

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Single/download.png?raw=true" width="420" height="250"><img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Single/download%20(2).png?raw=true" width="420" height="250">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Single/download%20(1).png?raw=true" width="420" height="250">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Single/download%20(3).png?raw=true" width="420" height="250">
</p>  

***Isolated strategies***  
From top left: Doves, Geese, Hawks, Crows. The horizontal lines indicate the average population over the simulation runtime. When left alone, each species reach an equilibrium with the environment. Hawks have a rather unstable equilibrium due to the fact that they kill each other on sight.

What happens when we let them interact?  

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Dual/download%20(4).png?raw=true" width="800" height="400">
</p>   

***Doves vs Hawks***  
Letting doves and hawks interact results in an equilibrium. This is because each strategy's average score from each interaction happens to be equal at a population fraction of 0.5, or 50% doves. When the fraction of doves rises above 50%, the hawks are able to score more points and increase their population. When the fraction drops below 50%, the opposite occurs. Thus, the stable equilibrium of these strategies is equal dominance.


<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Dual/download%20(1).png?raw=true" width="800" height="400">
</p>  

***Doves vs Crows***  
Doves and crows have a different payoff matrix: when facing a dove, its better to be a crow because extra points can be stolen. When facing a crow, its still better to be a crow because crows don't betray other crows. Thus, playing crow is a **strictly dominant strategy** as it is a better choice no matter what strategy the opposition plays. This is a situation known as the **Prisoner's Dilemma**.

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Dual/download%20(3).png?raw=true" width="800" height="400">
</p>  

***Geese vs Hawks***  
When facing a goose, a player's best strategy is to also play goose, or they die. When facing a hawk, there is no dominant strategy. This means that althought the results are similar to ***Doves vs Crows***, playing goose is not a **strictly dominant strategy**.



We can also allow for infiltration of invading strategies to see how they disrupt existing populations.

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Infiltration/download.png?raw=true" width="420" height="250"><img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Infiltration/download%20(1).png?raw=true" width="420" height="250">
</p>  

***Invading doves and hawks***  
Introduction of hawks to stable dove populations, or vice-versa, eventually results in a similar equilbrium as before given that the invading agents do not starve to death due to limited resources before gaining a foothold.

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Infiltration/download%20(9).png?raw=true" width="800" height="400">
</p>  

***Invading crows***  
Crows are able to hijack a stable Hawk/Dove equilibrium by exploiting the doves until they are eliminated. They then reach a similar equilibrium with the hawks by playing Dove henceforth.



## Variable payoffs

Each of the above interaction scenarios has a hard-coded payoff matrix. Changing this matrix results in a different equilibrium between strategies, which we can predict.***Variable_Payoff_Simulator.ipynb*** can be used to visualise the relative expectance of two competing strategies as a function of population fraction:

![Image1](https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/variable_payoff.png?raw=true)

Where:  
**a**: score for Species A when facing Species A  
**b**: score for Species B when facing Species A  
**c**: score for Species A when facing Species B  
**d**: score for Species B when facing Species B  

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/generalised.png" width="300">

Payoff values can be defined in **payoff_dict** below to simulate population growth and resource control between Species A and Species B. The equilibrium point (if present) of the preceding plot should indicate the long-term population fraction of Species A.

```python
payoff_dict = {
    "a": 1,
    "b": 1.5,
    "c": 0.5,
    "d": 0
}
```
<p align="center">
<img src= "https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Variable/download.png?raw=true" width = "800" height="400">
</p>  

***Payoff scores identical to Hawks vs Doves***  




Consider the Prisoner's Dilemma once more. The problem outlines a scenario where defection by both parties is a **Nash Equilibirum** - a stable state of the system whereby no agent can improve their score with a unilateral change of strategy. That payoff grid typically looks like this:

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/PD.png" width="300">

We can see how playing around with the payoff values may cause the decision flow between states to change, resulting in different equilibrium states; for example, Doves and Hawks:

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/HD.png" width="300">

In this case two arrows flip, so the equilibrium state of the system is when 50% of agents employ one strategy (playing Dove) and 50% the other (playing Hawk), as the expectance plot above predicts.

A payoff matrix can have one or several equilibria (which may or may not be true Nash Equilibria) depending on the interaction scores **(a, b, c ,d)** between strategies.  

**Example 1**  
What if, instead of fighting to the death, hawks left encounters wounded but with a 25% chance of survival? 

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/modified-hawks-expectance.png" width="300">

Our expectance plot predicts equilibrium at about one-third doves. We can insert our payoff values into **payoff_dict** and observe the simulation:

```python
payoff_dict = {
    "a": 1,
    "b": 1.5,
    "c": 0.5,
    "d": 0.25
}
```
<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Variable/download%20(1).png?raw=true" width="800" height = "400">
</p>

***Modified payoff***  
As predicted, stable equilibrium is reached at 33% doves.

## Further Reading

Prisoner's Dilemma:  https://www.investopedia.com/terms/p/prisoners-dilemma.asp  
Doves and Hawks:  https://www.youtube.com/watch?v=YNMkADpvO4w&ab_channel=Primer
