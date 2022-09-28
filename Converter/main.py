from fastapi import FastAPI
import services



app = FastAPI()


api_urls = [
    "https://test.mymxp.com/x/?27FC555D2A8B4163B8E13038E2098F3D",
    "https://test.mymxp.com/x/?6C97409671ED43A4A67FCBFB5ABAE8A4"
    # "https://www.mymxp.com/x/?CD1BDE28829148FB87E8C6C894F84AAD",
    # "https://www.mymxp.com/x/?9F8DB2899D2F4DC58E01A18EDABC8993",
    # "https://www.mymxp.com/x/?27EF192D027D41D7BB31CF422D037C30",
    # "https://www.mymxp.com/x/?4699EB93DD7C4E43B3AAC7726E597E18",
    # "https://www.mymxp.com/x/?77C7D2F677E740029A0BB053045A313F",
    # "https://www.mymxp.com/x/?CDCA743BC3314EFBA11C128F9992C66A",
    # "https://www.mymxp.com/x/?CDCA743BC3314EFBA11C128F9992C66A",
    # "https://www.mymxp.com/x/?080B5470215D4403B1C3B71E2A4E5A93",
    # "https://www.mymxp.com/x/?9F8DB2899D2F4DC58E01A18EDABC8993",
    # "https://www.mymxp.com/x/?6D38E6E5E56F4A6282CD152B6E24BACB",
    
]



@app.get("/get_po/")
async def get_purchase_order(link:str):
    data_list = services.get_data(link)
    return services.xml_to_json(data_list)

@app.get("/get_xml/")
async def get_xml():
    data_list = services.get_data("https://test.mymxp.com/x/?27FC555D2A8B4163B8E13038E2098F3D")
    json_data = services.xml_to_json(data_list)
    return services.json_to_xml(json_data[1])
