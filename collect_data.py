from utils import get_page_data, get_url_from_type


print('COLLECT PETITIONS\n\n')
p1 = int(input('from page no.: '))
p2 = int(input('till page no.: '))
page_type = input('enter type: ')


for page_no in range(p1,p2):

    print('page ', page_no)
    try:
        url = get_url_from_type(page_type) + str(page_no)
        print(url)
        get_page_data(url, page_type)

    except Exception as e:
        print(str(e))


