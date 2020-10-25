import os
os.chdir(r'H:\GitHub\nfls-basement-museum\images')
cnt = 0
for i in os.listdir():
    if i.endswith('.JPG') or i.endswith('.jpg'):
        cnt += 1
        os.rename(i, '%s.jpg' % (str(cnt).rjust(3, '0')))