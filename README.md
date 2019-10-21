# Creature-Forest
Game Theory and strategy evolution in a virtual biological ecosystem.

## Purpose
This repository aims to observe the interaction and long-term success of various strategies by allowing them to compete in a virtual ecosystem. Agents obtain points by foraging in the environment, and can use these points to survive and propagate their strategy. We can use Game Theory to predict the long-term success of these iterated interactions.  

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Multiple/download%20(4).png?raw=true" width="1000" height="400">  
<p align="center">
Fig 1. Multiple strategies
</p>


## Usage
These scripts are best run in Jupyter notebooks, but will also work in any normal Python IDE, with the exception of **Variable_Payoff.ipynb**

**Modules Required:**  
random  
numpy  
sympy  
pandas   
matplotlib.pyplot  
import_ipnyb (if using notebooks)  

New agents can be added by extending the base class in **Creature_Forest_Base.ipynb**. Each agent has a lifespan of 1, which allows it to survive for 10 cycles by default. The function `run_simulation()` runs the interactions and outputs a dataframe of agent populations. Increasing the ageing rate decreases the predictability of the model.  

`run_simulation()` offers the following parameters as arguments:  
* Starting population
* Environmental carrying capacity
* Number of generations
* Invading species
* Variable payoff scores
* Creature ageing rates
* Gene mutation rates
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

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Single/download.png?raw=true" width="420" height="250"><img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Single/download%20(2).png?raw=true" width="420" height="250">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Single/download%20(1).png?raw=true" width="420" height="250">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Single/download%20(3).png?raw=true" width="420" height="250">
</p>  
<p align="center">
Fig 2. Isolated strategies
</p>
  
From top left: Doves, Geese, Hawks, Crows. The horizontal lines indicate the average population over the simulation runtime. When left alone, each species reach an equilibrium with the environment. Hawks have a rather unstable equilibrium due to the fact that they kill each other on sight.

What happens when we let them interact?  

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Dual/download%20(4).png?raw=true" width="800" height="400">
</p>   
<p align="center">
Fig 3. Doves vs Hawks
</p>  
Dove and Hawk interactions result in a strategy equilibrium as each strategy's average interaction score happens to be equal at a population fraction of 0.5, or 50% doves. When the fraction of doves rises above 50%, the hawks are able to score more points and increase their population. When the fraction drops below 50%, the opposite occurs. Thus, the stable equilibrium of these strategies is equal dominance.


<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Dual/download%20(1).png?raw=true" width="800" height="400">  
</p>
<p align="center">
Fig 4. Doves vs Crows
</p>  

Doves and crows have a different payoff matrix: when facing a dove, its better to be a crow because extra points can be stolen. When facing a crow, its still better to be a crow because crows don't betray other crows. Thus, playing crow is known as a **strictly dominant strategy** as it is a better choice no matter what strategy the opposition plays. This is a situation known as the **Prisoner's Dilemma**.

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Dual/download%20(3).png?raw=true" width="800" height="400">
</p>  
<p align="center">
Fig 5. Geese vs Hawks
</p> 
When facing a goose, a player's best strategy is to also play goose, or they die. When facing a hawk, there is no dominant strategy. This means that althought the results are similar to Fig 4, playing goose is not a strictly dominant strategy.   

We can also allow for infiltration of invading strategies to see how they disrupt existing populations.

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Infiltration/download.png?raw=true" width="420" height="250"><img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Infiltration/download%20(1).png?raw=true" width="420" height="250">
</p>  
<p align="center">
Fig 6. Invading doves and hawks
</p>  
Introduction of hawks to stable dove populations, or vice-versa, eventually results in a similar equilbrium as before given that the invading agents do not immediately starve to death due to limited resources.

<p align="center">
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Infiltration/download%20(9).png?raw=true" width="800" height="400">
</p>  
<p align="center">
Fig 7. Invading crows
</p>
Crows are able to hijack a stable Hawk/Dove equilibrium by exploiting the doves until they are eliminated. They then reach a similar equilibrium with the hawks by playing the Dove strategy henceforth.



## Variable payoffs

Each of the above interaction scenarios has a hard-coded payoff matrix. Changing this matrix results in a different equilibrium between strategies, which we can predict. ***Variable_Payoff_Simulator.ipynb*** can be used to visualise the relative expectance of two competing strategies as a function of population fraction:

![Image1](https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/variable_payoff.png?raw=true)

Where:  
**a**: score for Strategy A when facing Strategy A  
**b**: score for Strategy B when facing Strategy A  
**c**: score for Strategy A when facing Strategy B  
**d**: score for Strategy B when facing Strategy B  

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/generalised.png" width="300">

Payoff values can be defined in **payoff_dict** to simulate population growth and resource control between Strategy A and Strategy B. The equilibrium point (if present) of the preceding plot should indicate the long-term population fraction of Species A.

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
<p align="center">
Fig 8. Payoffs identical to Doves/Hawks
</p>
Consider the Prisoner's Dilemma once more. The problem outlines a scenario where defection by both parties is a Nash Equilibrium -  a stable state where no agent can improve their score with a unilateral change of strategy. That payoff grid typically looks like this:

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/PD.png" width="300">

We can see how playing around with the payoff values may cause the decision flow between states to change, resulting in different equilibrium states; for example, Doves and Hawks:

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/HD.png" width="300">

In this case two arrows flip, so the equilibrium state of the system is when 50% of agents employ one strategy (playing Dove) and 50% the other (playing Hawk), as the expectance plot above predicts.

A payoff matrix can have one or several equilibria (which may or may not be true Nash Equilibria) depending on the interaction scores **(a, b, c ,d)** between strategies.  

**Example**  
What if, instead of fighting to the death, hawks left encounters with each other wounded but with a 25% chance of survival? 

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/modified-hawks-expectance.png" width="300">

Our expectance plot predicts equilibrium at about one-third Strategy A (Doves). We can insert our payoff values into **payoff_dict** and observe the simulation:

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
<p align="center">
Fig 9. Modified payoff
</p>

As predicted, stable equilibrium is reached at 33% doves.

## Strategy Evolution
What if we gave our agents the ability to modify their strategy over time? We will define a payoff matrix and give agents a chance to play either strategy A or B. The class attribute `gene_B` determines an agent's chance of playing strategy B and can mutate every time an agent replicates.

We can define `mutation_rate` and `gene_step` in `simulation_results()`:  

```python
starting_population = {
    "Mutant_0":[1]
}
simulation_results = run_simulation(starting_population=starting_population,gene_step=0.5,mutation_rate=0.1)                      
```                                   
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Mutants/download%20(1).png?raw=true" width="800" height = "400">
<p align="center">
Fig 10. Three strains
</p>

Each strain of mutant is named after the value of its strategy gene. For this simulation and the 2 following it, we will stick to using the Doves/Hawks payoff matrix. This means that an agent named "Mutant_0" has a 0% chance of playing Hawk, one named "Mutant_0.5" has a 50% chance of playing Hawk, and so on. We can make this distribution more continuous:

```python
simulation_results = run_simulation(starting_population=starting_population,gene_step=0.2,mutation_rate=0.1)  
```

<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Mutants/download%20(2).png?raw=true" width="800" height = "400">
<p align="center">
Fig 11. Six strains
</p>
One step further:

```python
simulation_results = run_simulation(starting_population=starting_population,gene_step=0.1,mutation_rate=0.1) 
```
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Mutants/download%20(3).png?raw=true" width="800" height = "400">
<p align="center">
Fig 12. Eleven strains
</p>

**How can we explain these results?**

Just like before, we can find the expected payoff of each interaction as a function of every strain's population fraction. We can solve the following system of equations, where [E] is a vector containing the average payoff of each strain's interactions, and [x] is a vector containing each strain's population fraction:  
 
[E] = [A][x]

In the case of 6 strains, we can use **Matrix_Solver.ipynb** to obtain the 6x6 matrix [A]: 

A =   
[5.   4.2  3.4  2.6  1.8  1.  ]  
     [4.6  3.84 3.08 2.32 1.56 0.8 ]  
     [4.2  3.48 2.76 2.04 1.32 0.6 ]  
     [3.8  3.12 2.44 1.76 1.08 0.4 ]  
     [3.4  2.76 2.12 1.48 0.84 0.2 ]  
     [3.   2.4  1.8  1.2  0.6  0.  ]
  
At equilibrium, the expectances are equal. Trying to solve this system reveals that the matrix [A] is singular (implying a loss of dimensionality), and the result that:  

x_0.0 = x_1.0  
x_0.2 = x_0.8  
x_0.4 = x_0.6  

As it turns out, we can prove that the expectance matrix will always be singular:  

1) The determinant of any nxn matrix can be reduced to a number of 3x3 matrix determinants  
2) Any 3x3 expectance matrix formed with our linearly spaced gene pattern is singular:

```python
import sympy as sp
a,b,c,d = sp.symbols('a b c d')
matrix_dict = {}
for i in range(1,4):
    for j in range(1,4):
        ki = sp.symbols('k{}'.format(i))
        kj = sp.symbols('k{}'.format(j))
        matrix_term = 'A{}{}'.format(i,j)
        expectance = (1-ki)*(1-kj)*a + (1-ki)*(kj)*c + (ki)*(kj)*d + (ki)*(1-kj)*b
        matrix_dict[matrix_term] = expectance
        
# where  ki and kj are the genes of the object and subject strains, respectively
  
det = matrix_dict.get("A11")*(matrix_dict.get("A22")*matrix_dict.get("A33")-matrix_dict.get("A32")*matrix_dict.get("A23")) - 
matrix_dict.get("A12")*(matrix_dict.get("A21")*matrix_dict.get("A33") - matrix_dict.get("A31")*matrix_dict.get("A23")) +  
matrix_dict.get("A13")*(matrix_dict.get("A21")*matrix_dict.get("A32")-matrix_dict.get("A31")*matrix_dict.get("A22"))

sp.expand(det) = ((a*(-k2 + 1)**2 + b*k2*(-k2 + 1) + c*k2*(-k2 + 1) + d*k2**2)*(a*(-k3 + 1)**2 + b*k3*(-k3 + 1) + 
c*k3*(-k3 + 1) + d*k3**2) - (a*(-k2 + 1)*(-k3 + 1) + b*k2*(-k3 + 1) + c*k3*(-k2 + 1) + d*k2*k3)*(a*(-k2 + 1)*(-k3 + 1) + 
b*k3*(-k2 + 1) + c*k2*(-k3 + 1) + d*k2*k3))*(a*(-k1 + 1)**2 + b*k1*(-k1 + 1) + c*k1*(-k1 + 1) + d*k1**2) + (-(a*(-k2 + 1)**2 + 
b*k2*(-k2 + 1) + c*k2*(-k2 + 1) + d*k2**2)*(a*(-k1 + 1)*(-k3 + 1) + b*k3*(-k1 + 1) + c*k1*(-k3 + 1) + d*k1*k3) + 
(a*(-k1 + 1)*(-k2 + 1) + b*k2*(-k1 + 1) + c*k1*(-k2 + 1) + d*k1*k2)*(a*(-k2 + 1)*(-k3 + 1) + b*k3*(-k2 + 1) + 
c*k2*(-k3 + 1) + d*k2*k3))*(a*(-k1 + 1)*(-k3 + 1) + b*k1*(-k3 + 1) + c*k3*(-k1 + 1) + d*k1*k3) - ((a*(-k3 + 1)**2 + 
b*k3*(-k3 + 1) + c*k3*(-k3 + 1) + d*k3**2)*(a*(-k1 + 1)*(-k2 + 1) + b*k2*(-k1 + 1) + c*k1*(-k2 + 1) + d*k1*k2) - 
(a*(-k1 + 1)*(-k3 + 1) + b*k3*(-k1 + 1) + c*k1*(-k3 + 1) + d*k1*k3)*(a*(-k2 + 1)*(-k3 + 1) + b*k2*(-k3 + 1) + 
c*k3*(-k2 + 1) + d*k2*k3))*(a*(-k1 + 1)*(-k2 + 1) + b*k1*(-k2 + 1) + c*k2*(-k1 + 1) + d*k1*k2)
= 0
```
This seems to imply that all multi-strain mutants will exhibit a strategy equilibrium similar to their hard-coded counterparts. Running this simulation with the payoff matrix from the prisoner's dilemma seems to confirm this:


```python
payoff_dict = {
    "a": 3,
    "b": 5,
    "c": 0,
    "d": 1
}
simulation_results = run_simulation(starting_population=starting_population,gene_step=0.1,mutation_rate=0.01) 
```
<img src="https://github.com/AryamanReddi99/Creature-Forest/blob/master/Images/Mutants/download.png?raw=true" width="800" height = "400">
<p align="center">
Fig 13. Prisoner's Dilemma, naturally selected
</p>
In this case each new strain of mutant eliminates the previous, as it has a higher chance of playing the strictly dominant strategy. Note that the total population decreases as the agents become more likely to defect, as the aggregate score for defection is lower than that for cooperation. Note also the strain Mutant_0.9 which persists at equilibrium, probably due to mutations in the population of Mutant_1.0.


## Further Reading

GT and biology: https://www.nature.com/scitable/knowledge/library/game-theory-evolutionary-stable-strategies-and-the-25953132/  
Prisoner's Dilemma:  https://www.investopedia.com/terms/p/prisoners-dilemma.asp  
Doves and Hawks:  https://www.youtube.com/watch?v=YNMkADpvO4w&ab_channel=Primer
