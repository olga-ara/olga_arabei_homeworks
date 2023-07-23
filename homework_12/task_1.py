# 1)Файл содержит числа и буквы. Каждый записан в отдельной строке. Нужно считать содержимое в список так,
# чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длины.
# list_1.sort()
# print(list_1)
# list_2 = []   #  список по длине
with open('task_1.txt', 'r') as file:
    print(file.read())

# list_num = []  # числа по возрастанию, слова по возрастанию длины
# list_str = []  # список строк
# for i in list_num:
#     if type(i) == int:
#         list_num.append(i)
#     else:
#         list_str.append(i)
# print(list_num.sort())
# print(list_str)

# 1. Файл содержит числа и буквы. Каждый записан в отдельной строке. Нужно считать содержимое в список так, чтобы
# сначала шли числа по возрастанию, а потом слова по возрастанию их длины.

    # file1 = open("hw_task1.txt", 'r')
    # list1 = []
    # list2 = []
    # def is_int(str):
    #     try:
    #         int(str)
    #         return True
    #     except ValueError:
    #         return False
    #
    # while True:
    #     line = file1.readline().strip()
    #     if is_int(line):
    #         list1.append(int(line))
    #         list1.sort()
    #     else:
    #         list2.append(line)
    #         list2.sort(key=len)
    #
    #     if not line:
    #         break
    #
    # file1.close
    # list2.pop(0)
    # print(list1+list2)




