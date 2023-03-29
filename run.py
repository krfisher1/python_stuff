import random
i = 0
ele_in_same_room = 0
zookeeper_in_same_room_as_both_ele = 0
zookeeper_in_same_room_as_one_ele = 0
zookeeper_in_neither_rooms = 0
again = True




while i in range(100000):
    ele1 = random.randint(1,7)
    ele2 = random.randint(1,7)
    zookeeper = random.randint(1,7)
    if zookeeper == ele1 and zookeeper == ele2:
        zookeeper_in_same_room_as_both_ele += 1
    else: 
        zookeeper_in_same_room_as_one_ele


    i += 1    
 
print(zookeeper_in_same_room_as_both_ele) 
print(zookeeper_in_same_room_as_one_ele)