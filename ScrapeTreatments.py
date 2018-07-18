import requests
from bs4 import BeautifulSoup

def clean_italics(string):
    string = str(string)
    bad_chars = ['\n', '\r', '<i>', '</i>']
    for b in bad_chars:
        string = string.replace(b, '')
    string.strip()
    return string

drugs = ['ciprofloxacin', 'levofloxacin', 'pip-tazo', 'doxycycline']

# need to account for MRSA/MSSA/Penicillin susceptible (might be in parentheses)

for d in drugs:
    url = 'http://www.antimicrobe.org/drugpopup/{drug}.htm'.format(drug=d)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    italics = set(soup.find_all('i'))
    print(d.upper() + ' - Antimicrobial Spectrum')
    print('-'*40)
    for i in italics:
        print(clean_italics(i))
    print('\n')

# treatment_id
# treatment_name

# org_id
# org_name

# treatment_id
# org_id