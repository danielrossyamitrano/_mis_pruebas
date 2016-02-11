from core.status import *
from core import Leaf

# def _walk(self, target):
    # if target == 'door':
        # print('reached', target, Success)
        # return Success

    # elif target == 'window':
        # print('reached', target, Success)
        # return Success

class _walk(Leaf):
    def __init__(self,*args,**kwargs):
        super().__init__(*args)
    
    def process(self,target):
        if target == 'door':
            print('reached', target, Success)
            return Success

        elif target == 'window':
            print('reached', target, Success)
            return Success

def _close(self, openable):
    print('closing', openable, Success)
    return Success


def _open1(self, openable):
    print('opening', openable, Success)
    return Success

def _open2(self, openable):
    print('opening', openable, Success)
    return Success
    
def _smash(self, openable):
    print('smashing', openable, Success)
    return Success


def _unlock(self, openable):
    print('unlocking', openable, Success)
    return Success


# leaves específicos del ejemplo 2  
def _getstackfrom(self, door, building):
    print('got stack')
    return Success


def _isnull(self, used_door):
    print('is_null',Failure)
    return Failure


def _popfromstack(self, door):
    status = Success
    print('popfromstack',status)
    return status


def _setvariable(self, door, used_door):
    return Success
