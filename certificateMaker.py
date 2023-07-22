from methods import createCertificate, select_directory
from projectsettingsgui import Settings
import os

def getExistingProjects():
    if not os.path.exists("projectlist.txt"):
        file1 = open("projectlist.txt", mode='w')
    else:
        file1 = open("projectlist.txt", 'r')
    # Read file, make a list of lists, each sub list containing the name at index 0 and path at index 1
    Lines = file1.readlines()
    projects = []
    for project in Lines:
        if project != '\n':
            projects.append(project.split('-'))
    
    return projects


def writeProjectsToFile(projects):
    if not os.path.exists("projectlist.txt"):
        file1 = open("projectlist.txt", mode='w')
    else:
        file1 = open("projectlist.txt", 'w+')
    print(projects)
    for project in projects:
        try:
            file1.write(project[0] + '-' + project[1].strip() + '\n')
        except Exception:
            pass

def makeCerts(config, path):
    userinput = input("Enter names separated by a comma: ")
    for name in userinput.split(','):
        if name != '' or name == ' ':
            nameslist.append(name)
    while len(nameslist) != 0:
        createCertificate(nameslist[0], config, path)
        nameslist.remove(nameslist[0])

def writeConfigFile(config, path):
    try:
        with open(path, 'w+') as file:
            for item in config:
                file.write(str(item) + '\n')
    except Exception as e:
        print(f"Error writing to the file: {e}")

def launchProject(path):
    Continue = True
    userinput = ""
    file1 = open(path + "/config.txt", 'r')
    config = file1.readlines()
    file1.close()
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
                config = file1.readlines()
                file1.close()
                makeCerts(config, path)
        elif userinput.strip() == '2':
            new_conf = Settings(config)
            if len(new_conf) != 0:
                config = new_conf
                writeConfigFile(config, path + "/config.txt")
        elif userinput.strip() == '3':
            Continue = False
        else:
            print("invalid selection, try again")

# MAIN
nameslist = []
userinput = ""
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
                try:
                    print(f"{i}. {projects[i-1][0]} | {projects[i-1][1]}", end = "")
                except Exception:
                    pass
            print()
            userinput = input()
            if userinput.isnumeric() and int(userinput) > 0 and int(userinput) <= len(projects):
                launchProject(projects[int(userinput)-1][1].strip())
            else:
                if userinput != 'exit':
                    print("invalid selection")
        else:
            print("No exisitng projects found")
    elif userinput.strip() == '2':
        projects = getExistingProjects()
        print(projects)
        project_name = input("Enter new project name: ")
        project_path = select_directory()
        # Create Directory at specified place
        if not os.path.exists(project_path + f'/{project_name}'):
            os.mkdir(project_path + f'/{project_name}')
        # Add config file in created directory
        writeConfigFile(Settings(None), project_path + f'/{project_name}' + '/config.txt')
        # Add project to projects
        projects.append([project_name, str(project_path) + f'/{project_name}'])
        print(projects)
        # Save projects to file
        writeProjectsToFile(projects)


    elif userinput.strip() == '3':
        mainContinue = False
    else:
        print("!Invalid Selection!")


