import requests
from bs4 import BeautifulSoup

header={
    "Cookie":'id58=c5/nq1jAMzBJvCEVA7K2Ag==; als=0; bj58_id58s="Nk9wZXFsNUZFdWhRMDU0NQ=="; es_ab=1; bj58_new_session=0; bj58_init_refer=""; bj58_new_uv=1; 58tj_uuid=e2bff950-c36e-470f-962f-d429d96775a3; new_session=0; new_uv=1; utm_source=; spm=; init_refer='
}
web_data=requests.get("http://jst1.58.com/counter?infoid=29084381340858&userid=0&uname=&sid=0&lid=1&px=540306529&cfpath=5,36",headers=header)
print(web_data.text)