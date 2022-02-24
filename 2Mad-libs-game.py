from random import sample
list = []  # 定義一個空列表

while True:
    data = input("""Please enter the words you want to create a new story
        (if you are done, please enter the "x" key):""")
    if data == "x" or data == "X":
        lists = list+[data]  # 將輸入資料持續加入至list
        del lists[-1]  # 移除最後輸入的"x"資料
        shuffled_lists = sample(lists, len(lists))  # 將lists中的資料隨機排列
        str_lists = " ".join(shuffled_lists)  # 將list轉換成str，並插入空格
        print("Your new story is:", str_lists)
        break
    elif data != "x" or data == "X":
        list = list+[data]  # 將輸入資料持續加入至list
