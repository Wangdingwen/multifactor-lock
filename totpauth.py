import os
import pyotp
import qrcode_terminal

def auth(id, code):
    file_path = 'totpauth/' + str(id) + '.txt'
    with open(file_path) as file_object:
	    contents = file_object.read()
    #totp = pyotp.TOTP(os.popen('cat totpauth/id.txt'))
    totp = pyotp.TOTP(contents)
    return totp.verify(code)

def auth_all(code):
    for i in range(1,len([name for name in os.listdir('totpauth/') if os.path.isfile(os.path.join('totpauth/', name))])):
        if auth(i, code):
            return i
    return -2

def generate(id):
    psecret = pyotp.random_base32()
    file_path = open('totpauth/' + str(id) + '.txt','a')
    file_path.write(psecret)
    #os.system('echo ' + psecret + '>totpauth/' + str(id) + '.txt')
    print('Scan the QR or input this code manually: ' + psecret)
    qrcode_terminal.draw(pyotp.totp.TOTP(psecret).provisioning_uri(str(id)+"@example", issuer_name="Lock"))

#generate(1)
#print(auth(1,input()))
