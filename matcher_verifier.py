def gale_shapley(free_hospitals, hospital_preferences, student_preferences, matches):
    
    unmatched_hospitals = []
    
    for h in free_hospitals:
        # h is 1 to n
        for a in hospital_preferences[h - 1]:
            # a is 1 to n
            if a not in matches.keys():
                matches[a] = h
                break

            student_list = student_preferences[int(a) - 1]
            if student_list.index(str(h)) < student_list.index(str(matches[a])):
                # IF a prefers h to her/his current assignment h' THEN assign a and h and h' has a slot free
                # Look at student's preference list and see if student prefers h over h' (index of h < index of h')
                unmatched_hospitals.append(matches[a])
                matches[a] = h
                break

    return unmatched_hospitals

# read the matching
def read_matching(match_file):
    matches = {}
    with open(match_file) as f:
        for line in f:
            h, s = line.split()
            matches[int(h)] = s
    return matches

def main():
    mode = input('Type 1 for matching engine or 2 for verifier: ')
    
    if mode == '1':
        
        # Read input
        file = input('Type name of input file: ')
        with open(file) as f_in:
            # Read first line of input file
            first_line = f_in.readline()
            try:
                if not first_line:
                    print('File is empty')
                    return
                n = int(first_line)     # n hospitals and n students
            except:
                print('First line of input file is invalid')
                return
            
            hospital_preferences = []       # list of (tuples of strings that have values of 1 to n)
            for _ in range(n):
                input_line = f_in.readline()
                hospital_preferences.append(list(input_line.split()))
            student_preferences = []        # list of (tuples of strings that have values of 1 to n)
            for _ in range(n):
                input_line = f_in.readline()
                student_preferences.append(list(input_line.split()))     


        # Matching algorithm
        
        matches = {}
        # Key:      (student)  -> string
        # Value:    (hospital) -> int
        
        unmatched_hospitals = list(range(1, n+1))
        while unmatched_hospitals:
            unmatched_hospitals = gale_shapley(unmatched_hospitals, hospital_preferences, student_preferences, matches)

        with open('output.txt', 'w', encoding="utf-8") as f_out:
            for key, value in sorted(matches.items(), key=lambda item: item[1]):
                f_out.write(f'{value} {key}\n')
        
        print('Output of matching engine was written to output.txt')

        
    elif mode == '2':
        print('Verifier')
    else:
        print('Invalid input')
            

if __name__ == '__main__':
    main()