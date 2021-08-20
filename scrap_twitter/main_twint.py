import requests
import lxml.html as html
#//*[@id="id__8vfqb183puk"]/div/div/div/a/div/div[2]/div/img

URL_TEST = 'https://twitter.com/Paulagat10/status/1424472836178026504'

#$x('//img[@alt="Imagen"]/@src')
XPATH_IMAGES = '//img[@alt="Imagen"]/@src'
def run():
    try:
        response = requests.get(URL_TEST)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            images = parsed.xpath()
            print(images)  
        else:
            raise ValueError(f'Error {response.status_code}')

    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    run()
