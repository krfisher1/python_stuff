
import random

again = ""


while again != "no": 
    i = 0

    zookeeper_in_same_room_as_both_ele = 0
    zookeeper_in_same_room_as_one_ele = 0


    for i in range(100000):
        ele1 = random.randint(1,7)
        ele2 = random.randint(1,7)
        zookeeper = random.randint(1,7)
       
        if zookeeper == ele1 and zookeeper == ele2:
            zookeeper_in_same_room_as_both_ele += 1
        elif zookeeper == ele1 or zookeeper == ele2: 
            zookeeper_in_same_room_as_one_ele += 1    
        i += 1 

    zookeeper_in_same_room_as_both_ele = (zookeeper_in_same_room_as_both_ele / 100000)
    zookeeper_in_same_room_as_one_ele = (zookeeper_in_same_room_as_one_ele / 100000)

  


    if (.40033) >=  zookeeper_in_same_room_as_one_ele >= (.26633):
        zookeeper_right_1ele = True
    else:
        zookeeper_right_1ele = False    
    if (.16967) >= zookeeper_in_same_room_as_both_ele >= (.16367):
        zookeeper_right_2ele = True
    else:
        zookeeper_right_2ele = False    


    if zookeeper_right_1ele:
        print("Zookeeper is correct about being in the same pen as one of the elephants 1/3 of the time ")
    else:
        print("The zookeeper is wrong about being in the same pen as one of the elephants 1/3 times it is actually " + str(zookeeper_in_same_room_as_one_ele))
    if zookeeper_right_2ele:
        print("Zookeeper is correct about being in the same pem as two elephants 1/6 of the nights ")
    else:
        print("The zookeeper is wrong about being in the same pen as two of the elephants 1/6 times it is actually " + str(zookeeper_in_same_room_as_both_ele))



    again = input("Do you want to run the program again? enter yes or no ")

   


            




