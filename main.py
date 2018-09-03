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
  'MAR_WRITE':False,
  'MDR_READ' :False,
  'MDR_HIGH':False,
  'MDR_LOW':False,
  'MDR_WRITE':False

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
'FETCH' : [['PC_WRITE', 'MAR_LOAD'],
        ['MDR_READ','PC_TICK'],
        ['MDR_WRITE', 'IR_LOAD']],
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


#execute does whatever the sent opcode implies
def execute_fetch(opcode):
    TCYCLE=0
    for a in opcode:
        print(a, TCYCLE)
        TCYCLE +=1
        for b in a:
            print(b)

def execute(opcode):
    TCYCLE=3
    for a in opcode:
        print (a, TCYCLE)
        TCYCLE +=1
        for b in a:
            if (sigs[b]==True):
                print(b, True)
            else:
                print(b,False)




execute_fetch(isa['FETCH'])
execute(isa[mem[0]])
