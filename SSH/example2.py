import paramiko, os

host = "192.168.1.20"
port = 22
username = "pi"
password = "raspberry"

# Connect to Android Device
print 'Start Connexion...'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=username, password=password)
sftp = ssh.open_sftp()
print 'Connected.'

sftp.get('/home/pi/FTP/test.txt', '/home/pi/Piathlon/SSH/test.txt')

# End Script
sftp.close()
ssh.close()
