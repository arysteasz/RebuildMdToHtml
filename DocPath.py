import glob,os




class DocPath():

    def list_md_file_directory(self,data_dir):

        file_path = []
        #data_dir = '/home/lech/Desktop/SzukanieRepozytoriow/c8y-docs/src/render/guides'
        for path, subdirs, files in os.walk(data_dir):
            for name in files:
                filetitle = os.path.join(path, name)
                # print(filetitle)
                if filetitle.endswith('.md'):
                    #print(filepath)
                    file_path.append(filetitle)


        return(file_path)


