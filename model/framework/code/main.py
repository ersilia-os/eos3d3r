import requests
from bs4 import BeautifulSoup
import sys
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

base = 'http://165.194.18.43:7050/cardpred'


# readlines()
input_file = open(sys.argv[1], 'r')
Lines = input_file.readlines()[1:]

df = pd.DataFrame(columns={'SMILES', 'Score'})


headers = {
    'Origin': 'http://bioanalysis.cau.ac.kr:7050',
    'Referer': 'http://bioanalysis.cau.ac.kr:7050/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryh77Oe3xhJIYB8YaY',
    'Host': '165.194.18.43:7050'
}



for SMILES in Lines:

    payload = f'''------WebKitFormBoundaryh77Oe3xhJIYB8YaY
Content-Disposition: form-data; name="sm"

{SMILES}
------WebKitFormBoundaryh77Oe3xhJIYB8YaY
Content-Disposition: form-data; name="file"; filename=""
Content-Type: application/octet-stream


------WebKitFormBoundaryh77Oe3xhJIYB8YaY--'''

    req = requests.post(base, data=payload, headers=headers)

    soup = BeautifulSoup(req.text, 'html.parser')
    score = (soup.find('td').text)

    # add row to dataframe
    df.loc[len(df.index)] = [SMILES, score];

df.to_csv(sys.argv[2], index=False)  

