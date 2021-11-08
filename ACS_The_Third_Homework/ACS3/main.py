import sys
import os.path
import tracemalloc
from Proverb import Proverb
from Aphorism import Aphorism
from Riddle import Riddle
import random
import string
from timeit import default_timer as timer

lst = []
size = 0
punctuation = ".,!?-():;"
default_output_file1 = "output1.txt"
default_output_file2 = "output2.txt"


def Randoming():
    global punctuation
    letter_list = string.ascii_lowercase
    letter_list += "   " + punctuation
    gen_string = ''.join(random.choice(letter_list) for i in range(25))
    gen_string += "\n"
    return gen_string


def Random_Forming():
    for i in range(0, size):
        type = random.randint(1, 3)
        if type == 1:
            aph = Aphorism(Randoming(), Randoming())
            lst.append(aph)
        elif type == 2:
            prov = Proverb(Randoming(), Randoming())
            lst.append(prov)
        elif type == 3:
            rid = Riddle(Randoming(), Randoming())
            lst.append(rid)


def fileinput(path):
    global lst
    global size
    myfile = open(path, "r")
    size = myfile.readline()
    try:
        size = int(size)
    except:
        errorInfo2()
        return 3
    if size < 1 or size > 10000:
        return 3
        errorInfo2()
    for i in range(0, size):
        status = myfile.readline()
        try:
            status = int(status)
        except:
            errorInfo3()
            return 3
        if status < 1 or status > 3:
            errorInfo3()
            return 3
        if status == 1:
            aph = Aphorism(myfile.readline(), myfile.readline())
            lst.append(aph)
        elif status == 2:
            prov = Proverb(myfile.readline(), myfile.readline())
            lst.append(prov)
        elif status == 3:
            rid = Riddle(myfile.readline(), myfile.readline())
            lst.append(rid)
    myfile.close()
    return 1


def errorInfo1():
    print("\nIncorrect input in command line.\nIt should consist of:")
    print("\nfile input.txt output1.txt output2.txt")
    print("\nor:");
    print("\nrandom number_of_instances output1.txt output2.txt")


def errorInfo2():
    print("\nThe size data was incorrect. The size should be less than 10000 and greater than 1.")
    print("\nIn this time the program will execute the random filling method to continue the current launch.")


def errorInfo3():
    print("\nThe type of structure was incorrect.")
    print("\nIn this time the program will execute the random filling method to continue the current launch.")


def errorInfo4():
    print("\nThe first argument was sent in an incorrect form.")
    print("\nIn this time the program will execute the random filling method to continue the current launch.")


def errorInfo5():
    print("\nThe second output file does not exist. Please check the spelling.")
    print("\nIn this time the program will continue with the default output file placed in debug folder.")


def File_Inp(output_file):
    global lst
    global size
    # Файловый поток на вывод.
    myfile = open(output_file, "w")
    myfile.write("There are ")
    myfile.write(str(size))
    myfile.write(" examples in the array")
    myfile.write("\n")
    for i in range(0, size):
        myfile.write(str(lst[i].returnTheContent()))
        myfile.write(str(lst[i].returnTheOwnField()))
    myfile.close()


def AltFun(content):
    global punctuation
    num = len(content)
    num1 = 0
    for i in range(0, num):
        if punctuation.find(content[i]) != -1:
            num1 += 1
    return num1 / num


def binary_search(val, start, end):

    if start == end:
        if AltFun(lst[start].returnTheContent()) < AltFun(val.returnTheContent()):
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if AltFun(lst[mid].returnTheContent()) > AltFun(val.returnTheContent()):
        return binary_search(val, mid + 1, end)
    elif AltFun(lst[mid].returnTheContent()) < AltFun(val.returnTheContent()):
        return binary_search(val, start, mid - 1)
    else:
        return mid


def Binary_Insertion():
    global lst
    for i in range(1, len(lst)):
        val = lst[i]
        j = binary_search(val, 0, i - 1)
        lst = lst[:j] + [val] + lst[j:i] + lst[i + 1:]


def main():
    tracemalloc.start()
    start_time = timer()
    global size
    global lst
    if len(sys.argv) != 5:
        errorInfo1()
        return 1
    print("Now we are ready to start!")
    if sys.argv[1] == "file":
        if os.path.exists(sys.argv[2]):
            print("Input file does exist")
            checker = 1
        else:
            print("There is no such input file. The program will continue with random method")
            checker = 2
    elif sys.argv[1] == "random":
        print("We will continue with automatic method")
        try:
            size = int(sys.argv[2])
        except Exception(BaseException):
            size = random.randint(1, 10)
        if size < 1 or size > 10000:
            size = random.randint(1, 10)
        checker = 2
    else:
        print("There is no such type of input data. The program will continue with random method")
        checker = 3
    if os.path.exists(sys.argv[3]):
        print("The first output file does exist")
        output_file1 = sys.argv[3]
    else:
        errorInfo4()
        output_file1 = default_output_file1
    if os.path.exists(sys.argv[4]):
        print("The second output file does exist")
        output_file2 = sys.argv[4]
    else:
        errorInfo4()
        output_file2 = default_output_file2
    if checker == 1:
        checker = fileinput(sys.argv[2])
    if checker != 1:
        if checker == 3:
            size = random.randint(1, 10)
            lst.clear()
        Random_Forming()
    File_Inp(output_file1)
    Binary_Insertion()
    File_Inp(output_file2)
    print("\nThis is the end of our journey. Thank you for joining us today!")
    print(tracemalloc.get_traced_memory())
    print(timer() - start_time)


if __name__ == "__main__":
    main()
