x = 1
y = 100
while x < y:
    x +=1
    output = ""
    if x % 3 == 0:
        output += "fizz"
    if x % 5 == 0:
        output += "buzz"
    if output == "":
        output = str(x)
    print(output)

    # if result_mod_3 == 0 and x % 5 == 0:
    #     print ("fizzbuzz")
    #     continue
    # if result_mod_3 == 0:
    #     print ("fizz")
    # elif  x% 5 == 0:
    #     print ("buzz")
    # elif x %3 >0 and x %5 >0:
    #     print (x)






