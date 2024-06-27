#!/usr/bin/env python
'''
' Organizador de KPIs para el IMS
'
' databases names and relations
' 
' 
' 0  (table_name=tb_kpi_cscf,            tuple: 'RoSSIR REAL,'    'Rate of S-CSCF Successful Initial Registrations (%)'),
' 1  (table_name=tb_kpi_cscf_subs_cause, tuple: 'RoRSMOIS REAL,'  'Rate of Responses (with Subscriber Cause) to S-CSCF MO Incoming Sessions (%)'),
' 2  (table_name=tb_kpi_cscf_subs_cause, tuple: 'RoRSMTIS REAL,'  'Rate of Responses (with Subscriber Cause) to S-CSCF MT Incoming Sessions (%)'),
' 3  (table_name=tb_kpi_cscf,            tuple: 'RoSSTPR REAL,'   'Rate of S-CSCF Successful Third-party Registrations (%)'),
' 4  (table_name=tb_kpi_cscf,            tuple: 'RoSSRR REAL,'    'Rate of S-CSCF Successful Re-registrations (%)'),
' 5  (table_name=tb_kpi_cscf_mo_out,     tuple: 'SRoSMOOIM REAL,' 'Success Rate of S-CSCF MO Outgoing Instant Messages (%)'),
' 6  (table_name=tb_kpi_cscf_mt_inc,     tuple: 'SRoSMTIIM REAL,' 'Success Rate of S-CSCF MT Incoming Instant Messages (%)'),
' 7  (table_name=tb_kpi_cscf,            tuple: 'SMOSCR REAL,'    'S-CSCF MO Session Completion Rate (%)'),
' 8  (table_name=tb_kpi_cscf,            tuple: 'SMTSCR REAL,'    'S-CSCF MT Session Completion Rate (%)'),
' 9  (table_name=tb_kpi_cscf,            tuple: 'RoSCD REAL,'     'Rate of S-CSCF Call Drop (%)'),
' 10 (table_name=tb_kpi_cscf,            tuple: 'NoVSRwS REAL,'   'Number of VoLTE Subscribers Registered with S-CSCF (number)'),
'
' Created by Cesar Zuniga (@czubrit)
'
'''
from functions_reader_kpi import *
import sqlite3

def main():
  try:
    connection = sqlite3.connect("vims-kpis.db")
    cursor = connection.cursor()
    regions = ["R5FRE", "R5TLA", "R7CTP", "R7FTE", "R8CAS", "R8YAX"]
    for region in regions:
      sqli = sql_create_cscf("tb_kpi_cscf", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      data_collect = list(record[0])

      sqli = sql_create_cscf_one("tb_kpi_cscf_subs_cause", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      RoRSMOIS, RoRSMTIS = list (record[0])
      data_collect.insert(1,RoRSMOIS)
      data_collect.insert(2,RoRSMTIS)

      sqli = sql_create_cscf_two("tb_kpi_cscf_mo_out", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      SRoSMOOIM = list (record[0])
      data_collect.insert(5,SRoSMOOIM[0])

      sqli = sql_create_cscf_three("tb_kpi_cscf_mt_inc", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      SRoSMTIIM = list (record[0])
      data_collect.insert(6,SRoSMTIIM[0])

      # PRINT KPIS OF CSCF PER REGION
      print (region + "RHWNFVCSCF01")
      print (str(data_collect) + "\n")
    
    for region in regions:
      sqli = sql_create_ats("tb_kpi_ats", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      data_collect = list(record[0])

      # PRINT KPIS OF ATS PER REGION
      print (region + "RHWNFVATS01")
      print (str(data_collect) + "\n")
    
    for region in regions:
      sqli = sql_create_sbc("tb_kpi_sbc_mean", region, "01")
      cursor.execute (sqli)
      record = cursor.fetchall ()
      data_collect = list(record[0])

      sqli = sql_create_sbc("tb_kpi_sbc_mean", region, "02")
      cursor.execute (sqli)
      record = cursor.fetchall ()
      data_collect2 = list(record[0])

      sqli = sql_create_sbc_one("tb_kpi_sbc_registration", region, "01")
      cursor.execute (sqli)
      record = cursor.fetchall ()
      RoABSIR, RoABSRR, NoABRRAts = list(record[0])
      data_collect.append(RoABSIR)
      data_collect.append(RoABSRR)
      data_collect.append(NoABRRAts)

      sqli = sql_create_sbc_one("tb_kpi_sbc_registration", region, "02")
      cursor.execute (sqli)
      record = cursor.fetchall ()
      RoABSIR, RoABSRR, NoABRRAts = list(record[0])
      data_collect2.append(RoABSIR)
      data_collect2.append(RoABSRR)
      data_collect2.append(NoABRRAts)

      # PRINT KPIS OF SBC PER REGION
      print (region + "RHWNFVSBC01/02")
      print (str(data_collect) + "\n")
      print (str(data_collect2) + "\n")

    for region in regions:
      sqli = sql_create_ccf("tb_kpi_ccf", region)
      cursor.execute (sqli)
      record = cursor.fetchall ()
      data_collect = list(record[0])

      # PRINT KPIS OF ATS PER REGION
      print (region + "RHWNFVCCF01")
      print (str(data_collect) + "\n")

  except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
  
  finally:
    if connection:
      connection.close()
      print("The SQLite connection is closed")

if __name__ == "__main__":
  main()