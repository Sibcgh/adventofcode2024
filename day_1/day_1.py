'''
find all distances and sum them up
put into arr 1 and arr2
sum up smallest arr1 with smallest arr2... up to largest for both


lets iterate over nums1 and then put that into an array called ids
create a dict on ids {k=id, val=count}

iterate over nums_2 if nums 2 in dict val += 1

iterate over dict.items()
res += (key*val)
return res
'''

def question_one():
    with open("day_1.txt") as f:
        lines = f.read().split("\n")

    arr1 = []
    arr2 = []
    for line in lines:
        num_1, num_2 = line.split()
        arr1.append(int(num_1))
        arr2.append(int(num_2))

    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    curr_sum = 0
    for i in range(len(arr1)):
        curr_sum += abs(arr1[i] - arr2[i])
    print(curr_sum)

def question_two():
    with open("day_1.txt") as f:
        lines = f.read().split("\n")

    arr1 = []
    arr2 = []
    for line in lines:
        num_1, num_2 = line.split()
        arr1.append(int(num_1))
        arr2.append(int(num_2))


    id_dict = {num: 0 for num in arr1}

    for num in arr2:
        if num in id_dict:
            id_dict[num] += 1

    res = 0
    for k, v in id_dict.items():
        res += (k*v)

    print(res)

question_one()
question_two()

