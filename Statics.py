#Statics Calculator for common statics problems
#Jon Murders
#Originally Written February 6th, 2019

#Needed modules
import math

#Functions
def Resultant():
   number_F = input('How many individual forces do you have?')
   number_F = int(number_F)
   i=1
   magnitudes = []
   alphas = []
   betas = []
   gammas = []
   while i<=number_F:
       i = i+1
       F_m = input('What is the magnitude of the force?')
       magnitudes.append(F_m)
       F_alphas = input('What is the alpha direction angle of the force?')
       alphas.append(F_alphas)
       F_betas = input('What is the beta direction angle of the force?')
       betas.append(F_betas)
       F_gammas = input('What is the gamma direction angle of the force?')
       gammas.append(F_gammas)
   





problems = ['Solve for resultant: R','Solve for component: C','Solve for unknown force: F']

print('Please use the letter at the end of the line to select your choice')

for x in problems:
	print(x)
choice1 = input('What would you like to do?')

if choice1 == 'R':
    Resultant()


if choice1 == 'C':
    print('Sorry this is not supported yet')

if choice1 == 'F':
    print('Sorry this is not supported yet')

else:
    print('Please restart the program and select a valid input')
