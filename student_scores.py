student_scores = {
	"Gabby": [98, 86, 76],
	"Jake": [99, 98, 95],
	"Angel": [96, 85, 80] #Iterable
}

# gabby_grades = student_score['Gabby']

# print(gabby_grades)

# for grade in gabby_grades:
#	print(grade + grade)

student_grades = [student_scores["Gabby"],
student_scores["Jake"],
student_scores["Angel"],
]

for student, grade in student_scores. Items():
	# for grade in grades:
	print(f'{student}', *grade)