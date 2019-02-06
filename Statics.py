#Statics Calculator for common statics problems
#Jon Murders
#Originally Written February 6th, 2019

#Needed modules
import math

#Functions
def Resultant():
    number_F = input('How many individual forces do you have?')
   i=0
   magnitudes = []
   alphas = []
   betas = []
   gammas = []
   for number_F:
       i = i+1
       F_m = input('What is the magnitude of the force?')
       magnitudes.append(i) = F_m



problems = ['Solve for resultant: R','Solve for component: C','Solve for unknown force: F']

print('Please use the letter at the end of the line to select your choice')

for x in problems:
	print(x)
choice1 = input('What would you like to do?')

if choice1 = 'R':
    print('Working on')


if choice1 = 'C':
    print('Sorry this is not supported yet')

if choice1 = 'F':
    print('Sorry this is not supported yet')

else:
    print('Please restart the program and select a valid input')
