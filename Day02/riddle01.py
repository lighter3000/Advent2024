




def riddle1():
    result = 0
    list1 = []
    with open("Day02/input.txt", "r") as f:
        for line in f:
            line = line.split(" ")
            list1 = list(map(int, line)) # Converts string list to int list
            result += is_safe(list1)
    return result
            
def is_safe(list):
    # Only safe if the levels are either all increasing or decreasing
    # Any two adjacent levels differ by at least one and at most three
    if all(earlier > later and 1 <= (earlier - later) <=3 for earlier, later in zip(list, list[1:])): 
        return 1
    elif all(earlier < later and 1 <= (later - earlier) <=3 for earlier, later in zip(list, list[1:])):
        return 1
    else:
        return 0
        
                
    
    
if __name__ == "__main__":
    #list_full = [[7,6,4,2,1],
    #            [1,2,7,8,9],
    #            [9,7,6,2,1],
    #            [8,6,4,4,1],
    #            [1,3,6,7,9]]
    #for thing in list_full:
    #    print(is_safe(thing))
    print(riddle1())