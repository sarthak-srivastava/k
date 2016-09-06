#! python3
password = {'#put your email address#':'#put your password#'}
import pyperclip,sys
if len(sys.argv)<2:
    print('run the program again with email')
    sys.exit()
account=sys.argv[1]
if account in password:
    pyperclip.copy(password[account])
    print('The password for '+account+' is copied to the clipbord. You can paste it into your password box. :-)')
else:
    print('There is no such account')
    
    
