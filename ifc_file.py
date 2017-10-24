import os

def eth(args):
    if (args == ""):
        ethInfo = os.popen('ifconfig eth0')
        ethDone = ethInfo.read()
        print(ethDone)
    else:
        newEth = os.popen('ifconfig' + args)
        newEthDone = newEth.read()
        print(newEthDone)