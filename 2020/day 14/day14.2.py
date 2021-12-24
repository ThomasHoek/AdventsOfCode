
import copy

inputfile =  [i.rstrip() for i in open("input.txt","r")]

mem_dict = {}


def get_binary(inp):            # https://stackoverflow.com/questions/699866/python-int-to-binary-string
    return "{0:b}".format(inp)

def binary_calc(imp,mask):
    new_binary = ""
    imp = '0' * (len(mask) - len(imp)) + imp
    for i in range(len(imp)):
        
        if mask[i] == "0":
            new_binary += imp[i]
        
        elif mask[i] == "X":
            new_binary += "X"

        elif mask[i] == "1":
            new_binary += "1"
    return new_binary

def float_to_lst(result):
    total_lst = [result]
    
    while sum([1 if "X" in i else 0 for i in total_lst]):
        new_lst = []
        for value in total_lst:
            if "X" in value:
                new_lst.append(value[:value.find("X")] + "0" + value[value.find("X") + 1:])
                new_lst.append(value[:value.find("X")] + "1" + value[value.find("X") + 1:])
    
        total_lst = copy.deepcopy(new_lst)

    return total_lst


mask = 0
for line in inputfile:
    if "mask" in line:
        mask = line.split("=")[1]
    
    else:
        
        num,decimal = line.split("=")
        num = int(num[4:-2])
        binary= get_binary(int(num))
        float_lst = float_to_lst(binary_calc(binary,mask))
        float_lst.sort()
        for value in float_lst:
            mem_dict[int(value,2)] = int(decimal)
        
print(sum(mem_dict.values()))
