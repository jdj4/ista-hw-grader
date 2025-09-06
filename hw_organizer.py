import os, re, sys, shutil

'''
PATHS = {
    'hw1': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW1/Grading',
    'hw2': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW2/Grading',
    'hw3': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW3/Grading',
    'hw4': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW4/Grading',
    'hw5': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW5/Grading',
    'hw6': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW6/Grading',
    'hw7': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW7/Grading',
    'hw8': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Homework/HW8/Grading',
    'final': '/home/jpc/Documents/5 - Fall 2024/ISTA 131 SL/Final Project',
}
'''

# Files to explicitly exclude from any processing
EXCL = []

def get_files(filenames: list[str]) -> (list[str], list[str], list[str]):
    file_data = ' '.join(filenames)
    pattern = re.compile(r"\b([a-zA-Z'-]+(?: [a-zA-Z'-]+){1,2})(?=- )\b")
    names = pattern.findall(file_data)
    submissions = []
    for filename in filenames:
        for name in names:
            if name in filename and filename.endswith('.py'):
                submissions.append(filename)
    data = [fname for fname in filenames if fname not in submissions and \
        not fname.endswith('.zip')]
    return submissions, data, names

def move_files(
    hw: str,
    submissions: list[str],
    data: list[str],
    names: list[str],
) -> None:
    for name in names:
        try:
            os.mkdir(name)
        except FileExistsError:
            continue
        for submission in submissions:
            if name in submission:
                shutil.move(submission, name)
                os.chdir(name)
                os.rename(submission, hw + '.py')
                os.chdir('..')
    for name in names:
        for filename in data:
            shutil.copy(filename, name)
    for filename in data:
        os.remove(filename)

def main() -> None:
    hw = input('Which homework is this? (hw0, hw1, hw2, etc.): ')
    zipfile = input('Enter name of submissions zip file: ')
    os.system(f"unzip '{zipfile}'")
    if 'index.html' in os.listdir():
        os.remove('index.html')
    filenames = [fname for fname in os.listdir() if fname not in EXCL]
    submissions, data, names = get_files(filenames)
    move_files(hw, submissions, data, names)
    
if __name__ == '__main__':
    main()
