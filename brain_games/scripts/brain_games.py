import prompt

def main():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

if __name__ == '__main__':
    main()