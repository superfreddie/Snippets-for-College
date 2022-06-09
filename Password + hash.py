def login():
    entry = False
    print("Please enter your log in details:")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    passwordhash = hash(password)
    file = open('task4.csv', 'r')
    some = file.readlines()
    for count in some:
        login = count.strip().split(',')
        if username == login[0] and passwordhash == [1]:
            print("Correct details, One moment while we let you though!")
            entry = True
            login.append(login[0] + login[1])
    if entry == False:
        print("Incorrect Details, Shutting Down...")
        quit()
    file.close()
