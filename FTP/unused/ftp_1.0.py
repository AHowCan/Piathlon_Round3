import ftplib
import sys

def gettext(ftp, filename, outfile=None):
  if outfile is None:
    outfile = sys.stdout
  ftp.retrlines("RETR " + filename, lambda s, w=outfile.write: w(s+ "\n")) 

ftp=ftplib.FTP("10.201.234.40")
ftp.login("upload", "ftp")

ftpFile = 'example1.txt'
localfile = open(filename, 'wb')

gettext(ftp, "README")

