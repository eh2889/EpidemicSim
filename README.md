# EpidemicSim
Epidemic Simulator in Python

The purpose of this project is to simulate the outbreak of an infectious disease. This is a common problem in the field of epidemiology, which is the study of infectious diseases. While the simulation we will write is an extremely simplified version of actual models, it is based on some of the the same ideas. 

We will simulate the spread of the disease on a map of New York City. Our map is a 150x150 grid. You can think of each cell (or pixel) of this grid as representing a number of individuals that live in that area. In step 1 of the project, you will read in map data from a file and display the map. The map will look something like this: 

<img width="585" alt="map1" src="https://user-images.githubusercontent.com/55852181/118294287-90b1aa00-b4a8-11eb-8fe5-d104326b70d4.png">



Our model is based on the so-called SRI model. At any time step, each cell on the map can be in one of three states: 

S (susceptible): The cell is healthy and not infected. Displayed green on the map. 
R (resistant): The cell cannot be infected (in our case, that means the cell is dead). Displayed gray on the map. 
I (infected): The cell is currently infected. Displayed red on the map. 
When a cell is infected, it has the potential to infect neighboring cells, it might recover after a certain time (revert to state S), or it might die (move to state R).  Initially all cells will be susceptible and only one cell will be infected. The details about how and when these changes occur are described below. 

Time is measured in discrete steps. After a number of steps, the disease will have spread and infected a number of cells. Some may have recovered and others may have died. The map might look something like this: 
<img width="362" alt="map2" src="https://user-images.githubusercontent.com/55852181/118294292-91e2d700-b4a8-11eb-8c01-81c5ff6d2e06.png">
