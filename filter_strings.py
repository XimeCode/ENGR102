def filter_strings(list,target):
    contains_target=[]
    for i in range(len(list)):
        letters = list[i].split()
        for letters in list[i]:
            if letters in target:
                contains_target.append(list[i])
    return contains_target

targets =filter_strings(["cat","hello","water"],"a")
print(targets)