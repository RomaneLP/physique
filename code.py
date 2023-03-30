import numpy as np
import scipy.integrate as integrate


""" 
We will represent the city by a list of Q lists of length H that represents the blocks. Each list representing the blocks will be filled
with 0 if noone lives in that flat or 1 if someone does. This list will be named L.

Since it is used a lot, let's begin by making a function that gives back a list with the density of each cube.
"""

# PRELIMINARY FUNCTION

def density (L):
    Q= len(L)
    H= len(L[0])
    dens=[]
    for i in range (Q):
        a=0
        for j in range (H):
            if L[i,j]==1:
                a+=1
        dens.append(a/H)
    return dens

# we have yet to write the indiv_utility function that represents individual utility


def individual_utility(dens,m): # 0<m<1 asymmetry parameter
    if dens <= 1/2 :
         return 2*dens
    else :
        return m + 2*(1-m)*(1-dens)


densite= np.linspace(0,1,100)











def collective_utility(L): 
    dens=density(L)
    H= len(L[0])
    answer=0
    for i in range (len(L)):
        answer+=H*dens[i]*indiv_utility(dens[i])
    return answer



# PROBABILITY OF MOVING

def gain(L,alpha, start, end):
    #let's make a new list representing the new city
    new_city= L.copy()
    new_city[a,b]=0
    new_city[c,d]=1
    #let's calculate the gain 
    delta_u=abs(indiv_utility(L)-indiv_utility(new_city))
    delta_U=abs(collective_utility(L)-collective_utility(new_city))
    return( delta_u+ alpha*(delta_U -delta_u) )

def moving_probability(L,alpha,T, start, end):
    G=gain(L,alpha, start, end)
    return (1/ (1 + np.exp(- G/T)))



# PARTIE 2 - Calculating the distribution 

def block_potential (dens,T,alpha): #f
    answer=0
    answer+= -T*dens*np.log(dens)- T*(1-dens)*np.log(1-dens)+ alpha*dens*indiv_utility(dens)
    answer+= integrate.quad(indiv_utility, 0, dens)
    return answer

def F(L,T,alpha):   #potential F
    dens=density(L)
    H= len(L[0])
    answer=0
    for i in range (len(L)):
        answer+=H*block_potential(dens[i],T,alpha)
    return answer

def distribution(L,Z,T,alpha):
    return (np.exp(F(L,T,alpha)/T)/Z)