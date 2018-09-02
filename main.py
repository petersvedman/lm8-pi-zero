from time import sleep

PC = 0
SYSCLK = 0
TCYCLE = 0
runcount=0
NOP = False

bus = {
  'VCC': True,
  'GND': False,
  'SYSCLK': False,
  'L0':False,
  'L1':False,
  'L2':False,
  'L3':False,
  'L4':False,
  'L5':False,
  'L6':False,
  'L7':False,
  'L8':False,
  'L9':False,
  'L10':False,
  'L11':False,
  'L12':False,
  'L13':False,
  'L14':False,
  'L15':False,
  '_HLT':True,
  '_CLR_RESET':True
}

sigs = {
  'AREG_LOAD': False,
  'AREG_WRITE': False,
  'BREG_LOAD': False,
  'BREG_WRITE':False,
  'PC_TICK':False,
  'PC_LOAD':False,
  'PC_WRITE':False,
  'MAR_LOAD':False,
  'MAR_WRITE':False

}

regs = {
  'AREG' : 0,
  'BREG' : 0,
  'CREG' : 0,
  'DREG' : 0,
  'PC' : 0,
  'IR' : 0,
  'ZREG' : 0,
  'ALPHA' : 0,
  'BETA' : 0,
  'MAR' : 0,
  'MDR' : 0,
  'IN' : 0,
  'OUT' : 0,
  'ZEROFLAG' : False,
  'EQUALITY' : True,
  'CARRYFLAG' : False
}

isa = {
'NOP': ['NOP'],
'FETCH' : [['PC_WRITE', 'MAR_LOAD'],['MDR_READ','PC_TICK'],['MDR_WRITE', 'IR_LOAD']],
'LDAI' : [['PC_WRITE', 'MAR_LOAD'],['MDR_READ','PC_TICK'],['MDR_WRITE','MDR_LOW','AREG_LOAD']],
'LDBI' : [['PC_WRITE','MAR_LOAD'],['MDR_READ','PC_TICK'],['MDR_WRITE','MDR_HIGH','BREG_LOAD']],


}

mem = [1,1,2,16,0,0,0,0]
#LDAI 1, ADDAI, 16, NOP, NOP, NOP, NOP



#tgen returns a new tcycle. If mode is set to False the tgen returns a 0, resetting the tcycle.

def tgen(tcyk,mode):
  if (mode == False):
    return 0
  else :
    return tcyk+1
#run_fetch runs the mechanics of the fetch cycle, advances TCYCLE to 3 and sets up for interpreting the opcode

def run_fetch():
    pass
    #do the fetch cycle


while(bus['_HLT']==True):
    if (TCYCLE==0):
        run_fetch()
    if (regs['IR']==100):
