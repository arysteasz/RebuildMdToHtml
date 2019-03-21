import glob,os
import os.path
import re
import json
import markdown2
from markdown2 import Markdown



class RebuildMdFileToHtml():

    def convert_mdfile_to_html(self,file_path, output_path):

        lines = []
        dywizers = []
        line_of_title = []



        #output_path = '/home/lech/Desktop/PythonSkrypt_1/work'
        #output_path = work_path

        with open(file_path, "rt", errors='ignore') as infile:
            for line in infile:
                lines.append(line)  # arrays of text lines
                line = line.rstrip('\n')

            lines_length = len(lines)  # length of the text array

            dywizer_x3_expression = re.compile('---')
            title_expression = re.compile('title')

            for i in range(0, lines_length, 1):

                if re.findall(dywizer_x3_expression, lines[i]):
                    dywizers.append(i)

                if re.findall(title_expression, lines[i]):
                    line_of_title.append(i)

                old_text = lines[i]
                new_text = old_text.replace('/guides/', 'https://cumulocity.com/guides/')
                lines[i] = new_text

            title = lines[line_of_title[0]]  # the title is two lines above

            newfiletitle = title[7:(len(title) - 1)]

            dywizers_length = len(dywizers)

        with open(os.path.join(output_path, '{}.md'.format(newfiletitle)),
                  mode='w') as md_file:

                for f in range((dywizers[dywizers_length -1]) +1 , lines_length, 1):
                    md_file.write(lines[f])

        markdowner = Markdown()


        with open(os.path.join(output_path, '{}.html'.format(newfiletitle)),
                  mode='w') as html_file:

                for f in range((dywizers[dywizers_length -1]) +1 , lines_length, 1):
                    html_file.write(markdowner.convert(lines[f]))

        del lines[:]
        del dywizers[:]
        del line_of_title[:]


        return file_path, newfiletitle
