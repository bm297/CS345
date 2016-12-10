import sys  # for command line arguments
import os   # for sys functions

# Step 1: Searchable
def search(name, cwd, file, docID):
    
    # List all the files and directories in cwd
    directories = os.listdir(cwd)   # ['hifidse.py', 'besho']

    # Checks each directory whether file or directory
    for directory in directories:
        # Ignore hidden files, they start with "."
        if(directory[0] == "."):
            continue
        elif(file_check(name, cwd, directory, file, docID)):
            continue
        else:
            directory_check(name, cwd, directory, file, docID)

# Search recusively and write(step1.txt) all directories in found directory
def directory_found(cwd, directory, file, docID):

    directories = os.listdir(cwd)
    for directory in directories:
        if(directory[0] == "."):
            continue
        elif(os.path.isfile(cwd + "/" + directory)):
            docID += 1
            # Check if TXT/TXTN
            if(text_file(directory)):
                # Write file path to step1.txt
                file.write(cwd + "/" + directory + "\tTXT\t{}\n".format(docID))
            else:
                file.write(cwd + "/" + directory + "\tTXTN\t{}\n".format(docID))
        else:
            # Write file path to step1.txt
            file.write(cwd + "/" + directory + "\tDIR\n")
            directory_found(cwd + "/" + directory, directory, file, docID)

def directory_check(name, cwd, directory, file, docID):

    if (directory == name):
        docID += 1
        # Write file path to step1.txt
        file.write(cwd + "/" + directory + "\tDIR\t{}\n".format(docID))
        directory_found(cwd + "/" + directory, directory, file, docID)
    # Search directory recursively 
    else:
        search(name, cwd + "/" + directory, file, docID)

def file_check(name, cwd, directory, file, docID):

    isfile = False
    
    # Check if file
    if(os.path.isfile(cwd + "/" + directory)):
        isfile = True
        # Split filename and check name
        filename = directory.split(".")
         # Check if it's our file
        if(filename[0] == name):
            docID += 1
            # Check if TXT/TXTN
            if(text_file(directory)):
                # Write file path to step1.txt
                file.write(cwd + "/" + directory + "\tTXT\t{}\n".format(docID))
            else:
                file.write(cwd + "/" + directory + "\tTXTN\t{}\n".format(docID))  
    return isfile


# Checks if text-file (.html , .htm , .txt , .cc , .cpp , .c , .h , .java)
def text_file(filename):

    text_extensions = ["html", "htm", "txt", "cc", "cpp", "c", "h", "java"]
    # Split filename and check extension
    extension = filename.split(".")

    # Files without extensions are skipped
    if(len(extension) == 1):
        return False
    elif(extension[1] in text_extensions):
        return True
    else:
        return False

def main():

    # check for two command line (action & name)
    if(len(sys.argv) == 3):
        # Check action type
        if(sys.argv[1].lower() == "searchable"):
            # Create file step1.txt
            file = open("step1.txt", "a")
            cwd = "/home"
            search(sys.argv[2], cwd, file, 0) # 0 is docID
            file.close()
        else:
            print("This is where we check for other commands ")
    else:
        print("You need an action and name in command line. Terminated")

if __name__ == "__main__":
    main()