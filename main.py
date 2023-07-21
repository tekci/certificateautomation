from methods import createCertificate


nameslist = []

userinput = ""

while True:
    userinput = input("Enter names separated by a comma: ")
    for name in userinput.split(','):
        if name != '' or name == ' ':
            nameslist.append(name)
    while len(nameslist) != 0:
        createCertificate(nameslist[0])
        nameslist.remove(nameslist[0])
