def Multi_or_Sum(num1, num2):
    product = num1 * num2
    # check the product is 1k or less
    if product<=1000:
        return product
    else:
        return num1+num2
res=Multi_or_Sum(20,30)
print("result is ",res)

res=Multi_or_Sum(40,30)
print("result is ",res)
    