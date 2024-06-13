text = input("Enter name of the source file: ")
with open("text.txt","r")as file:
    content = file.read()
    place = input("Enter the name of the destination file: ")
    with open(place,"w")as file:
        copy = file.write(content)
        print("copied Successful ")
