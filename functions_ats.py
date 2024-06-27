#!/usr/bin/env python
'''
' Funciones especiales para el ATS
'
' Developed by @czubrit
'
'''

import os, re

def create_table_ats (tb_name):
  sqli = 'CREATE TABLE IF NOT EXISTS ' + tb_name + ' ('\
    'date TEXT,'\
    'network_element TEXT,'\
    'RoASIR REAL,'\
    'RoASIRR REAL,'\
    'RoASUM REAL,'\
    'RoANRM REAL,'\
    'AMOSCR REAL,'\
    'AMTSCR REAL,'\
    'SRoeSH REAL,'\
    'RoASIDR REAL'\
    ');'
  return sqli

def create_table_ccf (tb_name):
  sqli = 'CREATE TABLE IF NOT EXISTS ' + tb_name + ' ('\
    'date TEXT,'\
    'network_element TEXT,'\
    'NoAERfIAR REAL,'\
    'NoAERfStAR REAL,'\
    'NoAERfSpAR REAL,'\
    'NoAERfEtAR REAL,'\
    'NoARfEAR REAL,'\
    'NoARfSIAR REAL,'\
    'NoARfStAR REAL,'\
    'NoARfSpAR REAL,'\
    'NoASRfEAA REAL,'\
    'NoASRfIAA REAL,'\
    'NoASRfStAA REAL,'\
    'NoASRfSpAA REAL'\
    ');'
  return sqli

def create_input_ats ():
  files = os.listdir ("./input/ats/")
  route_files = []
  for file in files:
    if file.endswith(".csv"):
      route_files.append (os.path.join("./input/ats/", file))
  return route_files

def create_input_ccf ():
  files = os.listdir ("./input/ccf/")
  route_files = []
  for file in files:
    if file.endswith(".csv"):
      route_files.append (os.path.join("./input/ccf/", file))
  return route_files

def validate_line_ats (line):
  if (re.search('^[0-9]+\/[0-9]+\/[0-9]+\s.*,\"ATS ID=0\",[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+,[0-9.]+',line)):
    return True
  return False

def validate_line_ccf (line):
  if (re.search('^[0-9]+\/[0-9]+\/[0-9]+\s.*,\"ATS ID=0\",([0-9.]+,?){12}',line)):
    return True
  return False

def insert_into_table_ats (tb_name, params):
  date, ne, one, two, three, four, five, six, seven, eight = params.split(',')
  sqli = 'INSERT INTO ' + tb_name + ' (date, network_element, RoASIR, RoASIRR, RoASUM, RoANRM, AMOSCR, AMTSCR, SRoeSH, RoASIDR) '\
    'VALUES ("%s",%s,%s,%s,%s,%s,%s,%s,%s,%s);' %(date, ne, one, two, three, four, five, six, seven, eight)
  return sqli

def insert_into_table_ccf (tb_name, params):
  date, ne, oe, to, te, fr, fe, sx, sn, et, nn, tn, en, tve = params.split(',')
  sqli = 'INSERT INTO ' + tb_name + ' (date, network_element, NoAERfIAR, NoAERfStAR, NoAERfSpAR, NoAERfEtAR, NoARfEAR, NoARfSIAR, '\
    'NoARfStAR, NoARfSpAR, NoASRfEAA, NoASRfIAA, NoASRfStAA, NoASRfSpAA) '\
    'VALUES ("%s",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);' %(date, ne, oe, to, te, fr, fe, sx, sn, et, nn, tn, en, tve)
  return sqli