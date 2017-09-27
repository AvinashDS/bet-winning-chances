'''
Question - This is a prediction of winning a bet.
Suppose you are going to climb up the Empire State Building.
You place a bet with your friends that you will climb up 60 steps.

Rules- 
You will be going to throw a dice for it 100 times.

For each 1 or 2 you will climb down 1 step.

For each 3, 4 or 5 you will climb up 1 step.

If you get 6 you will roll the dice again and climb up the resulting number.

You can't go lower than step 0.
If you fell down or slip, you will start from again.
Chances of slipping or falling down the steps are 0.1%

Calculate the chances of winning the bet.
'''

'''
Two Methods to solve 
1) Analytically
2) Simulate the Process 1000 of times and see what fractions of simulations you will reach 60 steps.

2) is called Hacker Statistics. Using it Now
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#We need a random number generator for the rolling of dice
#Using NumPy Rand Functions

np.random.seed(123)

#Results We Get From the Dice Roll 100 times
all_random_walks = []

#Simulation Count
sim_count = 500

for simulations in range(sim_count):

	#Containing all the steps
	random_walk = [0]

	for x in range(100):

		#Setting Steps
		step = random_walk[-1]

		#Roll the Dice
		dice = np.random.randint(1,7)

		#Throwing Rules - Determining Next Step

		if dice <=2:
			step = max(0, step -1) #So The Steps Never Go Down the Zero
		elif dice <=5:
			step = step + 1
		else:
			step = step + np.random.randint(1,7)

		# Chances of falling down are 0.1%
		if np.random.rand(0,1) <= 0.001:
			step =0


		random_walk.append(step)
	all_random_walks.append(random_walk)

np_arwt = np.transpose(np.array(all_random_walks))

ends = np_arwt[-1]

# plt.hist(ends, bins=20)
# plt.show()

chances  =np.mean(ends >= 60)

#The Estimated Chances Are
print("The Chances of Winning the Bet as predicted are " + str(chances* 100) + "%")
