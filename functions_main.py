#!/usr/bin/env python
'''
' Funciones para eventos principales
'
' Developed by @czubrit
'
'''

from functions_cscf import *
from functions_ats import *
from functions_sbc import *

import sqlite3

def main_completion():
  connection = create_database ('vims-kpis.db')
  cursor = connection.cursor ()
  sqli = create_table_completion ("tb_kpi_cscf")
  cursor.execute (sqli)
  connection.commit ()

  #input files cscf
  route_files = create_input_cscf ("completion")
  tuples = 0

  for file in route_files:
    #continue
    with open(file, 'r') as kpi_data:
      for kpi_line in kpi_data:
        kpi_line = kpi_line.strip ()
        if (validate_line_completion (kpi_line)):
          params = kpi_line.split(',')
          data_sample = params[0] +','+ params[2] +','+ params[6] +','+ params[8] +','+ params[7] +','+ params[5] +','+ params[4] +','+ params[9] +','+ params[10]
          #print (data_sample)
          sqli = insert_into_table_completion ("tb_kpi_cscf", data_sample)
          try:
            cursor.execute(sqli)
            connection.commit()
          except sqlite3.OperationalError as msg:
            print (msg)
            exit()
          print ("Data Inserted: " + data_sample)
          tuples += 1
  
  print ("Inserted tuples: " + str(tuples))
  print ("Developed by czubrit")


def main_mo_out ():
  connection = create_database ('vims-kpis.db')
  cursor = connection.cursor ()
  sqli = create_table_mo_out ("tb_kpi_cscf_mo_out")
  cursor.execute (sqli)
  connection.commit()

  #input files cscf
  route_files = create_input_cscf ("mo_outgoing")
  tuples = 0

  for file in route_files:
    #continue
    with open(file, 'r') as kpi_data:
      for kpi_line in kpi_data:
        kpi_line = kpi_line.strip()
        if (validate_line_mo_out(kpi_line)):
          params = kpi_line.split(',')
          data_sample = params[0] +','+ params[2] +','+ params[3] +','+ params[4]
          #print (data_sample)
          sqli = insert_into_table_mo_out ("tb_kpi_cscf_mo_out", data_sample)
          try:
            cursor.execute(sqli)
            connection.commit()
          except sqlite3.OperationalError as msg:
            print (msg)
            exit()
          print ("Data Inserted: " + data_sample)
          tuples += 1
  
  print ("Inserted tuples: " + str(tuples))
  print ("Developed by czubrit")

def main_mt_inc ():
  connection = create_database ('vims-kpis.db')
  cursor = connection.cursor ()
  sqli = create_table_mt_inc ("tb_kpi_cscf_mt_inc")
  cursor.execute (sqli)
  connection.commit()

  #input files cscf
  route_files = create_input_cscf ("mt_incoming")
  tuples = 0

  for file in route_files:
    #continue
    with open(file, 'r') as kpi_data:
      for kpi_line in kpi_data:
        kpi_line = kpi_line.strip()
        if (validate_line_mt_inc (kpi_line)):
          params = kpi_line.split(',')
          data_sample = params[0] +','+ params[2] +','+ params[3] +','+ params[4]
          #print (data_sample)
          sqli = insert_into_table_mt_inc ("tb_kpi_cscf_mt_inc", data_sample)
          try:
            cursor.execute(sqli)
            connection.commit()
          except sqlite3.OperationalError as msg:
            print (msg)
            exit()
          print ("Data Inserted: " + data_sample)
          tuples += 1
  
  print ("Inserted tuples: " + str(tuples))
  print ("Developed by czubrit")


def main_subs_cause():
  connection = create_database ('vims-kpis.db')
  cursor = connection.cursor()
  sqli = create_table_subs_cause ("tb_kpi_cscf_subs_cause")
  cursor.execute (sqli)
  connection.commit()

  #input files cscf
  route_files = create_input_cscf ("subscriber_cause")
  tuples = 0

  for file in route_files:
    #continue
    with open(file, 'r') as kpi_data:
      for kpi_line in kpi_data:
        kpi_line = kpi_line.strip()
        if (validate_line_subs_cause (kpi_line)):
          params = kpi_line.split(',')
          data_sample = params[0] +','+ params[2] +','+ re.sub('A.*\=','',params[3]) +','+ params[6] +','+ params[7]
          #print (data_sample)
          sqli = insert_into_table_subs_cause ("tb_kpi_cscf_subs_cause", data_sample)
          try:
            cursor.execute(sqli)
            connection.commit()
          except sqlite3.OperationalError as msg:
            print (msg)
            exit()
          print ("Data Inserted: " + data_sample)
          tuples += 1
  
  print ("Inserted tuples: " + str(tuples))
  print ("Developed by czubrit")

def main_ats ():
  connection = create_database ('vims-kpis.db')
  cursor = connection.cursor()
  sqli = create_table_ats ("tb_kpi_ats")
  cursor.execute (sqli)
  connection.commit()

  #input files cscf
  route_files = create_input_ats ()
  tuples = 0

  for file in route_files:
    #continue
    with open(file, 'r') as kpi_data:
      for kpi_line in kpi_data:
        kpi_line = kpi_line.strip()
        if (validate_line_ats (kpi_line)):
          params = kpi_line.split(',')
          data_sample = params[0]+','+params[2]+','+params[7]+','+params[9]+','+params[11]+','+params[10]+','+params[5]+','+params[6]+','+params[4]+','+params[8]
          #print (data_sample)
          sqli = insert_into_table_ats ("tb_kpi_ats", data_sample)
          try:
            cursor.execute(sqli)
            connection.commit()
          except sqlite3.OperationalError as msg:
            print (msg)
            exit()
          print ("Data Inserted: " + data_sample)
          tuples += 1

  print ("Inserted tuples: " + str(tuples))
  print ("Developed by czubrit")

def main_mean():
  connection = create_database ('vims-kpis.db')
  cursor = connection.cursor()
  sqli = create_table_sbc_mean ("tb_kpi_sbc_mean")
  cursor.execute (sqli)
  connection.commit()

  #input files cscf
  route_files = create_input_sbc ("mean")
  tuples = 0

  for file in route_files:
    with open(file, 'r') as kpi_data:
      for kpi_line in kpi_data:
        kpi_line = kpi_line.strip()
        if (validate_line_sbc_mean (kpi_line)):
          params = kpi_line.split(',')
          data_sample = params[0]+','+params[2]+','+params[4]+','+params[5]+','+params[6]+','+params[7]+','+params[8]+','+params[9]+','+params[10]
          #print (data_sample)
          sqli = insert_into_table_sbc_mean ("tb_kpi_sbc_mean", data_sample)
          try:
            cursor.execute(sqli)
            connection.commit()
          except sqlite3.OperationalError as msg:
            print (msg)
            exit()
          print ("Data Inserted: " + data_sample)
          tuples += 1
  
  print ("Inserted tuples: " + str(tuples))
  print ("Developed by czubrit")

def main_registration():
  connection = create_database ('vims-kpis.db')
  cursor = connection.cursor()
  sqli = create_table_sbc_registration ("tb_kpi_sbc_registration")
  cursor.execute (sqli)
  connection.commit()

  #input files cscf
  route_files = create_input_sbc ("registration")
  tuples = 0

  for file in route_files:
    with open(file, 'r') as kpi_data:
      for kpi_line in kpi_data:
        kpi_line = kpi_line.strip()
        if (validate_line_sbc_registration (kpi_line)):
          params = kpi_line.split(',')
          data_sample = params[0] +','+ params[2] +','+params[6]+','+params[7] +','+params[8]
          #print (data_sample)
          sqli = insert_into_table_sbc_registration ("tb_kpi_sbc_registration", data_sample)
          try:
            cursor.execute(sqli)
            connection.commit()
          except sqlite3.OperationalError as msg:
            print (msg)
            exit()
          print ("Data Inserted: " + data_sample)
          tuples += 1
  
  print ("Inserted tuples: " + str(tuples))
  print ("Developed by czubrit")

def main_ccf ():
  connection = create_database ('vims-kpis.db')
  cursor = connection.cursor()
  sqli = create_table_ccf ("tb_kpi_ccf")
  cursor.execute (sqli)
  connection.commit()

  #input files cscf
  route_files = create_input_ccf ()
  tuples = 0

  for file in route_files:
    #continue
    with open(file, 'r') as kpi_data:
      for kpi_line in kpi_data:
        kpi_line = kpi_line.strip()
        if (validate_line_ccf (kpi_line)):
          params = kpi_line.split(',')
          data_sample = params[0]+','+params[2]+','+params[4]+','+params[5]+','+params[6]+','+params[7]+','+params[8]+','\
            +params[9]+','+params[10]+','+params[11]+','+params[12]+','+params[13]+','+params[14]+','+params[15]
          #print (data_sample)
          sqli = insert_into_table_ccf ("tb_kpi_ccf", data_sample)
          try:
            cursor.execute(sqli)
            connection.commit()
          except sqlite3.OperationalError as msg:
            print (msg)
            exit()
          print ("Data Inserted: " + data_sample)
          tuples += 1

  print ("Inserted tuples: " + str(tuples))
  print ("Developed by czubrit")