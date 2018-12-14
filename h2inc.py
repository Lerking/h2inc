import os
from parser import PARSER

class H2INC:
    def __init__(self):
        self.filelist = []
        self.folderlist = []
        self.sourcedir = "/usr/include"
        self.destdir = "/data/include"
        self.filecnt = 0
        self.foldercnt = 0
        
    def srcfilecnt(self, sourcedir):
        ### Return the number of files, ending with '.h', in sourcedir - including subdirectories ###
        for folderName, subfolders, files in os.walk(self.sourcedir):
            for file in files:
                if file.lower().endswith('.h'):
                    self.filecnt += 1
                    self.filelist += [folderName+'/'+file]
        if self.filecnt > 0:
            return True
        else:
            return False
                
    def srcfoldercnt(self, src):
        ### Return the number of folders, if it contains '*.h' files, in sourcedir - including subdirectories ###
        for folderName, subfolders, files in os.walk(src):
            if subfolders:
                for subfolder in subfolders:
                    self.srcfoldercnt(subfolder)
            tempf = [file for file in files if file.lower().endswith('.h')]
            if tempf:
                self.foldercnt = self.foldercnt+1
                self.folderlist += [folderName]
        if self.foldercnt > 0:
            return True
        else:
            return False
        
    def read_file(self, fn):
        parse = PARSER()
        outfile = ''
        inputfile = fn
        passes = 0
        tempfile = []
        templine = []
        encodings = ['utf-8', 'latin-1', 'windows-1250', 'windows-1252', 'ascii',
                    'big5', 'big5hkscs', 'cp037', 'cp273', 'cp424', 'cp437', 'cp500',
                    'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856',
                    'cp857', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp864', 'cp865',
                    'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 'cp950', 'cp1006',
                    'cp1026', 'cp1125', 'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254',
                    'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp65001', 'euc-jp', 'euc-jis-2004',
                    'euc-jisx0213', 'euc-kr', 'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022-jp',
                    'iso2022-jp-1', 'iso2022-jp-2', 'iso2022-jp-2004', 'iso2022-jp-3',
                    'iso2022-jp-ext', 'iso2022-kr', 'iso8859-2', 'iso8859-3', 'iso8859-4',
                    'iso8859-5', 'iso8859-6', 'iso8859-7', 'iso8859-8', 'iso8859-9', 'iso8859-10',
                    'iso8859-11', 'iso8859-13', 'iso8859-14', 'iso8859-15', 'iso8859-16', 'johab',
                    'koi8-r', 'koi8-t', 'koi8-u', 'kz1048', 'mac-cyrillic', 'mac-greek',
                    'mac-iceland', 'mac-latin2', 'mac-roman', 'mac-turkish', 'ptcp154',
                    'shift-jis', 'shift-jis-2004', 'shift-jisx0213', 'utf-32', 'utf-32-be',
                    'utf-32-le', 'utf-16', 'utf-16-be', 'utf-16-le', 'utf-7', 'utf-8-sig']
        for e in encodings:
            try:
                fh = open(fn, 'r', encoding=e)
                fh.readlines()
                fh.seek(0)
            except UnicodeDecodeError:
                print('got unicode error with %s , trying different encoding' % e)
            else:
                break 
        self.tupfile = []
        for lines in fh:
            #outfile = outfile+lines #Initial phase
            self.tupline = []
            analyzed_line = parse.analyzer(lines)
            self.tupfile.append(analyzed_line)
            #self.tupfile.append(lines)
        passes += 1
        fh.close()
        
        #outputfile = os.path.splitext(inputfile)[0]+'.inc'
        #outputfile = str(outputfile).replace(self.sourcedir, self.destdir)
        #print(outputfile)
        #print(os.path.dirname(outputfile))
        #self.write_file(outputfile,outfile)
        
    def write_file(self, fn, data):
        if not os.path.exists(os.path.dirname(fn)):
            try:  
                os.makedirs(os.path.dirname(fn))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        newfile = open(fn, "w")
        newfile.write(data)
        newfile.close()


if __name__ == "__main__":
    app = H2INC()
    if app.srcfilecnt(app.sourcedir) == True:
        print(app.filecnt)
        #print(app.filelist)
        if app.srcfoldercnt(app.sourcedir) == True:
            print(app.foldercnt)
            #print(app.folderlist)
        #for f in app.filelist:
            #app.read_file(f)
        app.read_file("gtk.h") #testfile for comments and header includes
        print(app.tupfile)
