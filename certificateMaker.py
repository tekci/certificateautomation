from methods import createCertificate
import os


nameslist = []

userinput = ""

def getExistingProjects():
    if not os.path.exists("C:/Users/user/Desktop/certificateautomation/projectlist.txt"):
        file1 = open("C:/Users/user/Desktop/certificateautomation/projectlist.txt", mode='w')
    else:
        file1 = open("C:/Users/user/Desktop/certificateautomation/projectlist.txt", 'r')
    # Read file, make a list of lists, each sub list containing the name at index 0 and path at index 1
    Lines = file1.readlines()
    projects = []
    for project in Lines:
        projects.append(project.split('-'))
    
    return projects

def makeCerts(config, path):
    userinput = input("Enter names separated by a comma: ")
    for name in userinput.split(','):
        if name != '' or name == ' ':
            nameslist.append(name)
    while len(nameslist) != 0:
        createCertificate(nameslist[0], config, path)
        nameslist.remove(nameslist[0])

def launchProject(path):
    Continue = True
    userinput = ""
    while Continue:
        print("Make a selection:")
        print("1. Generate Certificates")
        print("2. Change Settings")
        print("3. Exit")
        userinput = input()
        if userinput.strip() == '1':
            if not os.path.exists(path + "/config.txt"):
                print("error, config file not found")
                Continue = False
            else:
                file1 = open(path + "/config.txt", 'r')
                Lines = file1.readlines()
                makeCerts(Lines, path)
        elif userinput.strip() == '2':
            pass
        elif userinput.strip() == '3':
            Continue = False
        else:
            print("invalid selection, try again")

mainContinue = True
while mainContinue:
    print("Make a selection:")
    print("1. Open Existing Project")
    print("2. Make New Project")
    print("3. Exit")
    userinput = input()
    if userinput.strip() == '1':
        projects = getExistingProjects()
        if len(projects) > 0:
            print("Chose a Project (type exit to exit): ")
            for i in range(1, len(projects)+1):
                print (f"{i}. {projects[i-1][0]} | {projects[i-1][1]}")
            userinput = input()
            if userinput.isnumeric() and int(userinput) > 0 and int(userinput) <= len(projects):
                launchProject(projects[int(userinput)-1][1])
            else:
                if userinput != 'exit':
                    print("invalid selection")
        else:
            print("No exisitng projects found")
    elif userinput.strip() == '2':
        pass
    elif userinput.strip() == '3':
        mainContinue = False
    else:
        print("!Invalid Selection!")


