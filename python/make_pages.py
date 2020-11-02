import os
import json

images_dir = r'E:\nfls-basement-museum\images'
pages_dir = r'E:\nfls-basement-museum\pages'
default_page = open(pages_dir + r'\default_page.html', 'r+', encoding = 'utf-8').read()
info = json.load(open(r'E:\nfls-basement-museum\info.json', 'r+', encoding = 'utf-8'))
dic = {}
for i in info['data']:
    dic[i[0]] = {'position': i[1], 'author': ', '.join(i[2]), 'tag': ', '.join(i[3])}

for i in [j for j in os.listdir(images_dir) if j.endswith('.jpg')]:
    name = i[:-4]
    pid = int(name)
    output = default_page

    output = output.replace('|id_int|', str(pid))
    output = output.replace('|id|', name)
    output = output.replace('|position|', dic[pid]['position'])
    output = output.replace('|author|', dic[pid]['author'])
    output = output.replace('|tag|', dic[pid]['tag'])
    with open('{}\\{}.html'.format(pages_dir, name), 'w+', encoding = 'utf-8') as f:
        f.write(output)