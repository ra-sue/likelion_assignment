grade_list = [60, 40, 30, 50, 25]

a = sum(grade_list) / len(grade_list)
for i in range(len(grade_list)):
    if grade_list[i] > a:
        print(f'{i+1}번째 학생 합격!')
    else:
        print(f'{i+1}번째 학생 불합격!')

print()
