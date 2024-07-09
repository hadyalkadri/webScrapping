from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from IPython.core.display import display, HTML

pages = [1, 2, 3]
updates = []

for page in pages:
    r = Request(f"https://grabscholarship.com/scholarships/page/{page}")
    r.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
    rawpage = urlopen(r).read()
    soup = BeautifulSoup(rawpage, 'html.parser')
    container = soup.find(class_= "elementor-posts-container")
    posts = container.find_all(class_="elementor-post__card")
    
    for post in posts:
        sub_array = []
        post_title = post.find('h3', class_='elementor-post__title').text.strip()
        post_link = post.find('a')['href']
        post_date = post.find('span', class_='elementor-post-date').text.strip()

        sub_array.append({"Title": post_title})
        sub_array.append({"Date": post_date})
        sub_array.append({"Link": post_link})

        updates.append(sub_array)

# print(updates[0][0])




html_body = "<html><body><table border='1'><tr>"
# Header row
index = 0
for keys in updates[0]:
    for key in keys.keys():
        html_body += f"<th>{key}</th>"
        index+=1
html_body += "</tr>"
print(index)
# Data rows
for array in updates:
    html_body += "<tr>"
    for dict in array:
       
        for value in dict.values():
            html_body += f"<td>{value}</td>"
    html_body += "</tr>"
html_body += "</table></body></html>"

# display(HTML(html_body))

# print(html_body)


# r = Request("https://grabscholarship.com/scholarships/")

# r.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')

# rawpage = urlopen(r).read()



# soup = BeautifulSoup(rawpage, 'html.parser')

# container = soup.find(class_= "elementor-posts-container")

# posts = container.find_all(class_="elementor-post")

# #postsLink = posts.find_all(class_="elementor-post__thumbnail__link")

# updates = []

# for post in posts:
#     post_content = post.text
#     post_link = post.find('a')['href']
#     updates.append((f"Post: {post_content}\n Link: {post_link}\n"))
#     # print(f"Post: {post_content}\n Link: {post_link}\n")


def sendEmail(content):
    sender_email = "hadyalkaderi@gmail.com"
    receiver_email = "hadyalkaderi@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Scholarships Update"
    
    # Add the news headlines to the email body
    # body = "/n".join(arr)
    body = content
    msg.attach(MIMEText(body, 'html'))
    
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Login to your Gmail account with your app password
    server.login(sender_email, "ydjk bagg vtsz abny")
    
    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    
    # Logout from the email server
    server.quit()
    
sendEmail(html_body)
