#Task1
lists = [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    x = i+1
    lists[i] = x
print(lists)

#task3
all_inf = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '4b', 'scores': [2,3,4,5,5]} ]
students_scores1 = [3,4,4,5,2]
students_scores2 = [2,3,4,5,5]
scores_sum1 = 0
scores_sum2 = 0
for score1 in students_scores1:
	scores_sum1 += score1
	scores_avg1 = scores_sum1 / len(students_scores1)
print(f"Средняя оценка 4 a {scores_avg1}")
for score2 in students_scores2:
	scores_sum2 += score2
	scores_avg2 = scores_sum2 / len(students_scores2)
print(f"Средняя оценка 4 b {scores_avg2}")
school_avg= (scores_avg1 + scores_avg2)/2
print(f"Средняя школы  {school_avg}")

#task2
a = 'kja'
print(a)
for a in "kja":
    print(a.upper())