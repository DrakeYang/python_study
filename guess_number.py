import random


user_name=str(input("Hello! What is your name? : "))
print('Well, '+user_name+', I am thinking of a number between 1 and 20.')
print('Take a guess.')
question=random.randint(1,21)

count=0
while(count<6):
	count+=1
	print (count)
