# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:03:20 2019

@author: Sam Kettlewell
"""

##Q1
from random import randint

#simulate a die throw 8 times
def die_throw8():
    return [randint(1,6) for x in range(8)]

#define some variables
throw = 1 #counts number of throws
counter = 0 #counts number satisfying criteria
max_throws = 10 #count upto/number of trials - HIGHER = MORE ACCURACY BUT LONGER TO RUN

while throw <= max_throws:
    #Throw a die eight times
    this_throw = die_throw8()
    
    #Count the number of evens and odds in this throw
    even_count = 0
    odd_count = 0
    
    for each_throw in this_throw:        
        if each_throw % 2 == 0:
            even_count += 1
            
        elif each_throw % 2 == 1:
            odd_count += 1
        
    #If the throw satisfies the criteria, add one to the counter
    if odd_count >= 2:
        if even_count >= 3:
            counter += 1
    
    #next throw       
    throw += 1

#print the approximate probability
print(counter/max_throws)

##Q2
from itertools import permutations, product

#Given a permutation, return the number of fixed points the permutation has
def no_of_fixed_points(perm):
    standard_list = sorted(perm) #Create the list [1,2,...,n]
    index = 0 #for comparing each value
    fixed_points = 0 #for counting fixed points
    
    #loop over the permutation and compare each element, if it's equal add one to the count
    while index < len(perm):
        if standard_list[index] == perm[index]:
            fixed_points = fixed_points + 1
        index = index + 1

    return fixed_points

n_value = 7 #count upto this number of n for permutations of {1,2,...,n}
counter = 0 #count the number of permutations with one fixed point
permutations_to_check = list(permutations([x for x in range(1, n_value+1)]))

#Loop through all the permutations and add one to the counter if each one has 1 fixed point
for each_perm in permutations_to_check:
    if no_of_fixed_points(each_perm) in [0,1,2,3]:
        counter = counter + 1

print("")
print(counter)
#print(len(permutations_to_check))

#Q3

print("q3")
from random import choice
alpha_numeric = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
print(len(alpha_numeric))

def choose_10_chars():
    return [choice(alpha_numeric) for x in range(10)]



print("")
##Q5
n_value = 6

x = ['a', 'b', 'c', 'd', 'e']
cartesian_product = [''.join(p) for p in product(x, repeat=n_value)]
#banned_characters = ['aaa', 'aab', 'aba', 'baa', 'abb', 'bab', 'bba', 'bbb']
count = len(cartesian_product)

#print(cartesian_product)
print(count)

for each_seq in cartesian_product:
    if 'aaa' in each_seq or 'aab' in each_seq or 'aba' in each_seq or 'baa' in each_seq or 'abb' in each_seq or 'bab' in each_seq or 'bba' in each_seq or 'bbb' in each_seq:
        #some have more than 1 banned seq in abaa is aba and baa
        #print(each_seq)
        count = count - 1

print(count)
#print(cartesian_product)


def subsets(n):
    #list of numbers from 1 to n
    s = [l for l in range(1, n+1)]
    
	# if n= 0, empty set
    if n == 0:
        return [[]]
    
    #Pick out the final (n-1)th element
    h = s[n-1]
    
    #Call the function on the (n-1)th element (recursive step)
    recursed_subsets = subsets(h-1)
    
    #this will only be run when the program has recursively done all the n's
    element_added_subsets = [] 
    
    #for each subset we've recursively generated
    for each_subset in recursed_subsets:
        element_added_subsets.append([h] + each_subset)
    return recursed_subsets + element_added_subsets
 
def hanoi(p1, p2, p3, n):
    moves = []
    
    if n == 1:
        moves.append((p1, p3))
    
    else:
        next_move = hanoi(p1, p3, p2, n-1)
        moves.append(next_move)
        
        moves.append((p1, p3))
        
        next_move = hanoi(p2, p1, p3, n-1)
        moves.append(next_move)
    
    return moves

print(hanoi('p1', 'p2', 'p3', 1))