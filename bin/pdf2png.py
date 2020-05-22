#!/usr/bin/python
import os
import sys
import subprocess

program_icon = "/usr/share/pixmaps/pdf2png.png"

def pdf_to_img(pdffile):

    pdfname, ext = os.path.splitext(pdffile)
    resolution = 200
    if os.path.exists('/usr/bin/gs'):
        arglist = ["gs", "-dBATCH", "-dNOPAUSE", "-dFirstPage={0}".format(1), "-dLastPage={0}".format(1), "-sOutputFile={0}.{1}".format(pdfname, 'png'), "-sDEVICE={0}".format('png16m'),"-r{0}".format(resolution), pdffile]
        sp = subprocess.Popen(args=arglist, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
    else:
        err = 'gs (GhostScript) not available for conversion'
    if err:
        print("error while converting", pdffile)
        return
   

    # Open the directory in which the pdf file and converted images are
    #pdfdir = os.path.dirname(pdffile)
    #subprocess.call(["exo-open", pdfdir])
    x = 1 # input page no. lower value
    y = 1 # input page no. upper value
    z = y - x + 1 # no of pages to be renamed
    e = 'png' # extension of output file
    while y >= x:
        if y == 1:
            break # single (first) page
        else:
            os.system('mv -f "{0}}.{1}"'.format(pdfname, e) + ' "{0}.{1}"'.format(pdfname, e))
        z = z - 1
        y = y - 1

    
if __name__ == '__main__':
    print("\n")
    print("Converting", len(sys.argv)-1, "files\n")
    files = sys.argv[1:]
    for file in files:
        print(file, "...")
        pdf_to_img(file)
