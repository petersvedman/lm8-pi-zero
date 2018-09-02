from time import sleep

PC = 0
SYSCLK = 0
TCYCLE = 0
runcount=0

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

mem = [1,1,2,16,0,0,0,0]
#LDAI 1, ADDAI, 16, NOP, NOP, NOP, NOP

def bus_print():
  pp=[]
  for a in bus :
    if (bus[a]==True):
      pp.append(1)
    else:
      pp.append(0)
  print(pp)

def sig_print():
  print('  ')
  for b in sigs:
    print(b, sigs[b])
  print(' ')

def update_bus(runcount):
  print('   ')
  print('bus update')
  print('   ')
  if (runcount%16):
      sigs['PC_TICK']=True
  if ((runcount-1)%16):
      sigs['PC_TICK']=False

#tgen returns a new tcycle. If mode is set to False the tgen returns a 0, resetting the tcycle.

def tgen(tcyk,mode):
  if (mode == False):
    return 0
  else :
    return tcyk+1

while(bus['_HLT']==True):
  #update the two next lines to read SYSCLK later
  bus['SYSCLK']= not (bus['SYSCLK']); #update this
  sleep(1)  #and this
  # if (bus['SYSCLK']) etc etc
  bus_print()
  sig_print()
  input()
  update_bus(runcount)
  print('PC = ', PC);
  if (sigs['PC_TICK']==True):
    PC+=1
  runcount+=1
  TCYCLE=tgen(TCYCLE, True)
  print(TCYCLE)
