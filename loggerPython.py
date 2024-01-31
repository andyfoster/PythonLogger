from datetime import datetime
from dataitem import DataItem


def main():
    current_channel = "general"

    while True:
        # Open the file in append and read mode
        with open("data.txt", "a+") as datafile:
            line = input("#" + current_channel + ": ")
            commands = line.split()

            if commands[0] == "q":
                print("Exiting...")
                break

            elif commands[0] == "help":
                print("Commands:")
                print("cd <channel> - change channel")
                print("ls - show items in channel")
                print("ls -a - show all items")
                print("rm {id} - remove item")
                print("{item} - add item to current channel")
                print("find {word} - find word in all channels")
                print("q - quit program")
                print("help - show help")
                continue

            elif commands[0] == "ls":
                if len(commands) > 1 and commands[1] == '-a':
                    print("Listing all items...")
                    datafile.seek(0)
                    for item in datafile:
                        print(item.strip())
                    continue
                else:
                    print('Listing items in channel')
                    datafile.seek(0)
                    for item in datafile:
                        # print(item.strip()[1])
                        # print("1 is " + item.split()[1])
                        if item.split()[1] == current_channel:
                            print(item.strip())
                        continue

            elif commands[0] == "cd" and len(commands) > 1:
                new_channel = commands[1]
                current_channel = new_channel
                # print(f"Switched to channel: {current_channel}")
                continue

            elif commands[0] == "find" and len(commands) > 1:
                query = commands[1]
                datafile.seek(0)
                for item in datafile:
                    if query in item:
                        print(item.strip())

            elif commands[0] == "rm" and len(commands) > 1:
                id_to_remove = commands[1]
                print("Removing item " + id_to_remove)

                datafile.seek(0)
                lines = datafile.readlines()
                datafile.close()

                with open("data.txt", "w") as datafile:
                    removed = False
                    for line in lines:
                        if line.strip().split()[0] == id_to_remove:
                            print("Removing: " + line.strip())
                            removed = True
                            continue
                        datafile.write(line)

                    if not removed:
                        print("ID not found.")

            else:
                item = DataItem(current_channel, datetime.now(), line)
                datafile.write(item.__str__() + "\n")
                datafile.flush()
                continue


if __name__ == '__main__':
    main()
