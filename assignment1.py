#!/usr/bin/python
# James Donohoe C13452398
# System Integration Assignment 1
# Custom Shell to run, pwd, ifconfig, dt and ud
currentDirectoryPath = ""

from cmd import Cmd
import os, time, getpass, ifc_file


class MyPrompt(Cmd):
    def do_quit(self, args):
        """Quits the program."""
        print("Exiting Shell....")
        raise SystemExit
        
    def do_ls(self, args):
        """Shows files in directory"""
        try:
            if (args==""):
                result = os.listdir(currentDirectoryPath)
                for i in result:
                    print(i)
            else:
                result = os.listdir(args)
                for i in result:
                    print(i)
        except:
            print("Error")
            pass
        
    def do_dt(self, args):
        """Prints Date as day month and year"""
        print(time.strftime("%Y%m%d%H%M%S"))
            
    def do_ifc(self, args):
        """Gets info from ipconfig, if no tail is supplied defaults to displaying ETH0 info."""
        ifc_file.eth(args)

    def getIntialPath(self):
        """Intialises the path for ls"""
        result = os.getcwd()
        global currentDirectoryPath
        currentDirectoryPath = result

    def do_pw(self, args):
        """Shows Current working Directory of script."""
        result = os.getcwd()
        global currentDirectoryPath
        currentDirectoryPath = result
        print(result)
    
    def do_CMD(self, args):
        print('---------------------------------')
        print('--Select the following commands--')
        print('---------------------------------')
        print('pw, dt, ls, quit, ifc, ud')
        print('---------------------------------')
        
	
if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.getIntialPath()
    prompt.prompt = '> '
    prompt.cmdloop('Welcome to My Custom Shell : Type CMD for list of commands')
