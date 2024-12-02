list1 = []
list2 = []

def riddle2(list1, list2):
    result = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            result += (list1[i]*list2.count(list1[i]))
    return result
            

def get_input():
    with open("Day01/input.txt", "r") as f:
        for line in f:
            line = line.split("   ")
            list1.append(int(line[0]))
            list2.append(int(line[1]))
    return (list1, list2)

if __name__ == "__main__":
    list1, list2 = get_input()
    #list1 = [3,4,2,1,3,3]
    #list2 = [4,3,5,3,9,3]
    #print(riddle1(list1, list2))
    print(riddle2(list1, list2))
    
    
