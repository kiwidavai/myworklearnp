def get_summ(one, two, delimiter = "!"):
    one = str(one)
    two = str(two)
    s = one + delimiter + two
    return(s)
    

result = get_summ("learn", "python")
print(result.upper())



