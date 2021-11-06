import os

 
file_name = input("Please write the name of the file to work with:\n")  # Request file name


if os.path.exists(file_name):   # check if file exists
    file = open(file_name)      # open file
    content = file.read()       # save file content to variable
    file.close()                # close file

    new_content = preprocess(content)   # preprocess content for writing to new file

    new_file = open(file_name + '_preprocessed.txt', 'w')   # open preprocessed file and write new content
    new_file.write(new_content)
    new_file.close()

    print("All done!")

else:
    print("The file you entered does not exist!")
