from random import sample
list = []

while True:
    data = input("""Please enter the words you want to create a new story
        (if you are done, please enter the "x" key):""")
    if data == "x" or data == "X":
        list += [data]
        del list[-1]
        shuffled_lists = sample(list, len(list))
        str_lists = " ".join(shuffled_lists)
        print("Your new story is:", str_lists)
        break
    elif data != "x" or data == "X":
        list +=[data]