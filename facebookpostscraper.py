import requests
from bs4 import BeautifulSoup
from secrets import username, password

class FaceBookBot():
    payload = {
            'email': username,
            'pass': password
        }
    post_ID = ""

    def parse_html(self, request_url):
        with requests.Session() as session:
            session = requests.Session()

            # Set headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            session.headers.update(headers)

            # Get login page
            response = session.get('https://www.facebook.com/')
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract form data and input fields
            form_data = {}
            for input_field in soup.find_all('input'):
                if input_field.has_attr('name'):
                    form_data[input_field['name']] = input_field.get('value', '')
            # Fill in form data
            form_data['email'] = username
            form_data['pass'] = password

            # Submit form
            response = session.post('https://www.facebook.com/login.php', data=form_data)
            print(response.text)
            # Check if login was successful
            if 'Find Friends' in response.text:
                print('Login successful!')
            else:
                print('Login failed.')
                print(self.payload)
        parsed_html = session.get(request_url)
        return parsed_html

    def post_content(self):
        REQUEST_URL = f'https://www.facebook.com/groups/6744817868918838'
        
        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        content = soup.findAll("div", {"class":"x1swvt13 x1pi30zi xexx8yu x18d9i69"})
        post_content = []
        for lines in content:
            post_content.append(lines.text)
        
        post_content = ' '.join(post_content)    
        return post_content

    def date_posted(self):
        REQUEST_URL = f'https://mbasic.facebook.com/story.php?story_fbid={self.post_ID}&id=415518858611168'
        
        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        date_posted = soup.find('abbr')
        return date_posted.text

    def post_likes(self):
        limit = 200
        REQUEST_URL = f'https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit={limit}&total_count=17&ft_ent_identifier={self.post_ID}'

        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        names = soup.find_all('h3')
        people_who_liked = []
        for name in names:
            people_who_liked.append(name.text)
        people_who_liked = [i for i in people_who_liked if i] 
        return people_who_liked

    def post_shares(self):        
        REQUEST_URL = f'https://m.facebook.com/browse/shares?id={self.post_ID}'
        
        with requests.Session() as session:
            post = session.post(self.login_mobile_url, data=self.payload)
            parsed_html = session.get(REQUEST_URL)
        
        soup = BeautifulSoup(parsed_html.content, "html.parser")
        names = soup.find_all('span')
        people_who_shared = []
        for name in names:
            people_who_shared.append(name.text)
        return people_who_shared

