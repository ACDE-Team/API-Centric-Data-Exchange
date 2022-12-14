import xmltodict
import json
import requests
from json2xml import json2xml


def link_extractor(link):
    code = link.split("/", 5)[-1]
    po_head_code = f"{code[1:9]}-{code[9:13]}-{code[13:17]}-{code[17:21]}-{code[21:]}"

    po_header_link = f"https://test.mymxp.com/x/MXP_ECom_ISAPI.dll/MW/QuoteDetail/PurchaseOrderHead?_dc=1663656477193&firstrow=true&documentID=%7B{po_head_code}%7D&"
    po_items_link = f"https://test.mymxp.com/cgi-bin/ExportDoc.exe/POInterfaceFile{code}&XML"

    return [po_header_link, po_items_link]


def get_data(link):

    links = link_extractor(link)

    po_header = requests.get(links[0])
    po_items = requests.get(links[1])

    return [json.loads(po_header.text), po_items.text]


def xml_to_json(data_list):
    data_dict = xmltodict.parse(data_list[1])['DATAPACKET']['ROWDATA']['ROW']
    return_value = [data_list[0]['data'], data_dict]
    return return_value


def json_to_xml(data):
    return json2xml.Json2xml(data).to_xml()
