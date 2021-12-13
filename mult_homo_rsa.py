"""только для чисел, показать гомоморфность RSA по умножению"""
import re

def encryptH(message, file_name = 'public_keys.txt'):
    
    try:
        f_public = open(file_name, 'r')

  
    except FileNotFoundError:
        print('Файл с таким именем не найден')
    else:
        n = int(f_public.readline())
        e = int(f_public.readline())
        f_public.close()

        m = message.split("*")
        mul = 1
    
        en_blocks = []
        for i in range(len(m)):
            tmp = pow(int(m[i]),e,n)
            en_blocks.append(str(tmp))
            mul *= tmp
        

    return  "*".join(en_blocks) + "=" +str(mul % n)
   


def decryptH(message, file_name = 'private_keys.txt'):

    f_private = open(file_name, 'r')
    n = int(f_private.readline())
    d = int(f_private.readline())
    f_private.close()


    pattern = re.compile(r"[*=]")
    c=pattern.split(message)
    d_blocks = []

    for i in range(len(c)):
        tmp = pow(int(c[i]),d,n)
        d_blocks.append(str(tmp))

    dec_msg = "=".join(d_blocks)
    
    return dec_msg.replace("=","*",1)