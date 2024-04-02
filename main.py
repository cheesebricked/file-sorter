import os
import shutil


def run():
    parent_dir = input("Enter the directory to sort: ")
    if os.path.exists(parent_dir) == False:
        print("ERROR: Directory does not exist.\n")
        run()
    else:
        file_types = set()
        print("\nSorting...")
        
        for file in os.listdir(parent_dir):

            if os.path.isfile(os.path.join(parent_dir, file)):
                file_extension = os.path.splitext(file)[1]
                path_name = file_extension[1:]  # move here

                if path_name in file_types:
                    source = os.path.join(parent_dir, file)
                    destination = os.path.join(parent_dir, path_name, file)
                    shutil.move(source, destination)
                else:
                    file_types.add(path_name)
                    os.mkdir(os.path.join(parent_dir, path_name))
                    source = os.path.join(parent_dir, file)
                    destination = os.path.join(parent_dir, path_name, file)
                    shutil.move(source, destination)
    print("Done!")

run()