#!/usr/bin/env python
'''
' Funciones del sqlite3 para obtener todos los KPIs
'
' Developed by @czubrit
'
'''

#CSCF
def sql_create_cscf(tb_name, region):
  sqli = 'SELECT avg(RoSSIR), avg(RoSSTPR), avg(RoSSRR), avg(SMOSCR), avg(SMTSCR), avg(RoSCD), avg(NoVSRwS) '\
    'FROM ' + tb_name + ' '\
    'WHERE ' + tb_name +'.network_element = "' + region + 'RHWNFVCSCF01";'
  return sqli

def sql_create_cscf_one(tb_name, region):
  sqli = 'SELECT avg(RoRSMOIS), avg(RoRSMTIS) '\
    'FROM ' + tb_name + ' '\
    'WHERE ' + tb_name +'.network_element = "' + region + 'RHWNFVCSCF01";'
  return sqli

def sql_create_cscf_two(tb_name, region):
  sqli = 'SELECT avg(SRoSMOOIM) '\
    'FROM ' + tb_name + ' '\
    'WHERE ' + tb_name +'.network_element = "' + region + 'RHWNFVCSCF01";'
  return sqli

def sql_create_cscf_three(tb_name, region):
  sqli = 'SELECT avg(SRoSMTIIM) '\
    'FROM ' + tb_name + ' '\
    'WHERE ' + tb_name +'.network_element = "' + region + 'RHWNFVCSCF01";'
  return sqli

#ATS
def sql_create_ats(tb_name, region):
  sqli = 'SELECT avg(RoASIR ), avg(RoASIRR), avg(RoASUM ), avg(RoANRM ), avg(AMOSCR ), avg(AMTSCR ), avg(SRoeSH ), avg(RoASIDR) '\
    'FROM ' + tb_name + ' '\
    'WHERE ' + tb_name +'.network_element = "' + region + 'RHWNFVATS01";'
  return sqli

#SBC
def sql_create_sbc(tb_name, region, number):
  sqli = ('SELECT avg(ABMOSCR), avg(ABMTSCR), avg(MDFATRS), avg(MDFOTRMOS), avg(MDFOTRMTS), avg(MDFOTAMOS), avg(MDFOTAMTS) '
  'FROM {} '
  'WHERE {}.network_element = "{}RHWNFVSBC{}";')
  sqli = sqli.format(tb_name, tb_name, region, number)
  return sqli

def sql_create_sbc_one(tb_name, region, number):
  sqli = ('SELECT avg(RoABSIR), avg(RoABSRR), avg(NoABRRAts) FROM {} WHERE {}.network_element = "{}RHWNFVSBC{}";')
  sqli = sqli.format(tb_name, tb_name, region, number)
  return sqli

#CCF
def sql_create_ccf(tb_name, region):
  sqli = 'SELECT avg(NoAERfIAR ), avg(NoAERfStAR), avg(NoAERfSpAR), avg(NoAERfEtAR), avg(NoARfEAR), avg(NoARfSIAR), avg(NoARfStAR), '\
      'avg(NoARfSpAR ), avg(NoASRfEAA ), avg(NoASRfIAA ), avg(NoASRfStAA), avg(NoASRfSpAA) '\
    'FROM ' + tb_name + ' '\
    'WHERE ' + tb_name +'.network_element = "' + region + 'RHWNFVATS01";'
  return sqli