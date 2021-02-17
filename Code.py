
"""######################### IMPORTED MODULE(S) #########################"""
import random

"""######################### GLOBAL VARIABLES #########################"""
MM = []
Cache = []
n = 0

"""######################### HELPER FUNCTIONS #########################"""

"""
:Function Name: CheckPositiveInteger
:Number of Parameters: 1 
:Type of Parameters: int
:Return Type: - 
:Function Description: Check if an integer is positive or not
"""


def CheckPositiveInteger(num):
    """
    :param num: An integer
    :return: Nothing
    """
    try:
        if num < 1:
            print("Memory size/Address cannot be negative or zero")
            exit()
    except TypeError:
        print("Wrong input format")


"""
:Function Name: BinToInt
:Number of Parameters: 1 
:Type of Parameters: string
:Return Type: int
:Function Description: Return decimal equivalent of a binary number
"""


def BinToInt(num):
    """
    :param num: A string containing binary equivalent of an integer
    :return: Decimal equivalent of binary number
    """
    i = '0b' + num
    return int(i, 2)


"""
:Function Name: Address
:Number of Parameters: 1 
:Type of Parameters: int
:Return Type: string
:Function Description: convert address from integer to binary
"""


def Address(num):
    """
    :param num: An integer
    :return: Binary equivalent with appropriate number of bits
    """
    bin_val = bin(num)[2:]
    bin_val = '0' * (N - len(bin_val)) + bin_val
    return bin_val


"""
:Function Name: SearchInCache
:Number of Parameters:  2
:Type of Parameters: list, string
:Return Type: boolean
:Function Description: Search for address is Cache 
"""


def SearchInCache(l, add):
    """
    :param l: A list
    :param add: A string containing binary address
    :return: True if address is present in list, False if not
    """
    for frame in l:
        if BinToInt(add) in frame:
            return True
    return False


"""
:Function Name: ReadAddress
:Number of Parameters: 0
:Type of Parameters: -
:Return Type: int
:Function Description: Input address to be searched in cache from user
"""


def ReadAddress():
    """
    :return: A string containing binary equivalent of entered address
    """
    A = int(input("\nEnter Main Memory address to search for (integer form) : "))

    if A >= 2 ** N or A < 0:
        print("Address size too large!")
        exit()
    add = Address(A)
    print("Entered address : " + add)
    return add


"""######################### CREATING FUNCTIONS #########################"""

"""
:Function Name: CreateDirectMapped
:Number of Parameters: 0
:Type of Parameters: -
:Return Type: -
:Function Description: Create a Directly mapped Cache 
"""


def CreateDirectMapped():
    """
    :return: Nothing
    """
    global Cache, MM
    choices = []

    for i in range(2 ** CL):
        choices.append([])

    temp = []

    for i in range(2 ** BL):
        if i % (2 ** CL) == 0:
            temp.append(i)

    choices[0] = temp

    for i in range(1, 2 ** CL):
        choices[i] = [j + 1 for j in choices[i - 1]]
    for i in range(len(Cache)):
        Cache[i] = MM[random.choice(choices[i])]

    print("\nCache memory:")
    print(*Cache, sep='\n')


"""
:Function Name: CreateFullyAssociated
:Number of Parameters: 0
:Type of Parameters: -
:Return Type: -
:Function Description: Create a fully associative cache
"""


def CreateFullyAssociated():
    """
    :return: Nothing
    """
    global Cache, MM
    choices = random.sample(MM, 2 ** CL)
    Cache = choices
    print("\nCache memory:")
    print(*Cache, sep='\n')


"""
:Function Name: CreateSetAssociated
:Number of Parameters: 0
:Type of Parameters: -
:Return Type: -
:Function Description: Create a N-way set associative cache
"""


def CreateSetAssociated():
    """
    :return: Nothing
    """
    global Cache, MM
    print("\nSets are of order 2^n")
    global n
    n = int(input("enter n : "))

    if n < 1:
        print("Sets have to have at least 2 elements")
        exit()

    ss = (CL - n)
    choices = []
    for i in range(2 ** ss):
        choices.append([])

    if ss == 0:
        print("Cache cannot have just one set. Please enter a smaller set size")
        exit()
    else:
        c = []

        for i in range(0, len(Cache), 2 ** n):
            c.append(Cache[i:i + 2 ** n])
        Cache = c

    temp = []
    for i in range(2 ** BL):
        if i % 2 ** ss == 0:
            temp.append(i)

    choices[0] = temp
    for i in range(1, 2 ** ss):
        choices[i] = [j + 1 for j in choices[i - 1]]
    for i in range(2 ** ss):
        ch = random.sample(choices[i], 2 ** n)
        for j in range(2 ** n):
            Cache[i][j] = MM[ch[j]]
    print("\nCache memory:")
    print(*Cache, sep='\n')


"""######################### SEARCHING FUNCTIONS #########################"""

"""
:Function Name: SearchDirectMapped
:Number of Parameters: 1
:Type of Parameters: string
:Return Type: -
:Function Description: Search for address in Direct mapped cache
"""


def SearchDirectMapped(add):
    """
    :param add: A sting containing binary equivalent of entered address
    :return: Nothing
    """
    global Cache, MM
    tag = add[:BL - CL]
    line = add[BL - CL:BL]
    offset = add[len(add) - B:]

    if BinToInt(add) == Cache[BinToInt(line)][BinToInt(offset)]:
        print("\nCache hit!")
        print("Tag = " + tag)
        print("Line = " + line)
        print("Block offset = " + offset)
    else:
        print("\nCache miss!")
        print("Loading into Cache...")
        Cache[BinToInt(line)] = MM[BinToInt(add[:BL])]
        print("Tag = " + tag)
        print("Line = " + line)
        print("Block offset = " + offset)
        print("\nCache memory:")
        print(*Cache, sep='\n')


"""
:Function Name: SearchFullyAssociated
:Number of Parameters: 1
:Type of Parameters: string
:Return Type: -
:Function Description: Search for address in fully associated cache
"""


def SearchFullyAssociated(add):
    """
    :param add: A sting containing binary equivalent of entered address
    :return: Nothing
    """
    global Cache, MM
    tag = add[:BL]
    offset = add[BL:]
    if SearchInCache(Cache, add):
        print("\nCache hit!")
        print("Tag = " + tag)
        print("Block offset = " + offset)
    else:
        print("\nCache miss!")
        print("Loading into Cache...")
        Cache[random.randint(0, (2 ** CL) - 1)] = MM[BinToInt(tag)]
        print("Tag = " + tag)
        print("Block offset = " + offset)
        print("\nCache memory:")
        print(*Cache, sep='\n')


"""
:Function Name: SearchSetAssociated
:Number of Parameters: 1
:Type of Parameters: string
:Return Type: -
:Function Description: Search for address in N-way associated cache
"""


def SearchSetAssociated(add):
    """
    :param add: A string containing binary equivalent of entered address
    :return: Nothing
    """
    ss = CL - n
    k = BL - ss

    tag = add[:k]
    setnum = add[k:k + ss]
    offset = add[k + ss:]

    if SearchInCache(Cache[BinToInt(setnum)], add):
        print("\nCache hit!")
        print("Tag = " + tag)
        print("Set number = " + setnum)
        print("Block offset = " + offset)
    else:
        print("\nCache miss!")
        print("Loading into Cache...")
        Cache[BinToInt(setnum)][random.randint(0, (2 ** n) - 1)] = MM[BinToInt(add[:BL])]
        print("Tag = " + tag)
        print("Set number = " + setnum)
        print("Block offset = " + offset)
        print("\nCache memory:")
        print(*Cache, sep='\n')


"""######################### MAPPING FUNCTIONS #########################"""

"""
:Function Name: DirectMapping
:Number of Parameters: 0
:Type of Parameters: -
:Return Type: -
:Function Description: Call functions for creating and searching a direct mapped cache 
"""


def DirectMapping():
    """
    :return: Nothing
    """
    CreateDirectMapped()
    c = 'y'
    while c == 'y' or c == 'Y':
        add = ReadAddress()
        SearchDirectMapped(add)
        c = input("\nDo you wish to find another address? (y/n): ")


"""
:Function Name: FullyAssociativeMapping
:Number of Parameters: 0
:Type of Parameters: -
:Return Type: -
:Function Description: Call functions for creating and searching a fully associated cache
"""


def FullyAssociativeMapping():
    """
    :return: Nothing
    """
    CreateFullyAssociated()
    c = 'y'
    while c == 'y' or c == 'Y':
        add = ReadAddress()
        SearchFullyAssociated(add)
        c = input("\nDo you wish to find another address? (y/n): ")


"""
:Function Name: SetAssociatedMapping
:Number of Parameters: 0
:Type of Parameters: -
:Return Type: -
:Function Description: Call functions for creating and searching a N-way associated cache 
"""


def SetAssociativeMapping():
    """
    :return: Nothing
    """
    CreateSetAssociated()
    c = 'y'
    while c == 'y' or c == 'Y':
        add = ReadAddress()
        SearchSetAssociated(add)
        c = input("\nDo you wish to find another address? (y/n): ")


"""
:Function Name: CacheMapping
:Number of Parameters: 1
:Type of Parameters: int
:Return Type: -
:Function Description: call functions for different types of mappings 
"""


def CacheMapping(mapping):
    """
    :param mapping: An integer to choose which tpe of mapping
    :return: Nothing
    """
    if mapping == 1:
        DirectMapping()
    elif mapping == 2:
        FullyAssociativeMapping()
    elif mapping == 3:
        SetAssociativeMapping()
    else:
        print("Option does not exist. Please try again")
        exit()


"""######################### MAIN PROGRAM #########################"""

print("\nMain memory size is 2^N")
N = int(input("Enter N: "))
CheckPositiveInteger(N)

print("\nBlock size is 2^B")
B = int(input("Enter B: "))
CheckPositiveInteger(B)

print("\nCache memory size is 2^S")
S = int(input("Enter S: "))
CheckPositiveInteger(S)

if S >= N:
    print("Cache size cannot be larger than or equal to Main memory size")
    exit()

if S <= B:
    print("Cache size cannot be smaller than or equal to Block size")
    exit()

CL = S - B
print("\nCache lines (CL): " + str(2 ** CL))

BL = N - B
print("Number of blocks in Main memory: " + str(2 ** BL))

print("\nBuilding Main Memory...")
a = 0
for i in range(2 ** (N - B)):
    t = []
    for j in range(2 ** B):
        t.append(a)
        a += 1
    MM.append(t)

for i in range(2 ** CL):
    Cache.append([])

print("\nMain Memory:")
print(*MM, sep='\n')

print("\nTypes of Mappings:")
print("1. Direct Mapping")
print("2. Fully Associative Mapping")
print("3. N-way Set Associative Mapping")
mapping = int(input("\nEnter the type of Mapping you want (1,2,3) : "))

CacheMapping(mapping)

"""######################### END OF PROGRAM #########################"""
