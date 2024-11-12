import sys

def read(fileName):
    try:
        with open(fileName,'r') as f:
            content = f.read()
        return content
    except FileNotFoundError as e:
        sys.exit(f'{fileName} does not exist')


def modifyContent(fileName):
    content = read(fileName)
    if not content: sys.exit(f'{fileName} has no content')
    return content.upper()

def write(fileToCopyFrom,fileToWriteTo):
    content = modifyContent(fileToCopyFrom)
    with open(fileToWriteTo,'w+') as f:
        f.write(content)
    print(f"Content has been successfully written to {fileToWriteTo}")
    
write('t.txt','file.txt')