import numpy as np
import pandas as pd
import math

#______________________________________________________________________________
# 
# region State
#______________________________________________________________________________
def get_state_code( state_data : object ) -> int :

    text = str(state_data) 
    if text == 'ZZ':
        return 0
    
    zero  = ord('A') -1

    conv = ord(text[1])-zero + 100* (ord(text[0])-zero)
    return conv

#______________________________________________________________________________
# 
# region NAICS
#______________________________________________________________________________
""" references 2012 North American Industry Classification System :
    https://www.census.gov/naics/?58967?yearbck=2012 """
INDUSTRY_CODES = {
    "11" : "Agriculture, Forestry, Fishing and Hunting",
    "21" : "Mining, Quarrying, and Oil and Gas Extraction",
    "22" : "Utilities",
    "23" : "Construction", 
    "31" : "Manufacturing",
    "32" : "Manufacturing",
    "33" : "Manufacturing",
    "42" : "Wholesale Trade",
    "44" : "Retail Trade",
    "45" : "Retail Trade",
    "48" : "Transportation and Warehousing",
    "49" : "Transportation and Warehousing",
    "51" : "Information",
    "52" : "Finance and Insurance",
    "53" : "Real Estate and Rental and Leasing",
    "54" : "Professional, Scientific, and Technical Services",
    "55" : "Management of Companies and Enterprises", 
    "56" : "Administrative and Support and Waste Management and Remediation Services",
    "61" : "Educational Services",
    "62" : "Health Care and Social Assistance",
    "71" : "Arts, Entertainment, and Recreation",
    "72" : "Accommodation and Food Services",
    "81" : "Other Services (except Public Administration)",
    "92" : "Public Administration"
}

def get_NAICS_data( naics_data : object) -> int :
    """ references 2012 North American Industry Classification System :
    https://www.census.gov/naics/?58967?yearbck=2012 """
    if naics_data :
        str_code = str(naics_data) 
        if len(str_code) != 6 :
            return 0 
        
        str_code = str_code[0:2]
        return int(str_code)

    return 0

#______________________________________________________________________________
# 
# region ApprovalFY
#______________________________________________________________________________
import re

def get_ApprovalFY_data(approvalFY_data : object) -> int :
    """
    default return == 50
    """
    if approvalFY_data :
        text = str(approvalFY_data)
        if len(text) == 0 :
            return 50
        
        text2 = re.sub("[^0-9]", "", text)
        
        year = int(text2)
        return year
    
    return 50
#______________________________________________________________________________
# 
# region Term
#______________________________________________________________________________
def get_Term_data(term_data : object) -> int :
    if term_data :
        months = int(term_data)
        return months
    
    return 0

#______________________________________________________________________________
# 
# region NoEmp 
#______________________________________________________________________________
def get_NoEmp_data(noEmp_data: object) -> float :
    if noEmp_data :
        months = int(noEmp_data)
        return months
    
    return 0

#______________________________________________________________________________
# 
# region NewExist 
#______________________________________________________________________________
def get_NewExist_data(new_exist_data : object ) -> int :
    if not new_exist_data :
        return 0
    
    data = float(new_exist_data)
    if data.is_integer() :
        return math.ceil(data)

    return 0
    
    

#______________________________________________________________________________
# 
# region CreateJob 
#______________________________________________________________________________

#______________________________________________________________________________
# 
# region RetainedJob 
#______________________________________________________________________________

#______________________________________________________________________________
# 
# region FranchiseCode 
#______________________________________________________________________________
def get_FranchiseCode_data (franchise_code : int ) -> int :
    match franchise_code :
        case 0 : return 0
        case 1 : return 0
        case _ : return 1

#______________________________________________________________________________
# 
# region UrbanRural 
#______________________________________________________________________________

#______________________________________________________________________________
# 
# region RevLineCr 
#______________________________________________________________________________
def get_RevLineCr_data (revLineCr : object ) -> int :
    if not revLineCr :
        return 0
    
    data = str(revLineCr)
    
    match data :
        case "0" : return 0 # Other
        case "N" : return 1 # No 
        case "T" : return 2 # Term
        case "Y" : return 3 # Yes 
        case _ : return 0


#______________________________________________________________________________
# 
# region LowDoc 
#______________________________________________________________________________
def get_LowDoc_data(lowDoc : object ) -> int :
    if not lowDoc :
        return 0
    
    if lowDoc == "Y" :
        return 1
    
    return 0


#______________________________________________________________________________
# 
# region MIS_Status 
#______________________________________________________________________________
def get_MIS_Status_data(mis_status : object) -> str : 
    if not mis_status :
        return "Unknown"
    
    if mis_status == "P I F" or mis_status == "CHGOFF":
        return str(mis_status)
    
    return "Unknown"

def predict_MIS_Status_data(row : dict) -> str : 
    if pd.isna(row['MIS_Status']) : 
        if pd.isna(row['ChgOffDate']):
            return 'P I F' 
        else :
            return 'CHGOFF' 
    
    return row['MIS_Status']
#______________________________________________________________________________
# 
# region GrAppv
#______________________________________________________________________________
def get_GrAppv_value(grAppv_data : object) -> int : 
    """
    default return == 0
    """
    if not grAppv_data :
        return 0
    
    str_data = str(grAppv_data)

    str_data = str_data.replace("$", "")
    str_data = str_data.replace(",", "")
    str_data = str_data.replace(" ", "")
    str_data = str_data.replace(".00", "")

    int_value = int(str_data)

    return int_value

#______________________________________________________________________________
# 
# region SBA_Appv
#______________________________________________________________________________
def get_SBA_Appv_value(sba_appv_data : object ) -> int :
    if not sba_appv_data :
        return 0
    
    str_data = str(sba_appv_data)

    str_data = str_data.replace("$", "")
    str_data = str_data.replace(",", "")
    str_data = str_data.replace(" ", "")
    str_data = str_data.replace(".00", "")

    int_value = int(str_data)

    return int_value
