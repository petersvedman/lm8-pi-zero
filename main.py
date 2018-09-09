from time import sleep

PC = 0
SYSCLK = 0
TCYCLE = 0
runcount=0
NOP = False
IR = []

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
  'MAR_WRITE':False,
  'MDR_READ' :False,
  'MDR_HIGH':False,
  'MDR_LOW':False,
  'MDR_WRITE':False,
  'IR_LOAD':False

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

gpio_map = {
    'SYSCLK' : 'GPIO1',
    'L0' : 'GPIO2',
    'L1' : 'GPIO3',
    'L2' : 'GPIO4',
    'L3' : 'GPIO5',
    'L4' : 'GPIO6',
    'L5' : 'GPIO7',
    'L6' : 'GPIO8',
    'L7' : 'GPIO9',
    '_CLR_RESET' : 'GPIO10',
    '_HLT' : 'GPIO11',
    'PC_TICK' : 'GPIO12',
    '_PC_WRITE' : 'GPIO13',
    'AREG_LOAD' : 'GPIO14',
    'AREG_WRITE' : 'GPIO15'
}

fetch = [['PC_WRITE', 'MAR_LOAD'], ['MDR_READ','PC_TICK'], ['MDR_WRITE', 'IR_LOAD']]

isa = {
'NOP': ['NOP'],
'LDAI': [['PC_WRITE', 'MAR_LOAD'],
        ['MDR_READ','PC_TICK'],
        ['MDR_WRITE','MDR_LOW','AREG_LOAD']],
'LDBI': [['PC_WRITE','MAR_LOAD'],
        ['MDR_READ','PC_TICK'],
        ['MDR_WRITE','MDR_HIGH','BREG_LOAD']],
'LDCI': [['PC_WRITE','MAR_LOAD'],
        ['MDR_READ','PC_TICK'],
        ['MDR_WRITE','MDR_LOW','CREG_LOAD']],
'LDDI': [['PC_WRITE','MAR_LOAD'],
        ['MDR_READ','PC_TICK'],
        ['MDR_WRITE','MDR_HIGH','DREG_LOAD']],
'STA' : [['PC_WRITE','MAR_LOAD'],
        ['MDR_READ', 'PC_TICK'],
        ['MDR_WRITE','MDR_LOW','ALUA_LOAD'],
        ['PC_WRITE','MAR_LOAD'],
        ['MDR_READ', 'PC_TICK'],
        ['MDR_WRITE','MDR_HIGH','ALUOP','ALUB_ZERO','ALUY_WRITE','ALUY_LOW','MAR_LOAD'],
        ['MDR_LOAD','AREG_WRITE']]
}

mem = ['LDAI',8,'STA',0x00,0xFF,'NOP']

#Code section

def tcycle_gen(t):
    """ returns a new tcycle number """
    return t+1

def cuteprint(sig):
    pstr = 'sigs : '
    for a in sig:
        if (sigs[a]==True):
            pstr+=('1')
        else:
            pstr+=('0')
    print(pstr, bus['SYSCLK'])




#execute fetch cycle
for a in fetch:
    for b in a:
        sigs[b] = not sigs[b]
    TCYCLE+=1
    cuteprint(sigs)
    bus['SYSCLK'] = not bus['SYSCLK']
    sleep(1)
    bus['SYSCLK'] = not bus['SYSCLK']
    for b in a:
        sigs[b] = not sigs[b]
    cuteprint(sigs)
print('fetch done')
#load opcode into IR
IR=mem[0]
print(IR)
#execute opcode in IR
for a in isa[IR]:
    for b in a:
        sigs[b] = not sigs[b]
    TCYCLE+=1
    cuteprint(sigs)
    bus['SYSCLK'] = not bus['SYSCLK']
    sleep(1)
    bus['SYSCLK'] = not bus['SYSCLK']
    for b in a:
        sigs[b] = not sigs[b]
    cuteprint(sigs)
