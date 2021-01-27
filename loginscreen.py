import sys
from time import sleep


class colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'
    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'


def entry():
    x = """

@@@  @@@   @@@@@@   @@@  @@@   @@@@@@    @@@@@@@  @@@  @@@  
@@@  @@@  @@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@  
@@!  !@@  !@@       @@!  @@@  @@!  @@@  !@@       @@!  !@@  
!@!  @!!  !@!       !@!  @!@  !@!  @!@  !@!       !@!  @!!  
 !@@!@!   !!@@!!    @!@!@!@!  @!@  !@!  !@!       @!@@!@!   
  @!!!     !!@!!!   !!!@!!!!  !@!  !!!  !!!       !!@!!!    
 !: :!!        !:!  !!:  !!!  !!:  !!!  :!!       !!: :!!   
:!:  !:!      !:!   :!:  !:!  :!:  !:!  :!:       :!:  !:!  
 ::  :::  :::: ::   ::   :::  ::::: ::   ::: :::   ::  :::  
 :   ::   :: : :     :   : :   : :  :    :: :: :   :   :::
\n"""

    for c in x:
        print(colors.CRED + c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    y = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n"
    for c in y:
        print(colors.CYELLOW + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    y = "@~~~               SHELL SHOCK TOOL                   ~~~@\n\n"
    for c in y:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    x = "@~~~~                                                ~~~~@\n\n"
    for c in x:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    z = "@~~~~~~          CODED BY    TMRSWRR               ~~~~~~@\n\n"
    for c in z:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    y = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n"
    for c in y:
        print(colors.CYELLOW + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    y = "@@@              WELCOME TO XSHOCK TOOL                @@@\n\n"
    for c in y:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

    y = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n"
    for c in y:
        print(colors.CYELLOW + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
