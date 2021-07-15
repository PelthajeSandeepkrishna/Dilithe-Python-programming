foo = [i for i in input() if i != ""]
for i in foo:
    if i in "~!@#$%^&*()_+":
        print("String is not accepted")
        break
else:
    print("String is accepted")
