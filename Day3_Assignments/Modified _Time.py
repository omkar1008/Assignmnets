import os
import datetime

def main():
    file_name = 'student.dat'
    if os.path.exists(file_name):
        with open(file_name) as ip_file:
            time = os.path.getmtime(file_name)
            modifieded = datetime.datetime.fromtimestamp(time)
            print(modifieded)

if __name__ == '__main__':
    main()
