import os
import datetime
# Attributes - f_name, file_size, file_contents, no_of_lines, no_of_characters, most_recent_modification
class FileUtilManger:

         def __init__(self, f_name):
             self.f_name = f_name
             self.file_size = os.path.getsize(f_name)
             self.most_recent_modification = datetime.datetime.fromtimestamp(os.path.getmtime(f_name))
             self.file_contents = self.filecontents()
             self.no_of_lines = self.get_no_of_lines()
             self.no_of_characters = self.get_characters()

         def FileDetails(self):
            print('File Name', self.f_name, '\n')
            print('File Size', self.file_size, '\n')
            print('Recent Modification', self.most_recent_modification, '\n')
            print('File Contents', self.file_contents, '\n')
            print('Number of Lines', self.no_of_lines, '\n')
            print('Number of characters', self.no_of_characters, '\n')


         def filecontents(self):
            content = ''
            if os.path.exists(self.f_name):
                with open(self.f_name) as ip_file:
                    for eachline in ip_file:
                        content = content + eachline

            return content

         def get_no_of_lines(self):
            line = 0
            if os.path.exists(self.f_name):
                with open(self.f_name) as ip_file:
                    for eachline in ip_file:
                        line += 1
            return line

         def get_characters(self):
            line = 0
            if os.path.exists(self.f_name):
                with open(self.f_name) as ip_file:
                    for eachline in ip_file:
                        line += len(eachline)
            return line

O = FileUtilManger('student.dat')
O.FileDetails()