def initial_state():
    return (8, 0, 0)

def is_goal(s):
    if s == (4,4,0): return s

def successors(s):
    x, y, z = s
    array = []

    if x > 0 and y < 5 : amount_of_water = min(x, 5-y)
    array.append(((x - amount_of_water, y + amount_of_water, z),amount_of_water)) 
    if x > 0 and z < 3 : amount_of_water = min(x, 3-z)
    array.append(((x - amount_of_water, y, z + amount_of_water),amount_of_water)) 
    if y > 0 and x < 8 : amount_of_water = min(y, 8-x)
    array.append(((x + amount_of_water, y-amount_of_water, z),amount_of_water)) 
    if y > 0 and z < 3 : amount_of_water = min(y, 3-z)
    array.append(((x, y - amount_of_water, z + amount_of_water),amount_of_water)) 
    if z > 0 and x < 8 : amount_of_water = min(z, 8-x)
    array.append(((x + amount_of_water, y, z-amount_of_water),amount_of_water))
    if z > 0 and y < 5 : amount_of_water = min(z, 5-y)
    array.append(((x, y+amount_of_water, z-amount_of_water),amount_of_water)) 
    return array