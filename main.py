#!/usr/bin/env python
'''
' Script para organizar los KPIs del IMS
' Databases names and relations
' 
' Para el CSCF se obnienen 4 querys
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
' Para el ATS se obniene 1 query
' 0 (table=tb_kpi_ats, tuple:RoASIR REAL,'   'Rate of ATS Successful Initial Registration (%)
' 1 (table=tb_kpi_ats, tuple:RoASIRR REAL,'  'Rate of ATS Successful Initial Refresh Register (%)
' 2 (table=tb_kpi_ats, tuple:RoASUM REAL,'   'Rate of ATS SH UDR Message (%)
' 3 (table=tb_kpi_ats, tuple:RoANRM REAL,'   'Rate of ATS Notification Request message (%)
' 4 (table=tb_kpi_ats, tuple:AMOSCR REAL,'   'ATS MO Session Completion Rate (%)
' 5 (table=tb_kpi_ats, tuple:AMTSCR REAL,'   'ATS MT Session Completion Rate (%)
' 6 (table=tb_kpi_ats, tuple:SRoeSH REAL,'   'Success Rate of  eSRVCC Handover (%)
' 7 (table=tb_kpi_ats, tuple:RoASIDR REAL,'  'Rate of  ATS Successfull Initial De Register (%)
'
'
' Created by Cesar Zuniga (@czubrit)
'
'''

from functions_main import *

if __name__ == "__main__":
  #CSCF KPIs
  main_completion ()
  main_mo_out ()
  main_mt_inc ()
  main_subs_cause ()
  
  #ATS KPIs
  main_ats ()

  #SBC KPIs
  main_mean ()
  main_registration ()

  #CCF KPIs
  main_ccf ()
  