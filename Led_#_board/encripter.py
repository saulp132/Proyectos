text = input("Ingrese la linea de texto que desea encriptar: ")
while True:
    shift = int(input("Ingrese un numero entre 1 y 25: "))
    if shift > 0 and shift < 26 and type(shift) == int:
        break
   
def encripter(text,shift):
    upp_start = 65
    low_start = 97
    encripted_text = ""
    for ch in text:
        limiter_u = ord("[") - ord(ch) 
        
        limiter_l = ord("{") - ord(ch) 
        print(ord(ch),limiter_l,limiter_l - shift)
        if ch.isalpha():
            if ch.isupper():
                if limiter_u > shift:
                    encripted_text += chr(ord(ch)+shift)
                else:
                    encripted_text += chr(upp_start + (shift - limiter_u))
            else:
                if limiter_l > shift :
                    encripted_text += chr(ord(ch)+shift)
                else:
                    encripted_text += chr(low_start + (shift - limiter_l))
        elif ch.isdigit() or ch.isspace:
            encripted_text += ch
    print(encripted_text)

encripter()