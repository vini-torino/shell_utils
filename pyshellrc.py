import getpass 
import sys 

# Check if a program is running as root and exit if get False
# must  import  [ 'getpass', 'sys' ]
def is_root():
    if getpass.getuser() != 'root':
        print('please, run this program as root', file=sys.stderr )
        sys.exit()

