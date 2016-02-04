from lib.status import *

def _walk(self, target):
        if target == 'door':
            print('reached', target, Success)
            return Success

        elif target == 'window':
            print('reached', target, Success)
            return Success


def _close(self, openable):
    print('closing', openable, Success)
    return Success


def _open(self, openable):
    print('opening', openable, Success)
    return Success


def _smash(self, openable):
    print('smashing', openable, Success)
    return Success


def _unlock(self, openable):
    print('unlocking', openable, Success)
    return Success
    
# leaves específicos del ejemplo 2  
def _getstackfrom(self,door,building):
    print('got stack')
    return Success
    
    
def _isnull(self,used_door):
    print('isnull')
    return Success
    
    
def _popfromstack(self,door):
    print('fail')
    return Success
       
    
def _setvariable(self,door,used_door):
    return Success
