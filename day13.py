students_data = [
    {"name": "Emma Johnson", "gpa": 3.45, "major": "Computer Science"},
    {"name": "Liam Chen", "gpa": 4.12, "major": "Physics"},
    {"name": "Olivia Rodriguez", "gpa": 3.89, "major": "Biology"},
    {"name": "Noah Patel", "gpa": 3.78, "major": "Engineering"},
    {"name": "Ava Thompson", "gpa": 4.56, "major": "Mathematics"},
    {"name": "Ethan Williams", "gpa": 3.22, "major": "Chemistry"},
    {"name": "Sophia Kumar", "gpa": 3.99, "major": "Medicine"},
    {"name": "Mason Garcia", "gpa": 2.67, "major": "Business"},
    {"name": "Isabella Lee", "gpa": 4.31, "major": "Law"},
    {"name": "James Wilson", "gpa": 3.55, "major": "Psychology"},
    {"name": "Mia Davis", "gpa": 2.95, "major": "Economics"},
    {"name": "Benjamin Martinez", "gpa": 4.08, "major": "Finance"},
    {"name": "Charlotte Brown", "gpa": 3.77, "major": "Marketing"},
    {"name": "Lucas Smith", "gpa": 2.43, "major": "Sociology"},
    {"name": "Amelia Taylor", "gpa": 4.25, "major": "Art History"},
    {"name": "Alexander Kim", "gpa": 3.11, "major": "Political Science"},
    {"name": "Harper Jones", "gpa": 3.66, "major": "English"},
    {"name": "William Anderson", "gpa": 4.49, "major": "Architecture"},
    {"name": "Evelyn Moore", "gpa": 2.88, "major": "Music"},
    {"name": "Michael Jackson", "gpa": 3.92, "major": "Drama"},
    {"name": "Grace Turner", "gpa": 3.34, "major": "Philosophy"},
    {"name": "Daniel Clark", "gpa": 4.01, "major": "Statistics"},
    {"name": "Chloe Walker", "gpa": 2.79, "major": "Anthropology"},
    {"name": "Henry Lewis", "gpa": 3.88, "major": "Geology"},
    {"name": "Zoe Hall", "gpa": 4.17, "major": "Astronomy"},
    {"name": "Samuel Young", "gpa": 3.42, "major": "Linguistics"},
    {"name": "Victoria King", "gpa": 2.91, "major": "Journalism"},
    {"name": "David Scott", "gpa": 3.75, "major": "Environmental Science"},
    {"name": "Lily Green", "gpa": 4.33, "major": "Biochemistry"},
    {"name": "Joseph Adams", "gpa": 3.19, "major": "Robotics"},
]


smart_students = [ item["name"] for item in students_data if item.get("gpa") > 3.5]
print("list of tudents with 3.5+ GPA:")
for name in smart_students:
    print(name)
        

