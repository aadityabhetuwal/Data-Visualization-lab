def alNumToAlpha(str):
    num = ""

    for i in str:
        if i.isdigit():
            num = i + num
    
    return num


print(alNumToAlpha("2001+3"))