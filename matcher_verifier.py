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

# Read input file
def read_input(input_file, hospital_preferences, student_preferences):
    
    with open(input_file) as f_in:
        # Read first line of input file
        first_line = f_in.readline()
        try:
            if not first_line:
                print('File is empty')
                return -1
            n = int(first_line)     # n hospitals and n students
        except:
            print('First line of input file is invalid')
            return -1
        
        # Initialize hospital_preferences and student_preferences
        for _ in range(n):
            hospital_preferences.append(list(f_in.readline().split()))

        for _ in range(n):
            student_preferences.append(list(f_in.readline().split()))

    return n

# read the matching
def read_matching(match_file):
    matches = {}
    with open(match_file) as f:
        for line in f:
            h, s = line.split()
            matches[int(h)] = s
    return matches

#check fro valid match
def is_valid_matching(matches, n):
    #since mathces is a dictionary it takes care of duplicate hospitals
    if len(matches) != n:
        print("incorrect number of matches")
        return False

    students = list(matches.values())

    #make sure that all hospitals are matched
    for h in range(1, n + 1):
        if h not in matches:
            print(f"hospital {h} unmatched")
            return False

    # set removes duplicates so we can see if duplicate students exist by comparing to n
    if len(set(students)) != n:
        print("duplicate students found matching")
        return False
    return True

def is_stable(matches, hospital_preferences, student_preferences):
    # build reversed matching map so that loop isnt needed for searching
    student_hospital_match = {}
    for h in matches:
        student_hospital_match[matches[h]] = h

    for h in matches:
        current_student = matches[h]
        h_pref = hospital_preferences[h - 1]

        # hospital checks students it prefers more than its current one
        for s in h_pref:
            if s == current_student:
                break

            curr_hospital_student = student_hospital_match[s]
            s_pref = student_preferences[int(s) - 1]

            if s_pref.index(str(h)) < s_pref.index(str(curr_hospital_student)):
                print(f"unstable pair ({h}, {s})")
                return False

    return True


def main():
    
    while True:
        mode = input('Type 1 for matching engine, 2 for verifier, or 3 to exit the program: ')
        
        hospital_preferences = []       # list of (tuples of strings that have values of 1 to n)
        student_preferences = []        # list of (tuples of strings that have values of 1 to n)

        if mode == '1':
            
            # Read input
            input_file = input('Type name of input file: ')
            n = -1
            while n == -1:
                n = read_input(input_file, hospital_preferences, student_preferences)
            
            
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
            # Read  input file of preferences
            input_file = input('Type name of input file: ')
            n = -1
            while n == -1:
                n = read_input(input_file, hospital_preferences, student_preferences)

            # Read output matching file
            match_file = input('Type name of matching output file: ')
            matches = read_matching(match_file)

            # check valid matching
            if not is_valid_matching(matches, n):
                return

            # check stable matching
            if is_stable(matches, hospital_preferences, student_preferences):
                print("Valid & Stable")
        
        elif mode == '3':
            break

        else:
            print('Invalid input')
            

if __name__ == '__main__':
    main()