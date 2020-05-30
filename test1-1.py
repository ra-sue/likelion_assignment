
a = int(input('주민번호 앞자리'))
b = int(input('주민번호 뒷자리'))
aa = a % 10000  # 402
aaa = a // 10000  # 96


birth_month = aa//100  # 4 -> 월을 구했다.
birth_day = aa % 100  # 2 -> 일을 구했다.


#print(f'생일 : {str(a)[2:4]}월 {str(a)[4:6]}일')


# if b // 1000000 % 2 ==1:

first_num = b // 1000000  # 1,2,3,4 중 하나가 나온다

if first_num < 3:
    birth_age = 120-aaa+1  # 96 -> 나이 구하기

elif first_num > 2:
    birth_age = 20-aaa+1

print(f'나이 : {birth_age}살')
print(f'생일 : {birth_month}월 {birth_day}일')

if first_num in [1, 3]:  # 남자
    print('남자')
elif first_num in [2, 4] == 0:  # 여자
    print('여자')


# if int(str(b)[0]) % 2 == 1:  # 남자
#    print('성별 : 남성')
# else:  # 여자
#    print('성별 : 여성')
# print()
