def main():
    mode = input('Type 1 for matching engine or 2 for verifier: ')
    
    if mode == '1':
        # Read input
        file = input('Type name of input file: ')
        with open(file) as f:
            # Read first line of input file
            first_line = f.readline()
            try:
                if not first_line:
                    print('File is empty')
                    return
                n = int(first_line)     # n hospitals and n students
            except:
                print('First line of input file is invalid')
                return
            # print(f.read())
            
            hospital_preferences = []
            for _ in range(n):
                input_line = f.readline()
                hospital_preferences.append(tuple(input_line.split()))
            student_preferences = []
            for _ in range(n):
                input_line = f.readline()
                student_preferences.append(tuple(input_line.split()))
        
        print(f'{n} hospitals')
        print(hospital_preferences)
        print(student_preferences)

    elif mode == '2':
        print('Verifier')
    else:
        print('Invalid input')
            

if __name__ == '__main__':
    main()