import requests

url = "https://mytimetable.anu.edu.au/even/rest/timetable/subjects"

payload = "search-term=&semester=ALL&campus=ALL&faculty=ALL&type=ALL&days=1&days=2&days=3&days=4&days=5&days=6&days=0&start-time=00%3A00&end-time=23%3A00"
headers = {
    "cookie": "AWSALB=9yDOgSdUUsBBsaAKK5us70sXWMLAUXw%2Fq%2B22I67%2Bo3dsBVeSw2lXvyNEG%2B5nXjia3wdF1aS6tyPQ0wSot9pz39ICR4jwVYvPtUGkTq5C7tM3JmY5rBp85ar84krc; AWSALBCORS=9yDOgSdUUsBBsaAKK5us70sXWMLAUXw%2Fq%2B22I67%2Bo3dsBVeSw2lXvyNEG%2B5nXjia3wdF1aS6tyPQ0wSot9pz39ICR4jwVYvPtUGkTq5C7tM3JmY5rBp85ar84krc",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://mytimetable.anu.edu.au",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://mytimetable.anu.edu.au/even/timetable/",
    "Cookie": "JSESSIONID=59EBF86BDDF7FC94A7C3FABFACA5F55F; _ga=GA1.3.488515367.1642665306; ELOQUA=GUID=5BC4AD65965B4580A2DD7D1448605626; PS_DEVICEFEATURES=width:2560 height:1440 pixelratio:1.5 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; AWSALB=nj07wBgWXB19Y6Vm2qPuSE9XCuQT3/kTakwITmKioUrRLFxef/1kvni/bl9XK59cXBzYd7+kt6fClzikZVtCEyaLp8l8eP+LwrknMQmOwvDo6Fyq2mhvAKnO0zaj; AWSALBCORS=nj07wBgWXB19Y6Vm2qPuSE9XCuQT3/kTakwITmKioUrRLFxef/1kvni/bl9XK59cXBzYd7+kt6fClzikZVtCEyaLp8l8eP+LwrknMQmOwvDo6Fyq2mhvAKnO0zaj",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.json())