# parse.py - txt2pdf

import sys
import os
from fpdf import FPDF
#from fonttools.ttlib import TTFont 
#import fonttools 


#font = ttlib.TTFont('c:/Windows/fonts/webding.ttf')
#font.save('c:/Windows/fonts/webding.ttf')
corpusgenpath = '../corpusgen/'
pdfgenpath = '../pdfgen/'



#get specific corpusgen directory name from commandline (default 'corpus0')
nargs = len(sys.argv) - 1
print(f'nargs = {nargs}')
corpusgenname = 'corpus0'
if nargs > 1:
    print('too many command line args!')
if nargs == 1:
    corpusgenname = sys.argv[1]  
    print(f'read corpusgenname = {corpusgenname} from cmdline')

corpusgenpath += corpusgenname +'/' 
pdfgenpath += corpusgenname + '/'
print(f'reading all text-files in {corpusgenpath}')
print(f'writing all generated pdf-files to {pdfgenpath}')

#create pdfgen directory if needed
if not os.path.exists(pdfgenpath):
    mode = 0o777
    os.mkdir(pdfgenpath, mode)
    #open(pdfgenpath, 'w').close()
    print(f'created directory {pdfgenpath}')




# index of text-files in corpusgenpath
i = 0

for entry in os.listdir(corpusgenpath):
    fd = os.path.join(corpusgenpath, entry)
    #if os.path.isfile(os.path.join(pdfpath, entry)):
    if os.path.isfile(fd):
        basename = os.path.splitext(entry)[0]
        ext = os.path.splitext(entry)[1]
        #print(f'discovered file = {entry} basename = {basename} ext = {ext}')
        if(ext == '.txt'):
            filepath = os.path.join(corpusgenpath, entry)
            print(f'\n*** processing file = {filepath}')
    
    
            # @@@ read text-file
            fd = open(filepath, 'r')
            text = fd.read()
            lines = text.split('\n')
            #print(text)
    

            # @@@ create pdf-file to write to pdfpath_
            pdf = FPDF()

    
            # Add a DejaVu Unicode font (uses UTF-8)
            # Supports more than 200 languages. For a coverage status see:
            # http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt
            #pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
            #pdf.set_font('DejaVu', '', 14)
            pdf.add_font('webding', '', 'webding.ttf', uni=True)
            pdf.set_font('webding', '', 14)

            
            pdf.add_page()
            pdf.set_font('Arial', size=10)

    
            #create cells for each line
            for j in range(len(lines)):
                #pdf.cell(100,5, txt=lines[j], ln=1, align='L')
                pdf.multi_cell(100,5, txt=lines[j], align='L')
    
            # write pdf-file
            target = pdfgenpath + basename + '.pdf'
            print(f'*** writing file = {target}')
            pdf.output(target)
            
    
            # increment text-file index     
            i = i + 1



