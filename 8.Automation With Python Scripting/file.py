
# Sending an Email with smtplib and MIMEText

import smtplib
from email.mime.text import MIMEText
smtp_server = 'smtp.gmail.com'
port = 587  # For TLS
sender_email = 'thenoobgunmaster@gmail.com'
receiver_email = 'thenoobgunmaster@gmail.com'
message = 'Hello, this is an automated message.'


msg = MIMEText(message)             #        Create a MIMEText object for the email content
msg['Subject'] = 'Automated Email'
msg['From'] = sender_email
msg['To'] = receiver_email


with smtplib.SMTP(smtp_server, port) as server:             # Set up the connection to the SMTP server
    server.starttls()                                            # Start TLS encryption
    password = input("Enter your Gmail password and press enter: ")     # Login to your Gmail account
    server.login(sender_email, password)
    server.sendmail(sender_email, [receiver_email], msg.as_string())        # Send the email

# Explanation:

#     This script sends an email using the Gmail SMTP server.
#     It uses the smtplib library for sending emails and MIMEText for formatting the email content.
#     You need to replace the sender_email and receiver_email with your own email addresses.
#     The email's subject, sender, and receiver are set using the msg object.
#     It prompts the user for their Gmail password (input is hidden) and uses it to log in to the Gmail account.
#     Finally, it sends the email.

# ++++++++++++++++++++++++++++++++  Extracting Links from a Web Page ++++++++++++++++++++++++++++++++++++++++++++++++++++

import requests
from bs4 import BeautifulSoup

url = 'https://example.com'  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = [link['href'] for link in soup.find_all('a')]
print(links)

# Explanation:

#     This script extracts all the links from a webpage.
#     It uses the requests library to fetch the content of the webpage.
#     BeautifulSoup is used to parse the HTML content.
#     It finds all anchor (<a>) tags and extracts the href attribute, which contains the link.
#     The links are stored in the links list and then printed.

#  ++++++++++++++++++++++++++++++++++++++++++  Renaming Files in a Directory ++++++++++++++++++++++++++++++++++++++++++

import os

directory = 'C:/Users/jaisw/Videos/Python/'

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        new_name = filename.replace('old_', 'new_')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

# Explanation:

#     This script renames files in a specified directory.
#     It iterates through all files in the directory and checks if they have a .txt extension.
#     If so, it constructs a new name by replacing 'old_' with 'new_' in the filename.
#     Then, it uses os.rename to rename the file.

#  +++++++++++++++++++++++++++++++  Removing Old Files from a Directory +++++++++++++++++++++++++++++++++++++++++++++

import os
import datetime

directory = 'C:/Users/jaisw/Videos/Python/'
threshold_date = datetime.datetime(2023, 10, 1)

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath) and os.path.getmtime(filepath) < threshold_date.timestamp():
        os.remove(filepath)

# Explanation:

#     This script removes files in a directory that are older than a specified date.
#     It uses os.listdir to iterate through all files in the directory.
#     For each file, it checks if it's a file and if its modification time (os.path.getmtime) is earlier than the specified threshold date.
#     If so, it uses os.remove to delete the file.

#  +++++++++++++++++++++++++++++++++++++++++  Scheduled Task using schedule +++++++++++++++++++++++++++++++++++++++++

import schedule
import time

def job():
    print("This is a scheduled task.")
schedule.every().day.at("14:00").do(job)        # Schedule a task to run every day at 2 PM

while True:
    schedule.run_pending()
    time.sleep(1)

# Explanation:

#     This script schedules a task to run at a specified time.
#     It defines a function job that prints a message.
#     Using schedule, it sets up the task to run every day at 2:00 PM.
#     The script enters an infinite loop where it checks if there are any pending scheduled tasks to run.

#  +++++++++++++++++++++++++++++++++++++ Shutting Down the System  +++++++++++++++++++++++++++++++++++++

import os

os.system('shutdown /s /t 30 ')  # Shutdown Windows after 30 min 

# For Linux/macOS
# os.system('shutdown -h now')

# Explanation:

#     This script shuts down the system.
#     It uses os.system to execute a command in the system's shell.
#     On Windows, it uses shutdown /s /t 0 to initiate a shutdown.
#     For Linux/macOS, the command would be shutdown -h now to initiate a shutdown.

# ++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++

# Certainly! I'll provide you with Python code snippets for each of the mentioned automation tasks along with explanations.

# Automating Data Entry
# Filling out forms or submitting data on websites:

from selenium import webdriver
driver = webdriver.Chrome()     # Initialize the webdriver (make sure you have chromedriver installed)
driver.get('http://example.com')            # Open the website
input_element = driver.find_element_by_name('username')     # Find the form element and fill it out
input_element.send_keys('your_username')

input_element.submit()          # Submit the form
driver.quit()           # Close the browser

# Explanation:

#     We're using the Selenium library to automate web interactions.
#     Initialize a web driver (in this case, Chrome).
#     Open a website.
#     Find the input field and fill it with your desired data.
#     Submit the form.
#     Close the browser.
#   ++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++
# Automating Social Media
# Posting updates on platforms like Twitter or Instagram:

from selenium import webdriver
driver = webdriver.Chrome()


driver.get('https://twitter.com/login')     # Open Twitter and log in
username = driver.find_element_by_name('session[username_or_email]')
password = driver.find_element_by_name('session[password]')
username.send_keys('your_username')
password.send_keys('your_password')
password.submit()


tweet_box = driver.find_element_by_xpath('//div[@role="textbox"]')      # Compose a tweet
tweet_box.send_keys('Automating my tweets with Python! #Automation #Python')


tweet_button = driver.find_element_by_xpath('//div[@data-testid="tweetButtonInline"]')      # Click the tweet button
tweet_button.click()

driver.quit()       # Close the browser

# Explanation:

#     We're again using Selenium to automate interactions with the web.
#     Open Twitter, log in, and compose a tweet.

# +++++++++++++++++++++++++++++++++++++  Automatically responding to messages or comments: +++++++++++++++++++++++++++++++++

# Note: This example is a simplified demonstration and may not work for all platforms.

# Assuming you're using a hypothetical social media API called 'mysocialapi'
import mysocialapi

def respond_to_messages():
    messages = mysocialapi.get_new_messages()
    for message in messages:
        sender = message.sender
        content = message.content

        response = f"Hi {sender}! Thanks for your message: {content}"
        mysocialapi.send_message(sender, response)

respond_to_messages()

# Explanation:

#     In this example, we're assuming the existence of a hypothetical social media API.
#     We define a function respond_to_messages which fetches new messages and responds to them.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Automating PDF Operations
# Merging, splitting, or extracting pages from PDF files:

from PyPDF2 import PdfFileReader, PdfFileWriter

# Merging PDFs
pdf1 = PdfFileReader(open('file1.pdf', 'rb'))
pdf2 = PdfFileReader(open('file2.pdf', 'rb'))

pdf_writer = PdfFileWriter()
pdf_writer.addPage(pdf1.getPage(0))
pdf_writer.addPage(pdf2.getPage(0))

with open('merged.pdf', 'wb') as out_pdf:
    pdf_writer.write(out_pdf)

# Extracting pages
pdf = PdfFileReader(open('source.pdf', 'rb'))
pdf_writer = PdfFileWriter()

for page_num in range(2, 6):  # Extract pages 2 to 5
    pdf_writer.addPage(pdf.getPage(page_num))

with open('extracted.pdf', 'wb') as out_pdf:
    pdf_writer.write(out_pdf)

# Explanation:

#     We're using the PyPDF2 library to handle PDF operations.
#     Merging: Open two PDF files, add pages to a new PDF writer, and save the merged file.
#     Extracting: Open a PDF file, add specific pages to a new PDF writer, and save the extracted file.

#  ++++++++++++++++++++++++++++++++     Converting PDFs to other formats (e.g., Word, Excel): ++++++++++++++++++++++++++++++++++++

from pdf2docx import Converter

pdf_file = "sample.pdf"
docx_file = "output.docx"

cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

# Explanation:

#     Here, we're using the pdf2docx library to convert PDF to Word.
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Automating System Tasks
# Scheduling tasks like backups or system maintenance:

# You can use system tools like cron (on Linux) or Task Scheduler (on Windows) to schedule the execution of your Python scripts.
# Monitoring system resources and taking actions based on conditions:

import psutil

# Example: If CPU usage is above 90%, send an alert
if psutil.cpu_percent() > 90:
    send_alert_email("High CPU Usage", "CPU usage is above 90%")

# Explanation:

#     We're using the psutil library to monitor system resources.
#     If a condition is met (e.g., high CPU usage), you can take appropriate actions.

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Automating Data Analysis
# Running regular reports and sending them to stakeholders:

import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Generate report using pandas
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 90, 75]}
df = pd.DataFrame(data)

# Save the report to a file (e.g., CSV)
df.to_csv('report.csv', index=False)

# Send the report via email
msg = MIMEMultipart()
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'recipient@example.com'
msg['Subject'] = 'Monthly Report'

body = "Please find attached the monthly report."
msg.attach(MIMEText(body, 'plain'))

with open('report.csv', 'rb') as attachment:
    part = MIMEApplication(attachment.read(), Name='report.csv')
    part['Content-Disposition'] = f'attachment; filename={"report.csv"}'
    msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('your_email@gmail.com', 'your_password')
server.sendmail('your_email@gmail.com', 'recipient@example.com', msg.as_string())
server.quit()

# Explanation:

#     We're using pandas for data analysis and smtplib for sending emails.
#     Generate a report (in this case, a CSV file), attach it to an email, and send it.

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Processing data and generating visualizations:

import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data.csv')

# Data processing
# (e.g., calculate summary statistics, filter data)

# Generate visualizations
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Value'])
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Data Visualization')
plt.savefig('visualization.png')

# Explanation:

#     Load data using pandas.
#     Process the data (e.g., calculate summary statistics, filter).
#     Generate visualizations using matplotlib.

#  +++++++++++++++++++++++++++ Automating Tests +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Writing and running automated tests for software applications:

# Example using unittest:

import unittest

class TestMathFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(3 - 1, 2)

    def test_multiplication(self):
        self.assertEqual(2 * 2, 4)

    def test_division(self):
        self.assertEqual(6 / 2, 3)

if __name__ == '__main__':
    unittest.main()

# Explanation:

#     We're using the built-in unittest framework for writing and running tests.
#     Define test cases as classes inheriting from unittest.TestCase.
#     Write individual test methods (e.g., test_addition, test_subtraction).
#     Run the tests using unittest.main().

#  ++++++++++++++++++++++ Automating Social Media Data Analysis ++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Extracting data from social media APIs for analysis or reporting:

import requests

# Assuming we're using a hypothetical social media API
api_url = 'https://api.example.com/posts'

response = requests.get(api_url)
data = response.json()

# Process and analyze data
# (e.g., calculate engagement metrics, sentiment analysis)

# Explanation:

#     Make a request to a hypothetical social media API to retrieve data.
#     Process and analyze the data as per your specific requirements (e.g., calculating engagement metrics, sentiment analysis).

#  +++++++++++++++++++++++++++++++++++ Monitoring social media trends or mentions: ++++++++++++++++++++++++++++++++++++++++++++++++

import tweepy

# Assuming you have Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets with a specific keyword
tweets = api.search(q='python', count=10)

for tweet in tweets:
    print(tweet.text)

# Explanation:

#     Use the Tweepy library to access the Twitter API.
#     Search for tweets containing a specific keyword (in this case, 'python').
