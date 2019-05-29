class Today:
    req = 'https://datazen.katren.ru/calendar/day/'
    def __init__(self):

        import requests
        import pprint

        print('Input date (YYYY-MM-DD):')
        date = input()
        Today.req = 'https://datazen.katren.ru/calendar/day/{}/'.format(date)
        print('Final request:', Today.req)
        req_result = requests.request('GET', Today.req)
        response = req_result.json()
        if (response['holiday']):
            print(date, 'is a holiday')
        else:
            print(date, 'is not a holiday')

Today()
