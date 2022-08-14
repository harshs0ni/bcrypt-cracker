# Author: Harsh Soni
# Tool: Bcrypt Hash Cracker
# Created on: 10-Oct-2021
# Tested on Python3
# Github: https://github.com/h4r5h5
# Instagram: https://www.instagram.com/h4r5h_h4ck5/
print("""
          -Bcrypt Hash Cracker-
           --------     --------                  
            --------     --------        
             ---------------------     
              ---------------------   
               --------     --------     
                --------     --------   
                 -Bcrypt Hash Cracker-
                 
                 
                 """)
import sys
try:
    import bcrypt
    import signal
    import progressbar
    import getopt
except ModuleNotFoundError:
    print("Python Module Required: Bcrypt, signal, progressbar, getopt")
    sys.exit(0)
def signal_handler(sig, frame):
    print('''

^C

----------------------------------------------------------
        Tool Terminated - Bcrypt Hash Cracker
----------------------------------------------------------
    ''')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

argv = sys.argv[1:]

try:
    
    opts, args = getopt.getopt(argv, 'h:w:', ['foperand', 'soperand'])
    
    for opt, arg in opts:
        try:
            hashed_bcrypt = opts[0][1]
            wordlist_path = opts[1][1]
        except IndexError:
            print (' usage: bcrypt_cracker.py -h <hash> -w <wordlist-path>')
            print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
            sys.exit(0)
        
except getopt.GetoptError:
    print (' usage: bcrypt_cracker.py -h <hash> -w <wordlist-path>')
    print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
    sys.exit(2)
try:
    hashed_bcrypt
    wordlist_path
except NameError:
    print (' usage: bcrypt_cracker.py -h <hash> -w <wordlist-path>')
    print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
    sys.exit(2)
else:
    
    hash = hashed_bcrypt.encode('utf8')
    wordlist=wordlist_path
    try:
        n_words = len(list(open(wordlist, "r", encoding="utf-8")))
    except FileNotFoundError:
        print ('\n Error: Incorrect Wordlist Path')
        print (' usage: bcrypt_cracker.py -h <hash> -w <wordlist-path>')
        print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
        sys.exit(2)
    else:
       
        print(" Total passwords:", n_words)
        print(" Setting up \n Wait......")
        wordlists_pass = open(wordlist, "r", encoding="utf-8").readlines()
        wordlists_pass = wordlists_pass
        new_list=[]
        for k in wordlists_pass:
            wordlists_pass_replace = k.encode('utf8')
            new_list.append(wordlists_pass_replace)
        print(" Starting the Attack")
        total_len=int(len(new_list)-1)
        def animated_marker():
            widgets = [' Craking Hash: ', progressbar.AnimatedMarker(), '                          Total:[', progressbar.SimpleProgress(), ']',  ' (', progressbar.ETA(), ') ',]
            bar = progressbar.ProgressBar(widgets=widgets, maxval=len(new_list)).start()
            for i in range(0, len(new_list)):
                try:
                    isSamePassword = bcrypt.checkpw(new_list[i],hash)
                except ValueError:
                    print("\n Invaild Hash: Hash Should be Bcrypt")
                    print(" Try: Adding Apostrophe Before and after Hash \n Example: -h '$2a$04$TXuWvK7tYFfMVk7yqVuZ8.Z0M3VTYU10yFMrwKLb0x.jH8fljSZVO' -w xyz.txt")
                    sys.exit(0)
                if isSamePassword == False:
                    bar.update(i)
                    if i == total_len:
                        print("\n\n Sorry:Unable to Crack Hash with This Wordlist")
                        print(" Tip: Try Another Wordlist")
                        print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
                        
                else:
                    cracked_password = new_list[i].decode()
                    print("\n Yooo! Hash cracked \n Password is:",cracked_password)
                    print('''
----------------------------------------------------------
                 Bcrypt Hash Cracker
----------------------------------------------------------''')
                    sys.exit(0)
                    break


        animated_marker()
