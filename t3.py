def longest_word(wlist):
    a=""
    for n in wlist:
        if len(n)>len(a):
            a=n
    return a
print(longest_word(["abcd", "BOY", "python"]))

            





