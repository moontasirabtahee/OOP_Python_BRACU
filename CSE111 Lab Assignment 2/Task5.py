def domainSolver(email,domain,oldDomain = "kaaj.com"):
    user = ""
    userDomain = ""
    for i in email:
        if i =="@":
            break
        else:
            user += i

    for i in range(len(user)+1,len(email)):
        userDomain += email[i]
    print(userDomain)
    print(user)
    if userDomain == domain:
        print("Unchanged: "+str(email))
    else:
        result = user+"@"+domain
        print("Changed: " + str(result))





domainSolver('bob@sheba.xyz', 'sheba.xyz')

