def square(x):
    return x * x

def  cube(x):
    return x * x * x

def ho_func(func, nums):
    return [func(num) for num in nums]

def main():
    nums = [1,2,3,4,5]

    sq_nums = ho_func(square, nums)
    cb_nums = ho_func(cube, nums)

    print(sq_nums,cb_nums)

main()    