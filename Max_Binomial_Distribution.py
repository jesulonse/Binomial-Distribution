import math

#Given the following values for probability of heads of coin,p and n is number of coin flips, k is  no. of heads 
#We want to determine the number of heads that gives the maximum value for the binomial distribution
p = 0.5
n = 20
k = 0
binomial_dist_list = list()
for i in range(0, 20):
    num_of_combinations = (math.factorial(n)/(math.factorial(n - k) * math.factorial(k)))
    binomial_dist = num_of_combinations *  p**k * (1 - p)**(n - k)
    binomial_dist_list.append(binomial_dist)
    k+=1
# number of heads that yields the max value of binomial distribution is max_val_k
max_val_k = binomial_dist_list.index(max(binomial_dist_list))
print(max_val_k)
