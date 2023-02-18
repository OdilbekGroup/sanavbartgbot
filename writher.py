def create_user(id, name, cheklov, count):
    with open("users.txt", "a") as users:
        user = f"{id}-{name}-{cheklov}-{count},\n"
        users.write(user)


def getUser(id):
    user = {}
    with open("users.txt", "r") as users:
        for i in users:
            for j in i.split(",\n"):
                for k in j.split("-"):
                    if k == f"{id}":
                        user["id"] = j.split("-")[0]
                        user["name"] = j.split("-")[1]
                        user["cheklov"] = j.split("-")[2]
                        user["count"] = j.split("-")[3]
    return user



def filtblocks():
    with open("users.txt", "r+") as users:
        usersl = []
        busersl = []
        dusersl = []
        for i in list(users):
            for j in i.split(",\n"):
                if "" == j:
                    continue
                if "yes" in j.split("-"):
                    busersl.append(j.split("-")[0])
                    continue
                else:
                    usersl.append(j.split("-"))
        for i in range(len(usersl)):
            for j in busersl:
                if usersl[i][0] != j:
                    dusersl.append(usersl[i])
        return usersl

def getUsersL():
    satr = ""
    s = 0
    for i in filtblocks():
        s += 1
        satr += f"👤 {s}-foydalanuvchi:\n" \
                f"ism-familya: {i[1]}\n" \
                f"ID: {i[0]}\n" \
                f"Taklif qilinganlar soni: {i[3]}\n\n"
    if satr:
        return satr
    else:
        return "Foydalanuvchilar topilmadi!"

def getides():
    with open("users.txt", 'r') as users:
        usersID = []
        usersl = []
        for i in users:
            for j in i.split(",\n"):
                if "" == j:
                    continue
                else:
                    usersl.append(j.split("-"))
        for i in usersl:
            usersID.append(i[0])
        return usersID

def changecountandsum(id, name, cheklov, count):
    with open("users.txt", "a+") as users:
        usersl = []
        busersl = []
        dusersl = []
        for i in list(users):
            for j in i.split(",\n"):
                if "" == j:
                    continue
                elif id == j.split("-")[0]:
                    continue
                else:
                    usersl.append(j.split("-"))
        for i in range(len(usersl)):
            for j in busersl:
                if usersl[i][0] != j:
                    dusersl.append(usersl[i])
        dusersl.append([id, name, cheklov, str(count)])
        s = 0
        for i in dusersl:
            for j in i:
                s += 1
                if s == 4:
                    users.write(j + ",\n")
                else:
                    users.write(j + "-")







def checkblock(id):
    with open("users.txt", "r") as users:
        for i in list(users):
            for j in i.split(",\n"):
                if "" == j:
                    continue
                if "yes" in j.split("-"):
                    return True
                else:
                    return False

