import os

# **** read the specified text file ****
def read_file(fileName):

    # **** open the specified text file ****
    try:
        stream = open(fileName)
    except OSError:
        print(f"open fileName ==>{fileName}<== exception OSError")
        os._exit(-1)
    except:
        print(f"open fileName ==>{fileName}<== failed")
        os._exit(-1)

    # **** check if stream is NOT readable ****
    if stream.readable() == False:
        print(f"fileName ==>{fileName}<== not readable")
        os._exit(-1)

    # **** read and display the contents of the text file ****
    count = 0
    while True:

        # **** read the next line from the file ****
        line = stream.readline()

        # **** check if the line is empty (end of file) ****
        if not line:
            break
        
        # **** remove trailing CR from the line ****
        line = line.rstrip()

        # **** skip this line (if empty) ****
        if line == "":
            continue

        # **** display the line ****
        print(f"line ==>{line}<==")

        # **** count this line ****
        count += 1

    # **** close the specified text file ****
    stream.close()

    # **** display the number of lines displayed ****
    print(f"\ncount: {count}")


# **** write the specified text file ****
def write_file(fileName, count, l):

    # **** open the specified text file ****
    try:
        stream = open(fileName, "at")
    except OSError:
        print(f"open fileName ==>{fileName}<== exception OSError")
        os._exit(-1)
    except:
        print(f"open fileName ==>{fileName}<== could not open")
        os._exit(-1)

    # **** write a set of lines ****
    for i in range(count):
        stream.write(f"this is line {i} in this file\n")

    # **** write the contents of the specified list ****
    stream.writelines(' '.join(l))
 
    # **** flush the stream (not needed in this case) ****
    stream.flush()

    # **** flush and close the file ****
    stream.close()


# **** read the contents of the specified file ****
fileName = 'c:\\Temp\\README.txt'
read_file(fileName)

# **** name of file to write ****
fileName = "c:\\Temp\\WRITEME.txt"

# **** check if the speficied file exists ****
exists = os.path.exists(fileName)
print(f"exists: {exists} fileName ==>{fileName}<==")

# **** remove file (if present) ****
if exists == True:
    os.remove(fileName)

# **** write the specified number of lines and list to the specified file ****
count = 10

list = []
list.append("James")
list.append("Bond")
list.append("007")
list.append("- License to Kill")

write_file(fileName, count, list)