import re



def get_input():
    lines = ""
    with open("Day03/input.txt", "r") as f:
        for line in f:
            lines += line
    return lines
    
def riddle1(inst_line):
    result = 0
    # Look in inst_line for mul(x,y)
    allMult = re.findall(r"mul\(([0-9]{1,3},[0-9]{1,3})\)|(do\(\))|(don't\(\))", inst_line)
    print(re.findall(r"do\(\)", inst_line))
    print(allMult)
    allMult = [match[0] or match[1] or match[2] for match in allMult]
    mul_enabled = True
    for instruction in allMult:
        print(instruction)
        if instruction == "do()":
            mul_enabled=True
        elif instruction == "don't()":
            mul_enabled=False
        elif instruction:  
            if mul_enabled:
                x,y = instruction.split(",")
                x = int(x)
                y = int(y)
                
                result += x*y
        # Seperate x,y via .split(",") or other methods and convert to int 
            
    return result
    
    
    
        
if __name__ == "__main__":
    list1 = get_input()
    
    #instr_line1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    
    #instr_line2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5)"
    
    print(riddle1(list1))
    