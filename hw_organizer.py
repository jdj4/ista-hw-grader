import os, re, sys, shutil

# Files to explicitly exclude from any processing
EXCL = []

def get_files(filenames: list[str]) -> (list[str], list[str], list[str]):
    file_data = ' '.join(filenames)
    pattern = re.compile(r"\b([a-zA-Z'-]+(?: [a-zA-Z'-]+){1,3})(?=- )\b")
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
