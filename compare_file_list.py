file_list_str1 = input("file_list字段字符串1：")
numbers_list1 = file_list_str1[1:-1].split(',')
file_list_str2 = input("file_list字段字符串2：")
numbers_list2 = file_list_str2[1:-1].split(',')
for i in numbers_list1:
    if i in numbers_list2: continue
    else: print(i)