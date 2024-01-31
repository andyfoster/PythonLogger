import os
from datetime import datetime
from dataitem import DataItem

# Initialize variables
channels = ["general"]
unique_id = 0  # Start an ID counter

# Create a directory for channel files if it doesn't exist
if not os.path.exists("channels"):
    os.makedirs("channels")

current_channel = channels[0]

def ensure_channel_exists(channel_name):
    if channel_name not in channels:
        channels.append(channel_name)
        open(f"channels/{channel_name}.txt", "w").close()  # Create a file for the new channel


# Function to update the unique_id to the highest found in the channels
def update_unique_id():
    global unique_id
    highest_id = 0
    for channel in channels:
        try:
            with open(f"channels/{channel}.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    id = int(line.split()[0])  # Assuming the ID is the first element
                    if id > highest_id:
                        highest_id = id
        except FileNotFoundError:
            continue  # If a channel file doesn't exist, move on to the next
    return highest_id


unique_id = update_unique_id()
current_channel = channels[0]

while True:
    line = input("#" + current_channel + ": ")
    print("You entered:", line)

    commands = line.split()
    if commands[0] == "ch" and len(commands) > 1:
        new_channel = commands[1]
        ensure_channel_exists(new_channel)
        current_channel = new_channel
        print(f"Switched to channel: {current_channel}")
        continue

    elif commands[0] == "ls":
        if len(commands) > 1:
            if commands[1] == "-a":
                # show all items in  all files
                for channel in channels:
                    try:
                        with open(f"channels/{channel}.txt", "r") as channel_file:
                            for item in channel_file:
                                print(item.strip())
                    except FileNotFoundError:
                        print(f"Channel file {channel} not found.")
            elif commands[1] == "-c":
                # show all channels
                print("Listing channels...")
                for channel in channels:
                    print(channel)
            elif commands[1] == "-t":
                #         show items in all files today
                for channel in channels:
                    try:
                        with open(f"channels/{channel}.txt", "r") as channel_file:
                            for item in channel_file:
                                if item.split()[1].startswith(datetime.now().strftime('%Y-%m-%d')):
                                    print(item.strip())
                    except FileNotFoundError:
                        print(f"Channel file {channel} not found.")

        # print("Listing channels...")
        # for channel in channels:
        #     print(channel)
        # continue

    if line == "quit":
        print("Exiting...")
        break

    elif line == "list":
        print("Listing items...")
        try:
            with open(f"channels/{current_channel}.txt", "r") as channel_file:
                for item in channel_file:
                    print(item.strip())
        except FileNotFoundError:
            print("No items found.")

    elif line == "remove":
        print("Removing an item...")
        remove_id = input("Enter the item ID to remove: ")
        try:
            with open(f"channels/{current_channel}.txt", "r") as channel_file:
                lines = channel_file.readlines()
            with open(f"channels/{current_channel}.txt", "w") as channel_file:
                for line in lines:
                    if line.split()[0] != remove_id:
                        channel_file.write(line)
            print(f"Item with ID {remove_id} removed.")
        except FileNotFoundError:
            print("Channel file not found.")

    else:
        unique_id += 1  # Increment the ID for each new item
        with open(f"channels/{current_channel}.txt", "a") as channel_file:
            channel_file.write(f"{unique_id} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {line}\n")
        print(f"Item added with ID {unique_id}.")

    # else:
    #     print("Unknown command. Type 'help' for a list of commands.")
