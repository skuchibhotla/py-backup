students = []


def get_students_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase = student["name"].title()
    return student_titlecase


def print_students_titlecase():
    student_titlecase = get_students_titlecase()
    print(student_titlecase)


# def add_student(name, student_id = 332):
def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)


# def var_args(name, *args):
#     print(name)
#     print(args)

# def var_kwargs(name, **kwargs):
#     print(name)
#     print(kwargs["description"], kwargs["feedback"])

# student_list = get_students_titlecase()

# print_student_tilecase()

# add_student("Mark", 332)

# var_args("Mark", "Loves Python", None, "Hello", True)

# var_kwargs(name = "Mark", description = "Loves Python", feedback = None, pluralsight_subscriber = True)