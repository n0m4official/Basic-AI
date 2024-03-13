import random

ai_level=10 #Change the number to increase/decrease the chance of the character moving. 0=not active
num=(random.randint(1,20))        #Movement opprotunity generator
speed=(random.randint(1,10))      #Speed value generator
direction=(random.randint(1,4))   #Direction value generator
distance=(random.randint(1,10))   #Distance value generator

if ai_level >0 :                  #Ignore this
    print("AI: active")

else :                            #Ignore this
    print("Character not active")

if num <=ai_level :               #If this condition is met, the character will move. If met, the rest of the code will function.
    print("Move: true")

else :                            #Otherwise, the character will stay where they are.
    print("Move: false")

print(num)

if num <=ai_level :               #if a movement opprotunity has succeeded, a random speed will be generated
    if speed <5 :
        print("Speed: slow")

    if speed == 5 :
        print("Speed: average")

    if speed >5 :
        print("Speed: fast")
    
    print(speed)

else :                            #if a movement opprotunity has failed, no speed will be generated  
    print("Speed: n/a")
    print("No Movement")

if num <=ai_level :               #if a movement opprotunity has succeeded, a random direction will be generated
    if direction == 1 :
        print("Direction: forward")

    if direction == 2 :
        print("Direction: backward")

    if direction == 3 :
        print ("Direction: right")

    if direction == 4 :
        print("Direction: left")
    
    print(direction)

else :                            #if a movement opprotunity has failed, no direction will be generated
    print("Direction: n/a")
    print("No Movement")

if num <=ai_level :               #if a movement opprotunity has succeeded, a random distance will be generated
    print("Distance to travel:", distance, "meters")
    print(distance)

else :                            #if a movement opprotunity has failed, no direction will be generated
    print("Distance: n/a")
    print("No Movement")

 
