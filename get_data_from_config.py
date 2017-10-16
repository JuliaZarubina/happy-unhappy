import json

def get_credentials():
    with open('config.json', 'r') as config:
        data = json.load(config, encoding ='utf-8')
    
        APP_ID = data['credentials']['appId']
        APP_SECRET = data['credentials']['appSecret']
        token = '{}|{}'.format(APP_ID, APP_SECRET)
    
        return token

def get_list_of_pages():
    with open('config.json', 'r') as config:
        data = json.load(config, encoding ='utf-8')
        pages = data['pages']
        list_of_pages = []
        for page in pages:
            list_of_pages.append(page['facebook_name'])
        
        return list_of_pages

def get_database_path():
    with open('config.json', 'r') as config:
        data = json.load(config, encoding ='utf-8')
        database_path = data['database_path']
        
        return database_path

if __name__ == '__main__':
    get_database_path()
    get_credentials()
    get_list_of_pages()
    