def gather_credits(number_of_credits, *args):
    # args - tuple consisting of two elements: course name, course credits
    courses = []
    gained_credits = 0
    result = ''
    for course_name, course_credits in args:
        if number_of_credits > 0 and course_name not in courses:
            number_of_credits -= course_credits
            gained_credits += course_credits
            courses.append(course_name)
        if number_of_credits <= 0:
            result += f'Enrollment finished! Maximum credits: {gained_credits}.\n'
            result += f'Courses: '
            result += ', '.join(sorted(courses))
            return result
    else:
        return f'You need to enroll in more courses! You have to gather {number_of_credits} credits more.'

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
