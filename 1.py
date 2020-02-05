file = open('clust4.txt', encoding='utf-8')
t = file.read().split('\n')
res = {}
g = ['ward', 'centroid', 'weighted', 'average', 'complete']
lastg = ''
lastp = ''
for i in t:
    ob = i.split()
    if ob[0] in g:
        if i in res.keys():
            pass
        else:
            res[i] = {}
        lastg = i
    if ob[0] == 'Clusters:':
        lastp = int(ob[-1])
        res[lastg][lastp] = {}
    if ob[0] == 'silhouette_score:':
        res[lastg][lastp]['sil'] = float(ob[-1])
    if ob[0] == 'calinski':
        res[lastg][lastp]['calin'] = float(ob[-1])
    if ob[0] == 'davies_bouldin_score:':
        res[lastg][lastp]['dav'] = float(ob[-1])
print(res['average braycurtis'][2])
print(res['average cosine'][3])
print(res['average cosine'][4])
print(res['centroid cosine'][7])


'''
for i in res.keys():
    for j in res[i].keys():
        try:
            if j == 16 and res[i][j]['sil']>0.5 and res[i][j]['calin'] > 100:
                print(i)
                print(res[i][j])
        except Exception:
            pass
'''
"""
for i in res.keys():
    print(i)
    values = list(res[i].values())
    keys = list(res[i].keys())
    try:
        m1 = max(res[i].values(), key=lambda x: x['sil'])
        print(keys[values.index(m1)])
        print(m1)
        m2 = max(res[i].values(), key=lambda x: x['calin'])
        print(keys[values.index(m2)])
        print(m2)
        m3 = min(res[i].values(), key=lambda x: x['dav'])
        print(keys[values.index(m3)])
        print(m3)
    except Exception:
        pass
#    for j in res[i].keys():
#        if res[i][j]['sil']>0.6 and j>5 and res[i][j]['calin']>6000:
#            print(str(j) + str(res[i][j]))
"""

