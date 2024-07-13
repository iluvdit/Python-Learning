import os

def print_directory_contents(directory):

    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    # Print the contents of the directory
    print(f"Contents of directory '{directory}':")
    for item in os.listdir(directory):
        print(item)

# Example usage:
directory_path = "/home/kali/Documents/"  
print_directory_contents(directory_path)



# Another Small program for printing directory contents/items

'''
import os

directory_path = '/home/iluvdit/Downloads'

contents = os.listdir(directory_path)

for item in contents:
    print (item)
'''
