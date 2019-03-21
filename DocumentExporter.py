from ReadTitleFromPath import ReadTitleFromPath
from RebuildMdFileToHtml import RebuildMdFileToHtml
from DocPath import DocPath
from CheckTitleCreateNew import CheckTitleCreateNew



class DocumnetationExporter(object):
    def __init__(self):
        self.md_file_path = []
        self.emp = CheckTitleCreateNew()
        self.bmp = ReadTitleFromPath()
        self.dmp = RebuildMdFileToHtml()


    def list_md_file (self, working_driectory):
        amp = DocPath()
        self.md_file_path = amp.list_md_file_directory(working_driectory)


    def get_file_work_on_it(self, file_path):
        #for file in range (0, len(file_path), 1):
        docs = []
        for file in range(0, 10, 1):
            #print(file_path[file])
            docs.append(DocumentHolder())
            doc.transform_md_file_to_html(file_path[file],output_path)
            doc.read_title_from_md_file(file_path[file])


        return file_path[file]

    def read_title_from_md_file(self, md_file_path):

        #bmp = ReadTitleFromPath()
        #self.md_file_title = bmp.discover_title(md_file_path)
        return self.bmp.find_title(md_file_path)

    def transform_md_file_to_html(self, md_file_path,output_path):

        #dmp = RebuildMdFileToHtml()

        return self.dmp.convert_mdfile_to_html(md_file_path, output_path)
        #self.transform_md_file_to_html = dmp.convert_mdfile_to_html(md_file_path)

    def create_new_md_file(self,file_path, output_path, new_md_file_title ):

        #emp = CheckTitleCreateNew()

        return self.emp.found_title(file_path, output_path, new_md_file_title )




# methods
doc = DocumnetationExporter()
doc.list_md_file('/home/lech/Desktop/SzukanieRepozytoriow/c8y-docs/src/render/guides')
output_path = '/home/lech/Desktop/PythonSkrypt_1/work'
#new_md_file_title = 'HakunaMatata'
new_md_file_title = 'Device credentials'


print(doc.md_file_path)
file_path = doc.md_file_path

doc.get_file_work_on_it(file_path)
doc.create_new_md_file(file_path,output_path,new_md_file_title)








