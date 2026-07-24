# ==========================================
# SCHOOL LOGIN SYSTEM
# ==========================================

#INPUT
# Required Structures
users = {
    'jperez':  {
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo':  {
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez':  {
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez':  {
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc':  {
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam':  {
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo':  {
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':  {
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}
 
subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)
 
notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}# PROCESS
access_granted = False
current_user = ''

while access_granted == False:
    username = input('Username: ')
    password = input('Password: ')

    if username in users and users[username]['password'] == password:
        access_granted = True
        current_user = username
    else:
        # OUTPUT
        print('Invalid username or password. Please try again.\n')

current_name = users[current_user]['name']
current_role = users[current_user]['role']

# OUTPUT
print('\nWelcome, ' + current_name + ' (' + current_role.capitalize() + ')')
print('=' * 40)

# PROCESS
if current_role == 'student':

    print('Report Card for ' + current_name)
    print('-' * 40)

    passed_subjects = set()

    for subject in subjects:
        grade = grades[current_user][subject]
        print(subject + ': ' + str(grade))

        if grade >= 8.0:
            passed_subjects.add(subject)

    pending_subjects = set(subjects) - passed_subjects

    print('\nPassed subjects: ' + str(passed_subjects))
    print('Pending subjects: ' + str(pending_subjects))

elif current_role == 'teacher':

    print('Student List:')
    print('-' * 40)

    for username in users:
        if users[username]['role'] == 'student':
            print(username.ljust(10) + ' | ' + users[username]['name'])

    continue_grading = True

    while continue_grading == True:
        print()

        student = input('Student username (or type "Exit" to quit): ')

        if student == 'Exit':
            continue_grading = False
        else:
            if student in grades:

                subject = input('Subject: ')

                if subject in subjects:

                    current_grade = grades[student][subject]
                    new_grade = float(input('New grade: '))

                    print('Current grade: ' + str(current_grade))
                    print('New grade: ' + str(new_grade))
                    confirmation = input('Confirm change? (yes/no): ')

                    if confirmation == 'yes':
                        grades[student][subject] = new_grade
                        print('Grade updated.')
                    else:
                        print('Change canceled.')
                else:
                    print('Invalid subject.')
            else:
                print('Student not found.')

elif current_role == 'coordinator':

    print('Teacher List:')
    print('-' * 40)

    for username in users:
        if users[username]['role'] == 'teacher':
            print(username.ljust(10) + ' | ' + users[username]['name'])

    print('\nSubject List:')
    print('-' * 40)

    for subject in subjects:
        print(subject)

    print('\nStudent List with Grades:')
    print('-' * 90)

    header = 'Subject'.ljust(15)
    for username in grades:
        header = header + users[username]['name'].ljust(20)
    print(header)
    print('-' * 90)

    for subject in subjects:
        row = subject.ljust(15)
        for username in grades:
            grade = grades[username][subject]
            grade_text = str(grade)
            if grade < 8.0:
                grade_text = grade_text + ' (F)'
            row = row + grade_text.ljust(20)
        print(row)

else:
    print('Access type not recognized.')
