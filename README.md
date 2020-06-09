About
=======

pdf2png converts PDF files to various image formats with a simple graphical interface based on python, using ghostscript.

It supports up to 4 different image extensions like PNG, JPEG, BMP and TIFF.

## How To

Increasing or decreasing the resolution will change the image quality.

Once given correct numbers for the From page and To page, click on Select PDF file to open a dialog window to browse and select the wanted PDF book, and click on Convert to convert the selected pages.

It would convert the pdf and output the image(s) in the same directory where the pdf resides.

## Credits

Forked from WifiExtender's <a href="https://github.com/wifiextender/pdf2png">pdf2png</a>, so Thanks to him :)

This has minor chnages from his version like no tray icon and no over-riding of the system theme.

## Requirements

* python 3
* ghostscript
* python-gobject (for debian its python-gi)

## Installation

(as root)
~~~~
 # make install
~~~~
(or)
~~~~
 $ sudo make install
~~~~

## Usage

It takes a list of pdf as input and converts them to png. It converts only the first page of the pdf since the script has been adapted to convert output of R markdown.

`./pdf2png example1.pdf example2.pdf ...`

*This script has been made specifically to convert pdf charts exported by Rmarkdown when using knit to compile a pdf.



