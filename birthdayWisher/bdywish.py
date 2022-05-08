
import datetime as t
import smtplib
import pandas as pd

GMAIL_ID = 'sonushaukee113@gmail.com'
GMAIL_PSWD = ''

def sendEmail(to,sub,msg):
    # print(f"Email to {to} sent with subject: {sub} and message: {msg}")
    s = smtplib.SMTP_SSL('smtp.gmail.com',465)
    s.login(GMAIL_ID, GMAIL_PSWD)
    # s.sendmail(From, To, Subject)
    s.sendmail(GMAIL_ID, to, f"Subject:{sub}\n\n {msg}")
    s.quit()

if __name__ == '__main__':
    #reading excel file data
    df = pd.read_excel('contact.xlsx')
    today = t.datetime.now().strftime("%d-%m-%y")
    
    for index, item in df.iterrows():
        # Items of Birthday column of excel sheet
        bdy = item['Birthday'].strftime("%d-%m-%y")
    
        if (today == bdy):
            msg = "Generall I don't wish people on email but you are so special form me that I bound to send you my wishes on the beautiful occation of your birthday."
            # sendEmail(To, "Subject", "test massage")
            sendEmail("always4ukittu@gmail.com", 'Happpy Birthday', msg)
