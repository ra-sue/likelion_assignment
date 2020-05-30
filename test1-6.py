my_dict = {"이종훈": "010-6355-xxxx"}

i = input("찾고자 하는 사람을 입력하시오.")

if i in my_dict.keys():
    print(my_dict[i])
else:
    print('응 없어~')
