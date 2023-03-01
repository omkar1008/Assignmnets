import os

Files = ['student_comma.dat', 'student_double_semi.dat', 'student_semi.dat']

def main():
    for eachfile in Files:
        print('Data from: ', eachfile)
        if os.path.exists(eachfile):
            with open(eachfile) as ip_file:
                for line in ip_file:
                    line = line.strip()
                    print(line)

        print('\n')
if __name__ == '__main__':
    main()
