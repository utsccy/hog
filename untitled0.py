# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:08:50 2019

@author: utscc
"""

customer = pd.read_csv('1_ul_customer.csv', encoding = "ISO-8859-1")
vehicle = pd.read_csv('4_ul_vehicle.csv', encoding = "ISO-8859-1")
insurance = pd.read_csv('3_ul_insurance.csv', encoding = "ISO-8859-1")

df = customer.merge(vehicle,left_on='latestbmwvin_h',right_on='vin_h',how='left')

