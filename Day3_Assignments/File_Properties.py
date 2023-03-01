import os
import datetime

Files = ['student_comma.dat', 'student_double_semi.dat', 'student_semi.dat']

def main():

    for eachfile in Files:
        count = 0
        numberOfCharacters = 0
        if os.path.exists(eachfile):
            with open(eachfile) as ip_file:
                print("file name:", os.path.basename(eachfile))
                for eachline in ip_file:
                    count += 1
                    numberOfCharacters += len(eachline)
                print('number of lines:', count)
                print('No of characters:', numberOfCharacters)
                print('Size:', os.path.getsize(eachfile), 'bytes')
                print("Modified:", datetime.datetime.fromtimestamp(os.path.getmtime(eachfile)) )

            print('------------------\n')

if __name__ == '__main__':
    main()
