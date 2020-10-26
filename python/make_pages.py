import os

images_dir = r'H:\GitHub\nfls-basement-museum\images'
pages_dir = r'H:\GitHub\nfls-basement-museum\pages'
default_page = open(r'H:\GitHub\nfls-basement-museum\pages\default_page.html', 'r+', encoding = 'utf-8').read()


for i in [j for j in os.listdir(images_dir) if j.endswith('.jpg')]:
    name = i[:-4]
    output = default_page
    output = output.replace('|id|', name)
    with open('{}\\{}.html'.format(pages_dir, name), 'w+', encoding = 'utf-8') as f:
        f.write(output)