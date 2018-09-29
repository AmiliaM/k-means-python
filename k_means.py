import random
import numpy
import operator
import csv

import matplotlib.pyplot as plt
import matplotlib.cm as cm

n_means = 3 #the amount of clusters
means = [] #list containing n_means amount of Mean objects
n_samples = 50 #amount of test data points - replace with real data
samples = []
data_dimensions = 2

class Mean: #object to store one mean/centroid
    def __init__(self, pos):
        self.pos = pos
        self.points = []
        self.prev_points = [] #to check if the algorithm has completed
        self.color = None

def nearest_mean(x): #returns mean object closest to given point
    distances = {} #dict of mean to distance to point
    for mean in means: 
        distances[mean] = numpy.linalg.norm(mean.pos - x) 
    return min(distances.items(), key=operator.itemgetter(1))[0] 

def update_mean(): #assigns the means a new pos based on the centroid of its corresponding cluster (where the magic happens)
    for mean in means:
        mean.prev_points = mean.points
        for i in range(data_dimensions):
            mean.pos[i] =  sum(map(lambda x: x[i], mean.points))/len(mean.points)
            mean.pos[i] = sum(map(lambda x: x[i], mean.points))/len(mean.points)
        

def main():
    for _ in range(n_means):
        means.append(Mean(numpy.array([random.randint(1, 100), random.randint(1, 100)]))) #Randomly generates initial coordinates for Means
    colors = cm.rainbow(numpy.linspace(0, 1, len(means)))
    for i, c in enumerate(means):
        c.color: colors[i]
    samples = [[random.randint(1, 100), random.randint(1, 100)] for _ in range(n_samples)] #Randomly generate samples    
    
    print("Successfully generated sample list:")
    print(samples)
    fit = False
    while not fit:
        for sample in samples:
            closest = nearest_mean(sample)
            closest.points.append(sample)
        if len([c for c in means if c.points == c.prev_points]) == n_means: #check to see if all the points lists have been the same for 1 itr
            fit = True
            update_mean()
        else:
            update_mean()
    for mean in means:
        print("mean generation finished:")
        print(mean.points)
        print(" ")

    #plotting test
    for i, c in enumerate(means):
        plt.scatter(c.pos[0], c.pos[1], marker = 'o', color = c.color, s = 75)
        x_cors = [x[0] for x in c.points]
        y_cors = [y[1] for y in c.points]
        plt.scatter(x_cors, y_cors, marker = '.', color = c.color)
    plt.xlabel('x')
    plt.ylabel('y')
    title = 'K-means'
    plt.title(title)
    plt.savefig('{}.png'.format(title))
    plt.show()



if __name__ == "__main__":
    main()