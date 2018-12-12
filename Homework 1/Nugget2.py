
def is_nugget_number(candidate, packets):
    s = packets['s']
    m = packets['m']
    l = packets['l']
    for i in range(candidate//s + 1):  # look at these for loops in a console to understand with a unit of 3
        for j in range(candidate//m + 1):
            for k in range(candidate//l + 1):
                if(candidate == i*s + j*m + k*l):
                    return True
                

packets = {'s' : 6, 'm' :9, 'l' : 20}


# Is a given number a nugget number
candidate = packets['s']

# keep track of how many candidates in a row are nugget numbers
count = 0

# what is the most recent candidate that was not a nuggt number
largest = 0

# Loop until stopping met
while count < packets['s']:
    if is_nugget_number(candidate, packets):
        count+=1
    else:
        count = 0
        largest = candidate
        
    candidate += 1
    
print(f"The largest number of nuggets that I cannot get is: {largest}")
    