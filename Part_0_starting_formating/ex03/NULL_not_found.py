
def NULL_not_found(object: any) -> int:
    if object == None:
        print(f"Nothing: {object} {type(object)}")
    elif object != object:
        print(f"Garlic: {object} {type(object)}")
    elif type(object) is bool and object == False:
        print(f"Fake: {object} {type(object)}")
    elif object == 0:
        print(f"Zero: {object} {type(object)}")
    elif object == "":
        print(f"Empty: {object} {type(object)}")

    else:
        print("Type not found")
    return 1

