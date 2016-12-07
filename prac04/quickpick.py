import random
picks = []

userinput = int(input("How many quick picks?"))

for i in range(userinput):
    temp_picks = []
    for j in range(6):
        rand_no = random.randint(1, 45)
        temp_picks.append(rand_no)
        #how to ensure no duplication?
