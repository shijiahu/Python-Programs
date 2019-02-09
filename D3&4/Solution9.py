import pexpect

passwd = 'j' 
ssh = pexpect.spawn('ssh shijiahu@192.168.1.110 ls')
ssh.expect('Password:')
ssh.sendline(passwd)
ssh.read()
print(str(ssh.before, encoding = "utf-8"))

