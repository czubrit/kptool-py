#!/usr/bin/env python
'''
' Funciones especiales para el SBC
'
' Developed by @czubrit
'
'''

import os, re

def create_table_sbc_mean (tb_name):
  sqli = 'CREATE TABLE IF NOT EXISTS ' + tb_name + ' ('\
    'date TEXT,'\
    'network_element TEXT,'\
    'ABMOSCR REAL,'\
    'ABMTSCR REAL,'\
    'MDFATRS REAL,'\
    'MDFOTRMOS REAL,'\
    'MDFOTRMTS REAL,'\
    'MDFOTAMOS REAL,'\
    'MDFOTAMTS REAL'\
    ');'
  return sqli

def create_table_sbc_registration (tb_name):
  sqli = 'CREATE TABLE IF NOT EXISTS ' + tb_name + ' ('\
    'date TEXT,'\
    'network_element TEXT,'\
    'RoABSIR REAL,'\
    'RoABSRR REAL,'\
    'NoABRRAts REAL'\
    ');'
  return sqli

def create_input_sbc (carpeta):
  files = os.listdir ("./input/sbc/" + carpeta)
  route_files = []
  for file in files:
    if file.endswith(".csv"):
      route_files.append (os.path.join("./input/sbc/" + carpeta, file))
  return route_files

def validate_line_sbc_mean (line):
  if (re.search('^[0-9]+\/[0-9]+\/[0-9]+\s.*,\"Entity name.*\",[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+',line)):
    return True
  return False

def validate_line_sbc_registration (line):
  if (re.search('^[0-9]+\/[0-9]+\/[0-9]+\s.*,.*name\=.*PCSCF,.*,[0-9.]+,[0-9.]+,[0-9.]+',line)):
    return True
  return False

def insert_into_table_sbc_mean (tb_name, params):
  date, ne, one, two, three, four, five, six, seven = params.split(',')
  sqli = 'INSERT INTO ' + tb_name + ' (date, network_element, ABMOSCR, ABMTSCR, MDFATRS, MDFOTRMOS, MDFOTRMTS, MDFOTAMOS, MDFOTAMTS) '\
    'VALUES ("%s",%s,%s,%s,%s,%s,%s,%s,%s);' %(date, ne, one, two, three, four, five, six, seven)
  return sqli

def insert_into_table_sbc_registration (tb_name, params):
  date, ne, one, two, three = params.split(',')
  sqli = 'INSERT INTO ' + tb_name + ' (date, network_element, RoABSIR, RoABSRR, NoABRRAts) '\
    'VALUES ("%s",%s,%s,%s,%s);' %(date, ne, one, two, three)
  return sqli