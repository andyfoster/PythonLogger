from datetime import datetime, timedelta
import os

channels = ["general"]

# write a text file for each channel and scan the channel folder for files
# if a file is not in the list, add it to the list

# if no data file exists, create one

if not os.path.exists("data.txt"):
    open("data.txt", "w").close()

# datafile = open("data.txt", "wr")

print("LOGGER: \nType 'quit' to exit, 'l' to list all, 't' for today, 'y' for yesterday, 's' + {search term} to search")

print("Enter a message to log it.")

while True:
    # line = input("#" + channels[0] + ": ")
    line = input("LOGGER: ")
    # print("You entered:", line)

    if line == "quit":
        print("Exiting...")
        # exit(0)
        break

    elif line == "l":
        datafile = open("data.txt", "r")
        for line in datafile:
            print(line.strip())

    elif line == "t":
        datafile = open("data.txt", "r")
        today = datetime.now().strftime("%Y-%m-%d")
        for line in datafile:
            if today in line:
                print(line.strip())

    elif line == "y":
        datafile = open("data.txt", "r")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        for line in datafile:
            if yesterday in line:
                print(line.strip())

    # handle s + {search term}, convert all to lower case, don't search the date part
    elif line.startswith("s "):
        datafile = open("data.txt", "r")
        search_term = line[2:].lower()
        for line in datafile:
            if search_term in line.lower():
                print(line.strip())


    else:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("data.txt", "a") as datafile:
            datafile.write(f"{current_time} {line}\n")
