
def capitalization(String):
    length = len(String)
    final = ""

    for i in range(length):
        if i == 0:

            if ord("a") <= ord(String[i]) <= ord("z"):
                new = ord(String[i]) - 32
                final += chr(new)

            else:
                final += String[i]

        elif i > 2 and (String[i - 2] == "?" or String[i - 2] == "." or String[i - 2] == "!"):
            if ord("a") <= ord(String[i]) <= ord("z"):
                new = ord(String[i]) - 32
                final += chr(new)
            else:
                final += String[i]

        elif String[i] == "i":
            if String[i - 1] == " " and (
                    String[i + 1] == " " or String[i + 1] == "." or String[i + 1] == "?" or String[i + 1] == "!"):
                new = ord(String[i]) - 32
                final += chr(new)

            else:
                final += String[i]

        else:
            if ord("A") <= ord(String[i]) <= ord("Z"):
                new = ord(String[i]) + 32
                final += chr(new)
            else:
                final += String[i]

    return final


str = input("Enter the string: ")

print(capitalization(str))