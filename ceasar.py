import string
# import pyperclip
from appJar import gui


def closettc(btn):
    app.hideSubWindow("ttc")

def closectt(btn):
    app.hideSubWindow("ctt")
# def cpy(btn):
#     pyperclip.copy()

def shhow(name):
    app.showSubWindow(name)

def ascii_check(text):
    for i in text:
        if i not in string.ascii_letters:
            return False

        else:
            pass
    return True


def encode(btn):

        shhow("ttc")
        text = app.getEntry("Text").upper()
        # text = app.textBox("Text to Cipher", "Please input Text").upper()
        key = app.getEntry("Key").upper()
        # key = app.textBox("Key", "Please input Key").upper()
        # if(ascii_check(text) or ascii_check(key)):
        #     app.errorBox("Error!", "Please input only Alphabet")
        #     app.setStopFunction(encode)
        #     app.clearEntry("Text")
        #     app.clearEntry("Key")
        #
        #
        #
        app.clearEntry("Text")
        app.clearEntry("Key")

        if len(key) < len(text):
            key *= len(text) // len(key)
            key += key[:len(text) - len(key)]
        if len(key) > len(text):
            key = key[:len(text)]

        i = 0
        cipher = ''
        try:
            while i < len(text):

                keylist = string.ascii_uppercase.index(key[i])
                # print(keylist)
                keylist = string.ascii_uppercase[keylist:] + string.ascii_uppercase[:keylist]
                cipher += keylist[string.ascii_uppercase.index(text[i])]
                i += 1

            app.infoBox("Text to Cipher", "Cipher: " + str(cipher))
            return str(cipher)
        except ValueError:
                app.errorBox("Error!", "Please input only Alphabet")


        # print("Cipher: " + str(cipher))

def decode(btn):
        shhow("ctt")
        cipher = app.getEntry("Cipher T").upper()

        key = app.getEntry("Keys").upper()
        # key = app.textBox("Key", "Please input Key").upper()
        # if(ascii_check(cipher) or ascii_check(key)):
        #     app.errorBox("Error!", "Please input only Alphabet")
        #
        app.clearEntry("Cipher T")
        app.clearEntry("Keys")

        if len(key) < len(cipher):
            key *= len(cipher) // len(key)
            key += key[:len(cipher) - len(key)]
        if len(key) > len(cipher):
            key = key[:len(cipher)]

        i = 0
        text = ''
        try:
            while i < len(cipher):
                keylist = string.ascii_uppercase.index(key[i])
                keylist = string.ascii_uppercase[keylist:] + string.ascii_uppercase[:keylist]
                text += string.ascii_uppercase[keylist.index(cipher[i])]
                i += 1
            app.infoBox("Cipher to Text", "Text: " + str(text))
        except ValueError:
                app.errorBox("Error!", "Please input only Alphabet")


        # print("Plain Text: " + str(text))

if __name__ == "__main__":
    text = ''
    key = ''

    app = gui("Caesar Cipher GUI BY THANAWAT", "500x500")
    # mode = int(input("Enter Number to Choose Mode\nPlain Text to Cipher Text: 1\nCipher Text to Plain Text: 2\nMode: "))
    # cipher(mode)
    app.setSticky("new")
    app.setExpand("both")
    app.setFont(20)
    app.addLabel("Cipher", "Caesar Cipher Encoding and Decoding")

    app.setSticky("n")
    app.addButton("encode", encode)

    app.setSticky("n")
    app.addButton("decode", decode)

    app.addMessage("mess", """This program will make a Cipher code from text
    and also decode a Cipher text into a decoded text""")

    app.startSubWindow("ttc", "Text to Cipher", blocking=True)
    # app.go("ctt")
    app.addLabel("TtC", "Text to Cipher encoder")
    app.addLabelEntry("Text")
    app.addLabelEntry("Key")
    app.addButton("OK", closettc)
    # app.addButton("Copy", cpy)
    app.stopSubWindow()

    app.startSubWindow("ctt", "Cipher to Text", blocking=True)
    # app.go("ctt")
    app.addLabel("CtT", "Cipher to text decoder")
    app.addLabelEntry("Cipher T")
    app.addLabelEntry("Keys")
    app.addButton("OK!", closectt)
    # app.addButton("Copy", cpy)
    app.stopSubWindow()



    # app.ad
    # app.a

    app.go()


#prai sarun chaisutanon
#abcdefghijklmnopqrstuvwxyz
'''
Plaintext:        ATTACKATDAWN
Key:            LEMONLEMONLE
Ciphertext:    LXFOPVEFRNHR
'''
