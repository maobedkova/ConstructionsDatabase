import codecs, json, re

o = codecs.open('vn.json', 'w', 'utf-8')
f = codecs.open('V_N.csv', 'r', 'utf-8')
i = 0
arr = []
for line in f:
    if i < 1:
        i += 1
        continue
    line = line.strip()
    sp_line = line.split(';')
    if sp_line[3] == '':
        sp_line[3] = '0'
    if sp_line[4] == '':
        sp_line[4] = '0'
    if sp_line[6] == '':
        sp_line[6] = '0'
    if sp_line[7] == '':
        sp_line[7] = '0'
    sp_line[8] = re.sub('[\"\';]', '', sp_line[8])
    arr.append(u'{"id":' + str(i) +
            ',\r\n"noun":"' + sp_line[0] +
            '",\r\n"class_noun":"' + sp_line[1] +
            '",\r\n"verb":"' + sp_line[2] +
            '",\r\n"tax_verb":"' + sp_line[4] +
            '",\r\n"act_verb":"' + sp_line[3] +
            '",\r\n"collocation":"' + sp_line[5] +
            '",\r\n"special construction":' + sp_line[6] +
            ',\r\n"subject":"' + sp_line[7] +
            '"\r\n,"example":"' + sp_line[8] +
            '"\r\n,"freq":' + sp_line[9] + '}')
    i += 1
json.dump(arr, o, ensure_ascii = False, indent=2)
f.close()
o.close()
