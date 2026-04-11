def uppercase(str):
    for c in str:
        print(chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c, end="")
    print()
