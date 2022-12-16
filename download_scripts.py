import requests
from bs4 import BeautifulSoup


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()



if __name__ == '__main__':
    links = open_file('script_links.txt').splitlines()
    for link in links:
        print(link)
        x = requests.get(link)
        lines = x.text.splitlines()
        for line in lines:
            if '.pdf' in line:
                continue
            if '<a href="/scripts/' in line and 'Read' in line:
                try:
                    print(line)
                    url = line.split('"')[1]
                    print(url)
                    html = requests.get('https://imsdb.com/%s' % url).text
                    soup = BeautifulSoup(html)
                    text = soup.get_text('\n')
                    text = text.split('ALL SCRIPTS')[1]
                    text = text.split('User Comments')[0]
                    title = url.replace('/scripts/','').replace('.html','')
                    print(title, '\n\n\n')
                    filename = 'imsdb %s.txt' % title
                    filename = filename.replace(':','')
                    filename = filename.replace('?','')
                    ilename = filename.replace('"','')
                    filename = filename.replace('\\','')
                    filename = filename.replace('/','')
                    save_file('data_screenplays/%s' % filename, text.strip())
                except Exception as oops:
                    print('\n\n\n########### ERROR ########', oops, '\n\n\n')
                    #exit()