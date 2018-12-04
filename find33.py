def find33(nums):
    # convert list to string, use comprehension
    # to convert num to str (.join expects str)
    tostring = ''.join(str(e) for e in nums)
    if '33' in tostring:
        return True
    else:
        return False


print(find33([3,3,1]))
print(find33([1,3,1,3]))