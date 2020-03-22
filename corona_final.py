# Code to analyze countries on quality of Corona Virus containment with various country characteristics
# Authors: Shikhar Suryavansh (shh.suryavansh11@gmail.com) and Saurabh Bagchi (saurabh.bagchi.1@gmail.com)
# Last update: March 22, 2020
# Input needed: country.csv with headers: 
# Country	Quality	Healthcare-spend	Freedom-score	Freedom-category	Population(in1M)

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
import csv
import random as rnd


with open('Python-Data/country.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	country_list = []
	quality = []
	health_spend = []
	freedom_cat = []
	pop_mill = []

	i = 1

	for row in reader:
		if i == 1:
			i = 2
			continue
		country_list.append(row[0])
		quality.append(row[1])
		health_spend.append(row[2])
		freedom_cat.append(row[4])
		pop_mill.append(row[5])

pop_mill = [float(i) for i in pop_mill]
health_spend = [int(i) for i in health_spend]

size = np.interp(pop_mill, (min(pop_mill), max(pop_mill)), (200, 3500))

col = []
for fr in freedom_cat:
	if(fr == 'Free'):
		col.append('green')
	elif(fr == 'Partly free'):
		col.append('orange')
	else:
		col.append('red')

red_patch = mpatches.Patch(color='red', label='Not Free', alpha=0.7)
orange_patch = mpatches.Patch(color='orange', label='Partly Free', alpha=0.7)
green_patch = mpatches.Patch(color='green', label='Free', alpha=0.7)
population_patch = mpatches.Circle((0,0), 10, label='Size of population', alpha=0.7) # does not work, still generates rectangle patch

plt.rcParams["figure.figsize"] = (10,10)
# print (plt.rcParams["figure.dpi"])
plt.rcParams["figure.dpi"] = 288.0
# print (plt.rcParams["figure.dpi"])
fig=plt.figure()
# print (plt.figure().figsize) # does not work
# fig2 = plt.figure(figsize = 2*fig1.figsize)

y = np.array([0,1,2])
my_yticks = ['Not so great', 'Meh', 'Great job']
plt.yticks(y, my_yticks)

for i,country in enumerate(country_list):
	x = health_spend[i]
	y = quality[i]
	if(y=='B'):
		y = 0
	elif(y=='M'):
		y = 1
	else:
		y = 2
	plt.scatter(x, y, marker='o', color=col[i], s = size[i], alpha = 0.7)
	# print (" size[i] = ", size[i])
	plt.text(x-200, y+(rnd.randrange(1,15,3)/100), country, fontsize=9)    
    
ymin, ymax = plt.ylim()
# print (ymin, ymax)
plt.ylim(ymin, 1.05*ymax)

plt.xlabel('Healthcare spending per capita (in $)')
plt.ylabel('How well was Corona Virus contained')
line1 = plt.Line2D(range(2), range(2), color="white", marker='o', markerfacecolor="blue", markersize=20.0, label="Size of population")
plt.legend(handles=[green_patch, orange_patch, red_patch, line1])
# plt.legend([mpatches.Circle((0,0), fc='g')], ["Green Circle"])
plt.autoscale(enable=True, axis='x', tight=False)

plt.show()
