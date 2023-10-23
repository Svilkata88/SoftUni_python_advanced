def students_credits(*args):
    total_credits = 0
    courses = {}
    for el in args:
        data = el.split('-')
        course_name = data[0]
        credits = float(data[1])
        max_test_points = int(data[2])
        diyan_points = int(data[3])
        proportion_percents = diyan_points / max_test_points
        diyan_credits = credits * proportion_percents
        total_credits += diyan_credits
        if course_name not in courses:
            courses[course_name] = 0
        courses[course_name] += diyan_credits

    result = ''
    if total_credits >= 240:
        result += f'Diyan gets a diploma with {total_credits:.1f} credits.\n'
    else:
        result += f'Diyan needs {240-total_credits:.1f} credits more for a diploma.\n'

    for course, credits in sorted(courses.items(), key=lambda kvp: -kvp[1]):
        result += f'{course} - {credits:.1f}\n'
    return result

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)


