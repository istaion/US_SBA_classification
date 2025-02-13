#______________________________________________________________________________
# 
# region Centralized MIS_Status definition
#______________________________________________________________________________
MIS_Status_dict = {
    "CHGOFF" : 0,
    "P I F" : 1
}

def convert_MIS_Status_to_int(mis_status : str) -> int:
    if mis_status in MIS_Status_dict:
        return MIS_Status_dict[mis_status]
    
    raise Exception(f"Invalid MIS_status string:  {mis_status}")

def convert_MIS_Status_to_string(mis_status: int) -> str:
    for key, value in MIS_Status_dict.items():
        if value == mis_status:
            return key
        
    raise Exception(f"Invalid MIS_status integer: {mis_status}")
