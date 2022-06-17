import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# set the plot style
plt.style.use('fivethirtyeight')

# generate 4 random numbers from the interval  <0,1)
random_num = np.random.random(4)
random_num

# this sets the seed to number 42
np.random.seed(42)

n = 10
p = 0.5
size = 1000

samples = np.random.binomial(n, p, size)

head_occu_count = Counter(samples) 

head_proba = [val/size for val in head_occu_count.values()]

plt.scatter(x=head_occu_count.keys(), y=head_proba)
plt.xlabel('number of heads out of 10 tosses')
plt.ylabel('probability')

# show the plot
plt.show()