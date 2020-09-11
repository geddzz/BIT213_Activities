# Simple Banking queue simulation program
# By: Marvin M. Monteagudo

# Added length of transactions for each costumer might have
# Modified by: Gerard Vince I. Lillo

# This simple program simulates the transaction queueing in a bank, assuming 
# that each teller has their own transaction completion capability

# Libraries
import random
import os

# Initialize random seed
random.seed = (os.urandom(1024))

# Arrays that will hold each teller's list of clients   
tellerA = []
tellerB = []
tellerC = []

# Integer that describes each teller's speed in completing a single 
# transaction. Smaller number means faster completion time
timeItTakesA = 1
timeItTakesB = 5
timeItTakesC = 10

# Minimum additional length of transactions
minimum = -2

# Maximum additional length of transactions
maximum = 5

# Initialized variable that will contain the actual running time for every 
# teller
runTimeA = 0
runTimeB = 0
runTimeC = 0

# Initialization of each teller, set to false as at the start, all tellers 
# have no client
hasCustA = False
hasCustB = False
hasCustC = False

# Initial customers list, where the alphabet is exploded into an array
aCustomers = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Initial count of the array
curCount = len(aCustomers)

# Transaction counter (for the message)
transCounter = 0

# Loop continues while the customers list is still more than 0
while curCount > 0:
    transCounter = transCounter + 1

    # Selecting a random number in the range of the minimum and maximum
    transaction_time_a = random.randint(minimum, maximum)
    transaction_time_b = random.randint(minimum, maximum)
    transaction_time_c = random.randint(minimum, maximum)

    # The new time is the sum of the teller's speed and the transaction time
    new_time_a = timeItTakesA + transaction_time_a
    new_time_b = timeItTakesB + transaction_time_b
    new_time_c = timeItTakesC + transaction_time_c

    if hasCustA == False:
        if len(aCustomers) > 0:
            tellerA.append(aCustomers.pop(0))
            hasCustA = True            
        else:
            break

    runTimeA = runTimeA + 1
    if runTimeA >= new_time_a:
        runTimeA = 0;
        hasCustA = False   

    msgA = "Done" if runTimeA == 0 else "Busy"
        
    if hasCustB == False:
        if len(aCustomers) > 0:
            tellerB.append(aCustomers.pop(0))
            hasCustB = True 
        else:
            break

    runTimeB = runTimeB + 1
    if runTimeB >= new_time_b:
        runTimeB = 0;
        hasCustB = False   

    msgB = "Done" if runTimeB == 0 else "Busy"
    
    if hasCustC == False:
        if len(aCustomers) > 0:
            tellerC.append(aCustomers.pop(0))
            hasCustC = True 
        else:
            break

    runTimeC = runTimeC + 1	
    if runTimeC >= new_time_c:
        runTimeC = 0;
        hasCustC = False   

    msgC = "Done" if runTimeC == 0 else "Busy"

    # The next 2 lines are used for debugging and tracing purposes    
    transMsg = "At Round #" + str(transCounter) + " | Teller A is " + msgA + " | Teller B is " + msgB  + " | Teller C is " + msgC
    print(transMsg)
    


print("The clients that went to teller A were: " + ", ".join(tellerA))
print("The clients that went to teller B were: " + ", ".join(tellerB))
print("The clients that went to teller C were: " + ", ".join(tellerC))
