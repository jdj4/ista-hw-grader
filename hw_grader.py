import os

'''
This is redundant but keeping it just in case. Would need to be updated every
semester.
PATHS = {
    'hw1': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW1/Grading',
    'hw2': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW2/Grading',
    'hw3': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW3/Grading',
    'hw4': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW4/Grading',
    'hw5': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW5/Grading',
    'hw6': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW6/Grading',
    'hw7': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW7/Grading',
    'hw8': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW8/Grading',
}
'''

def is_student_directory(filename: str) -> bool:
    if filename == '__pycache__' or '.' in filename:
        return False
    try:
        os.chdir(filename)
    except NotADirectoryError:
        return False
    os.chdir('..')
    return True

def grade_submission(hw: str, student: str) -> None:
    os.chdir(student)
    print(f'\n{student}')
    os.system(f'python3 {hw}_test.py')
    os.chdir('..')

def main() -> None:
    hw = input('What homework is this? (hw1, hw2, etc.): ')
    student_directories = [fname for fname in os.listdir() if is_student_directory(fname)]
    for student in student_directories:
        grade_submission(hw, student)
    
if __name__ == '__main__':
    main()
