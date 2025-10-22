import math
import sys

class BICON:
    #Binary to Integer Method
    @staticmethod
    def bin_to_int(bin):
        i = 0
        res = 0
        #From end of the binary to start
        for b in bin[::-1]:
            #Multiply each number with its level of two
            res += int(b) * pow(2,i)
            #Move to next level
            i += 1
        #Return result
        return res
    
    @staticmethod
    #Binary to String Method(Use _ between each character)
    def bin_to_string(bin):
        res = ""
        #Split given binary to characters
        bin_list = bin.split("_")

        #For each binary character
        for part in bin_list:
            #Convert binary character to integer
            num = BICON.bin_to_int(part)
            #Add its character equavelent to result
            res += chr(num)
        
        #Return result
        return res
    
    #Integer to Binary Method
    @staticmethod
    def int_to_bin(num):
        #Set remainder to given number
        rem = int(num)
        
        #If number is 0, return 0
        if rem == 0:
            return "0"
        
        #Initialize Result variable
        res = ""

        #While there is a remainder
        while rem > 0:
            #Set mod to mod with 2 of remainder
            mod = rem % 2
            #Set remainder to remainder // 2
            rem = rem // 2
            #If mod is 1, add 1 to res
            if mod == 1:
                res += "1"
            #Else mod is 0, add 0 to res
            else:
                res += "0"
        #Return reverse of mod since we add numbers to result in reverse
        return res[::-1]
    
    #String to Binary Method
    @staticmethod
    def string_to_bin(text=""):
        res = ""
        #For each character in text
        for c in text:
            #Convert it to int and convert that int to binary
            num = ord(c)
            res += BICON.int_to_bin(num) + " "
        #Return result(without space in the end)
        return res[:-1]

#Main Function
def main():
    #Get operation type and data from command line
    opr = sys.argv[1]
    data = sys.argv[2]
    #Do operations accordingly
    if opr == "BIN_INT":
        print(BICON.bin_to_int(data))
    elif opr == "BIN_STR":
        print(BICON.bin_to_string(data))
    elif opr == "INT_BIN":
        print(BICON.int_to_bin(data))
    elif opr == "STR_BIN":
        print(BICON.string_to_bin(data))
    else:
        print("Invalid Type")

if __name__ == "__main__":
    main()