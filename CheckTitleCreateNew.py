import json
import glob,os
import re


class CheckTitleCreateNew():

    def found_title(self, file_path, output_path, new_md_file):

        lines = []
        line_of_title = []
        j = 0;


        for file in range(0, len(file_path), 1):

            with open(file_path[file], "rt", errors='ignore') as infile:


                for line in infile:
                    lines.append(line)  # arrays of text lines
                    line = line.rstrip('\n')

                k = len(lines)  # length of the text array

                title_expression = re.compile('title')
                for i in range(0, k, 1):
                    if re.findall(title_expression, lines[i]):
                        line_of_title.append(i)

                title = lines[line_of_title[0]]  # the title is two lines above
                newfiletitle = title[7:(len(title) - 1)]


                if newfiletitle == new_md_file:
                    j = j+1


            del lines[:]
            del line_of_title[:]
            del newfiletitle

        if j == 0:

            result = {
                "year": "2018",
                "month": "08"
            }

            with open(os.path.join(output_path, '{}.md'.format(new_md_file)),
                      mode='w') as md_file:
                json.dump(result, md_file, indent=2)

            print("The new file is created: ")
            print(new_md_file)

        else:
            print("The any new md file wasn't create")

        return None
