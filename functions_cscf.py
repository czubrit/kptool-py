#!/usr/bin/env python
'''
' Funciones especiales para el CSCF
'
' Developed by @czubrit
'
'''

import os, re, sqlite3

def create_database (db_name):
  try:
    connection = sqlite3.connect (db_name)
    return connection
  except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
    exit ()

def create_table_completion (tb_name):
  sqli = 'CREATE TABLE IF NOT EXISTS ' + tb_name + ' ('\
    'date TEXT,'\
    'network_element TEXT,'\
    'RoSSIR REAL,'\
    'RoSSTPR REAL,'\
    'RoSSRR REAL,'\
    'SMOSCR REAL,'\
    'SMTSCR REAL,'\
    'RoSCD REAL,'\
    'NoVSRwS REAL'\
    ');'
  return sqli

def create_table_mo_out (tb_name):
  sqli = 'CREATE TABLE IF NOT EXISTS ' + tb_name + ' ('\
    'date TEXT,'\
    'network_element TEXT,'\
    'ip TEXT,'\
    'SRoSMOOIM REAL'\
    ');'
  return sqli

def create_table_mt_inc (tb_name):
  sqli = 'CREATE TABLE IF NOT EXISTS ' + tb_name + ' ('\
    'date TEXT,'\
    'network_element TEXT,'\
    'ip TEXT,'\
    'SRoSMTIIM REAL'\
    ');'
  return sqli

def create_table_subs_cause (tb_name):
  sqli = 'CREATE TABLE IF NOT EXISTS ' + tb_name + ' ('\
    'date TEXT,'\
    'network_element TEXT,'\
    'type TEXT,'\
    'RoRSMOIS REAL,'\
    'RoRSMTIS REAL'\
    ');'
  return sqli

def create_input_cscf (carpeta):
  files = os.listdir ("./input/cscf/" + carpeta)
  route_files = []
  for file in files:
    if file.endswith(".csv"):
      route_files.append (os.path.join("./input/cscf/" + carpeta, file))
  return route_files

def validate_line_completion (line):
  if (re.search('^[0-9]+\/[0-9]+\/[0-9]+\s.*,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+',line)):
    return True
  return False

def validate_line_mo_out (line):
  if (re.search('^[0-9]+\/[0-9]+\/[0-9]+\s.*,[0-9.]+.*10.182.224.*,[0-9.]+,NIL',line)):
    return True
  return False

def validate_line_mt_inc (line):
  if (re.search('^[0-9]+\/[0-9]+\/[0-9]+\s.*,[0-9.]+.*10.182.224.*,[0-9.]+',line)):
    return True
  return False

def validate_line_subs_cause (line):
  if (re.search('^[0-9]+\/[0-9]+\/[0-9]+\s.*,[0-9.]+.*(VOWIFI_ACCESS|LTE_ACCESS).*Office name=All.*[0-9.]+,[0-9.]+',line)):
    return True
  return False

def insert_into_table_completion (tb_name, params):
  date, ne, one, two, three, four, five, six, seven = params.split(',')
  sqli = 'INSERT INTO ' + tb_name + ' (date, network_element, RoSSIR, RoSSTPR, RoSSRR, SMOSCR, SMTSCR, RoSCD, NoVSRwS) '\
    'VALUES ("%s",%s,%s,%s,%s,%s,%s,%s,%s);' %(date, ne, one, two, three, four, five, six, seven)
  return sqli

def insert_into_table_mo_out (tb_name, params):
  date, ne, ip, one  = params.split(',')
  sqli = 'INSERT INTO ' + tb_name + ' (date, network_element, ip, SRoSMOOIM) '\
    'VALUES ("%s",%s,%s,%s);' %(date, ne, ip, one)
  return sqli

def insert_into_table_mt_inc (tb_name, params):
  date, ne, ip, one  = params.split(',')
  sqli = 'INSERT INTO ' + tb_name + ' (date, network_element, ip, SRoSMTIIM) '\
    'VALUES ("%s",%s,%s,%s);' %(date, ne, ip, one)
  return sqli

def insert_into_table_subs_cause (tb_name, params):
  date, ne, type, one, two  = params.split(',')
  sqli = 'INSERT INTO ' + tb_name + ' (date, network_element, type, RoRSMOIS, RoRSMTIS) '\
    'VALUES ("%s",%s,%s,%s,%s);' %(date, ne, type, one, two)
  return sqli
