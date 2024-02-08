student_scores = {
	"Gabby": [98, 86, 76],
	"Jake": [99, 98, 95],
	"Angel": [96, 85, 80]
}


#gabby_grade = student_score['Gabby']

#print(gabby_grade)

#for grade in gabby_grade:
 	#print(grade + grade)

student_grades = [student_scores["Gabby"],
student_scores["Jake"],
student_scores["Angel"],
]

for student, grade in student_scores.items():
	# for grade in grades:
		print(f'{student}', *grade)
