import numpy as np

# 4x4 matrix: rows=students, cols=subjects (Math, Science, English, History)
student_scores = np.array([
    [85, 90, 78, 92],
    [72, 68, 80, 75],
    [91, 88, 95, 89],
    [60, 74, 65, 70]
])

subjects = ['Math', 'Science', 'English', 'History']

print("Student Scores (4 students x 4 subjects):")
print(student_scores)

# Average score per subject (column-wise mean)
avg_scores = np.mean(student_scores, axis=0)
print("\nAverage score per subject:")
for subj, avg in zip(subjects, avg_scores):
    print(f"  {subj}: {avg:.2f}")

# Subject with highest average
best_idx = np.argmax(avg_scores)
print(f"\nSubject with highest average score: {subjects[best_idx]} ({avg_scores[best_idx]:.2f})")
