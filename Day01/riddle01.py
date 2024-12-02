list1 = []
list2 = []


def riddle(list1, list2):
    list1.sort()
    list2.sort()
    result = 0
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            result += (list1[i] - list2[i])
        else:
            result += (list2[i] - list1[i])
    return result

def get_input():
    with open("Day01/input.txt", "r") as f:
        for line in f:
            print(line)
            line = line.split("   ")
            list1.append(int(line[0]))
            list2.append(int(line[1]))
    return (list1, list2)

if __name__ == "__main__":
    list1, list2 = get_input()
    #list1 = [3,4,2,1,3,3]
    #list2 = [4,3,5,3,9,3]
    print(riddle(list1, list2))