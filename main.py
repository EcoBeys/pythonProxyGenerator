import urllib.request
from sys import *
import urllib3
from os import system as terminal
import requests
from colorama import Fore, Style
import sys
import time
sys.path.insert(0,"./pythonProxyGenerator-master/")
print("""
      _______  _______  _______
     (  ____ )(  ____ )(  ___  )|\     /||\     /|
     | (    )|| (    )|| (   ) |( \   / )( \   / )
     | (____)|| (____)|| |   | | \ (_) /  \ (_) /
     |  _____)|     __)| |   | |  ) _ (    \   /
     | (      | (\ (   | |   | | / ( ) \    ) (
     | )      | ) \ \__| (___) |( /   \ )   | |
     |/       |/   \__/(_______)|/     \|   \_/
        
% Kodlayan Kişi: Efe İnanç
% Düzenleyen Kişi: Enes Cört
% Python Version:3.8.5                        
""")
count = input("Oluşturulacak Proxy Sayısı: ")
proxy_api = "https://www.proxyscan.io/api/proxy?format=txt&type=http"

if __name__ == '__main__':

    i = int(count)

    for x in range(i):
        with urllib.request.urlopen(proxy_api) as url:
            s = url.read()
            proxy = (s.strip().decode("utf-8"))
            print(proxy)
            x = proxy        
            time.sleep(1)
            with open("Proxy.txt", "a") as file:
                        file.write(x +"\n")
            file.close()
        
    else:
        print("ProxyLeriniz Hazır!")
        print("Proxleriniz Başarıyla Dosyaya Kaydedildi")




