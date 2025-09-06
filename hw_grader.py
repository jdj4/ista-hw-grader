import os

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
