def mdc(a,b):
    if a==b:
        return a
    else:
        if a<b:
            return mdc(a,b-a)
        else:
            return mdc(b,a-b)
print(mdc(int(input()),int(input())))