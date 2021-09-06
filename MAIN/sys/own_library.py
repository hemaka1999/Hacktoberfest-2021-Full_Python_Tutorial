"""
usage: sub <command>
commands:
status - show status
list - print list
"""
import sys
print(sys.argv[1:])
def check():
    print("status")
    return 0
if sys.argv[1:] == ['status']:
    sys.exit(check())
elif sys.argv[1:] == ['list']:
    print("list")
else:
    print(__doc__.strip())