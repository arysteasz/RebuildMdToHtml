import re
import glob,os



class ReadTitleFromPath():

    def find_title(self, filepath):

        lines = []
        line_of_title = []

        with open(filepath, "rt", errors='ignore') as infile:

            for line in infile:
                lines.append(line)  # arrays of text lines
                line = line.rstrip('\n')

            title_expression = re.compile('title')

            for i in range(0, len(lines), 1):
                if re.findall(title_expression, lines[i]):
                    line_of_title.append(i)
                    break

        title = lines[line_of_title[0]]  # the title is in first line which is recognized

        file_title = title[7:(len(title) - 1)]

        del lines[:]

        print(file_title)

        return file_title
