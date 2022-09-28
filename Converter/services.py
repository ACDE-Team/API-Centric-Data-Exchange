import xmltodict
import json
import requests

def xml_to_json(links):
    return_value = []
    for link in links:
        print(link)
        code = link.split("/",5)[-1]

        xml_link = f"https://test.mymxp.com/cgi-bin/ExportDoc.exe/POInterfaceFile{code}&XML"

        response = requests.get(xml_link)
        data_dict = xmltodict.parse(response.text)
        data_dict = data_dict['DATAPACKET']['ROWDATA']['ROW']
        return_value.extend(data_dict)
    
    po_head_code = f"{code[1:9]}-{code[9:13]}-{code[13:17]}-{code[17:21]}-{code[21:]}"
    po_head_response = requests.get(f"https://test.mymxp.com/x/MXP_ECom_ISAPI.dll/MW/QuoteDetail/PurchaseOrderHead?_dc=1663656477193&firstrow=true&documentID=%7B{po_head_code}%7D&")
    po_head_dict = json.loads(po_head_response.text)
    data_dict.append(po_head_dict["data"])
    return return_value