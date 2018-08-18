import os

def generate(id):
    pwd = input('Please input your password: ')
    salta = 'VZJ4KDICUHPCJEA7' + str(id+1) + 'CRKJ6KZ34WK3SIB3'
    saltb = 'TBJZJREKFRHABNMA' + str(id-1) + 'SU3KANPTYEMPO462'
    hashpwd = hash(salta + pwd + saltb)
    os.system('echo ' + str(hashpwd) + '>passwd/' + str(id) + '.txt')

def auth(id, code):
    pwd = code
    salta = 'VZJ4KDICUHPCJEA7' + str(id+1) + 'CRKJ6KZ34WK3SIB3'
    saltb = 'TBJZJREKFRHABNMA' + str(id-1) + 'SU3KANPTYEMPO462'
    hashpwd = hash(salta + pwd + saltb)
    os.system('echo ' + str(hashpwd) + '>passwd/passwd-temp.txt')
    if os.system('diff passwd/passwd-temp.txt passwd/' + str(id) + '.txt') == 0:
        return True
    else:
        return False

def auth_all(code):
    for i in range(1,len([name for name in os.listdir('passwd/') if os.path.isfile(os.path.join('passwd/', name))])):
        if auth(i, code):
            return i
    return -2
