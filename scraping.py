import urllib.request
import pandas as pd
import numpy as np

def parse_results(contents):
    # Select result table
    start = contents.index('<div class="fr-table')
    end = contents[start:].index('</div>')
    results = [e.strip() for e in contents[start:start+end].split('\n')]
    # Split rows
    starts = np.flatnonzero(np.core.defchararray.find(results,'<tr')!=-1)
    ends = np.flatnonzero(np.core.defchararray.find(results,'</tr>')!=-1)
    blocks = [results[starts[i]+1:ends[i]] for i in range(len(starts))]
    # Get header
    header = [e[e.index('>')+1:e.index('</th>')] for e in blocks[0]]
    # Get data in rows
    data_info = []
    for i in range(1,len(blocks)):
        starts = np.flatnonzero(np.core.defchararray.find(blocks[i],'<td')!=-1)
        ends = np.flatnonzero(np.core.defchararray.find(blocks[i],'</td>')!=-1)
        info = [blocks[i][starts[j]+1:ends[j]][0].replace(',','.').replace('\u202f','') for j in range(len(starts))]
        data_info.append(info)
    # Create DataFrame
    data = pd.DataFrame(data_info, columns=header)
    for i in range(len(header)):
        try:
            if '.' in data[header[i]][len(data)-1]: 
                data[header[i]] = data[header[i]].astype(float)
            else: 
                data[header[i]] = data[header[i]].astype(int)
        except:
            data[header[i]] = data[header[i]].astype('U')
    return data

def parse_stats(contents):
    # Select stats table
    start = contents.index('<div class="fr-table')
    end = contents[start:].index('</div>')
    contents = contents[start+end:]
    start = contents.index('<div class="fr-table')
    end = contents[start:].index('</div>')
    results = [e.strip() for e in contents[start:start+end].split('\n')]
    # Split rows
    starts = np.flatnonzero(np.core.defchararray.find(results,'<tr')!=-1)
    ends = np.flatnonzero(np.core.defchararray.find(results,'</tr>')!=-1)
    blocks = [results[starts[i]+1:ends[i]] for i in range(len(starts))]
    # Get header
    header = [e[e.index('>')+1:e.index('</th>')] for e in blocks[0][1:]]
    header = ['Type'] + header
    # Get data in rows
    data_info = []
    for i in range(1,len(blocks)):
        block = blocks[i]
        starts = np.flatnonzero(np.core.defchararray.find(block,'<td')!=-1)
        ends = np.flatnonzero(np.core.defchararray.find(block,'</td>')!=-1)
        info = []
        for j in range(len(starts)):
            if starts[j]==ends[j]: info.append(np.nan)
            else: info.append(block[starts[j]+1:ends[j]][0].replace(',','.').replace('\u202f',''))
        data_info.append(info)
    # Create DataFrame
    data = pd.DataFrame(data_info, columns=header)
    for i in range(len(header)):
        try:
            if '.' in data[header[i]][len(data)-1]: 
                data[header[i]] = data[header[i]].astype(float)
            else: 
                data[header[i]] = data[header[i]].astype(int)
        except:
            data[header[i]] = data[header[i]].astype('U')
    return data

def get_results_url(url):
    # HTTPS request
    contents = urllib.request.urlopen(url).read().decode()
    data_results = parse_results(contents)
    data_stats = parse_stats(contents)
    return data_results, data_stats

def code_circo(department_name):
    dep_data = pd.read_csv("departement_2022.csv")
    try:
        idx = np.where(dep_data['LIBELLE']==department_name)[0][0]
    except:
        print(f"'{department_name}' not found ! Here is the list of available names : {dep_data['LIBELLE'].to_list()}")
        return None
    dep = dep_data.iloc[idx]
    return dep['REG'], dep['DEP']

def url_code(region=0, department=0, number=0):
    if region==0:
        return f"https://www.resultats-elections.interieur.gouv.fr/legislatives2024/ensemble_geographique/{department}/{department}{number:0>2}/index.html"
    return f"https://www.resultats-elections.interieur.gouv.fr/legislatives2024/ensemble_geographique/{region:0>2}/{department}/{department}{number:0>2}/index.html"

def get_results(department_name, number, verbose=True):
    region, department = code_circo(department_name)
    url = url_code(region=region, department=department, number=number)
    try:
        data_results, data_stats =  get_results_url(url)
    except:
        if verbose: print(f"Error with URL : {url}")
        return None
    return data_results, data_stats