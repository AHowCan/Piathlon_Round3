from ftplib import FTP

#domain name or server ip:
ftp = FTP('192.168.1.20')
ftp.login(user='upload', passwd = 'ftp')

def grabFile():

    filename = 'test.txt'

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()

grabFile()
