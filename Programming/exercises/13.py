with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# print(lines[4])


# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1


# def exponent(base, exp):
#     num = exp
#     result = 1
#     while num > 0:
#         result = result * base
#         num = num - 1
#     print(base, "raises to the power of", exp, "is: ", result)

# exponent(5, 4)

print(5**4)

def expo(b,e):
    return b**e

res=expo(5,4)
print(res)