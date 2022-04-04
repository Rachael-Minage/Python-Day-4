#Randomozation and lists
import random
#Getting a random integer
random_integer = random.randint(1,100)
print(random_integer)
#Getting a random float
random_float = random.random()
print(random_float)
random_float2 = random.random()*5
print(random_float2)
random_float3= random.random()*10
print(random_float3)

#Heads or tails tosser
seed = int(input("Enter a random number:\n"))
random.seed(seed)
random_side =int (random.randint(0,1))
if random_side ==0:
    print("Heads")
else:
    print("Tails")
    
#Python lists []

Kenya_counties = ["kajiado","Nairobi","Kilifi","Marsabit","Kakamega","Bungoma","Nakuru"]
print(Kenya_counties[4])
Kenya_counties.extend(["Turkana","Lamu","Kwale"])
print(Kenya_counties)
Kenya_counties.append("Kisumu")
print(Kenya_counties)

#Bankers roulette
test_seed = input("Create a seed number:\n")
random.seed(test_seed)
Names= input("Enter customer names:\n")
random_names= Names.split(",")
print("random_names")
names_length = len(random_names)
person_paying = random.randint(0,names_length-1)
payer =random_names[person_paying]
print(f"{payer} is taking today's bill" )

#Nested lists
fruits = ["Strawberries","Apples","Pineapples","guavas","Bananas","pears"]
vegetables = ["spinach", "Kales","Tomatoes","Pepper","Carrots","Cabbages"]

dirty_dozen =[fruits,vegetables]
print(dirty_dozen)
 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to python RPS")
game_images = [rock,paper,scissors]
Choice =int (input("Enter choice 0 for rock, 1 for paper and 2 for scissors\n"))
print(game_images[Choice])
import random
computer_choice= random.randint(0,2)
print("computer chose:\n")
print(game_images[computer_choice])
if Choice>=3 or Choice <0:
	print("Invalid choice.Try again")
elif computer_choice ==0 and Choice ==2:
	print("You win")
elif Choice==0 and computer_choice==2:
	print("You lose")
elif computer_choice>Choice:
	print("You lose")
elif Choice > computer_choice:
	print("You win")
elif computer_choice == Choice:
	print("It's a draw")

else:
	print("Invalid number")
	
	
	


 





