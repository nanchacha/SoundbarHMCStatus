# import requests
# from bs4 import BeautifulSoup
# import streamlit as st
#
# http_proxy = '70.10.15.10:8080'
# https_proxy = '70.10.15.10:8080'
#
# cntr_list = ['au', 'uk']
#
# for cntr in cntr_list:
#     r = requests.get('https://www.samsung.com/{}/audio-devices/help-me-choose'.format(cntr),
#                      proxies={'http': http_proxy, 'https': https_proxy}, verify=False)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     text = soup.find('h1', class_='find-my-sound__header-title')
#     if (text.text == 'Help Me Choose'):
#         print(cntr.upper(), ' is On Live')

import requests
import streamlit as st
from bs4 import BeautifulSoup
import time

# http_proxy = '70.10.15.10:8080'
# https_proxy = '70.10.15.10:8080'

requests.packages.urllib3.disable_warning()

st.markdown("<h2 style='text-align: center; color: #F95700;'>Soundbar Help Me Choose 라이브 현황</h2>", unsafe_allow_html=True)

cntrList = ['IQ_AR', 'IQ_KU', 'GR', 'UK', 'ID', 'MY', 'EG', 'HU', 'LEVANT', 'ES', 'LEVANT_AR', 'HK_EN', 'HK', 'RO', 'SE', 'NO',
            'DK', 'FI', 'AT', 'CH', 'VN', 'CH_FR',
            'TW', 'IT', 'DE', 'PH', 'BR', 'CZ', 'SK', 'FR', 'N_AFRICA', 'PT', 'KZ_KZ', 'KZ_RU', 'AU', 'ZA', 'EE', 'LV',
            'LT', 'CA', 'PY', 'AR', 'SI',
            'HR', 'AE', 'TH', 'NL', 'BE', 'BE_FR', 'SG', 'CL', 'CO', 'MX', 'CA_FR', 'PL', 'UA', 'PK', 'PE', 'AE_AR',
            'RU', 'UY', 'SA', 'SA_EN', 'IL', 'NZ', 'IN']

# cntrList = ['au', 'uk']

live_list = []

def statusYn(num):
    result = False
    if num == 200:
        result = True
    return result


def getStatus(cntr):
    r = requests.get("https://www.samsung.com/{}/audio-devices/help-me-choose".format(cntr), verify=False)
    num = -1
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    elem = soup.find('h1', class_='find-my-sound__header-title')

    # print('elem : ', elem.text);
    try:
        if elem.text:
            num = 200
    except:
        num = -1

    return num


div = round(len(cntrList) / 3)
sectionA = div
sectionB = div * 2
sectionC = len(cntrList)

col1, col2, col3 = st.columns(3)

with col1:
    for i in range(sectionA):
        if (statusYn(getStatus(cntrList[i]))):
            live_list.append(cntrList[i])
            st.write("{} :white_check_mark:".format(cntrList[i]))
        else:
            st.write("{} :red_circle:".format(cntrList[i]))

with col2:
    for i in range(sectionA, sectionB):
        if (statusYn(getStatus(cntrList[i]))):
            live_list.append(cntrList[i])
            st.write("{} :white_check_mark:".format(cntrList[i]))
        else:
            st.write("{} :red_circle:".format(cntrList[i]))

with col3:
    for i in range(sectionB, len(cntrList)):
        if (statusYn(getStatus(cntrList[i]))):
            live_list.append(cntrList[i])
            st.write("{} :white_check_mark:".format(cntrList[i]))
        else:
            st.write("{} :red_circle:".format(cntrList[i]))

st.success(body="Check Done!")

s= ''

for i in live_list:
    s += "- " + i

st.markdown(s)
