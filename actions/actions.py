# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction



#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class firstAction(Action):
    def name(self) -> Text:
        return "action_first"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        try:

            name = tracker.get_slot("name")
            email = tracker.get_slot("email")
            message = tracker.get_slot("message")
            message = "Name:-"+name+"\nEmail:-"+email+"\nMessage:-"+message
            mail_content = message
            sender_address = "rinkesh.panwar@xcitech.in"
            sender_pass = "xcitechtechnology14"
            receiver_address = 'rinkeshpanwar1997@gmail.com'
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'User query from chatbot.'   #The subject line
            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            dispatcher.utter_message(text="Thank you....")
        except:
            dispatcher.utter_message(text="Sorry i am not able to send your query try after sometime.")
        return []

class reviewForm(Action):
    def name(self) -> Text:
        return "action_review"
    
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        try:
            email = tracker.get_slot("email")
            star = str(tracker.get_slot("star"))
            likeAbout = tracker.get_slot("likeAbout")
            improve = tracker.get_slot("improve")
            message = "Email:-"+email+"\nStar:-"+star+"\nWhat user like:"+likeAbout+"\nWhat user want to improve:-"+improve
            mail_content = message
            sender_address = "rinkesh.panwar@xcitech.in"
            sender_pass = "xcitechtechnology14"
            receiver_address = 'rinkeshpanwar1997@gmail.com'
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'User query from chatbot.'   #The subject line
            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            dispatcher.utter_message(text="Thank you....")
        except:    
            dispatcher.utter_message(text="Sorry i am not able to send your query try after sometime.")
        return[]

class validateReviewForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_review_form"
    
    def validate_star(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: "DomainDict") -> Dict[Text, Any]:
        star = [i for i in range(1,11)]
        user_star = slot_value
        try:
            user_star = int(user_star)
            if(user_star in star):
                return {"star":user_star}
            dispatcher.utter_message(text="Only number out of 10 Allowed.")
            return {"star":None}
        except:
            dispatcher.utter_message(text="Only numbers are allowed.Please give review out of 10")
            return {"star":None}


# class user_query_form(FormAction):
#     def name(self) -> Text:
#         return super().name("query_form")
    
#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         return ["name","email","message"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         return {
#             "name": [self.from_entity(entity="name",intent="askName"),self.from_text()],
#             "email":[self.from_entity(entity="email"),self.from_text()],
#             "message":[self.from_text()]
#         }
#     def submit(self, dispatcher: "CollectingDispatcher", tracker: "Tracker", domain: "DomainDict") -> List[EventType]:
#         name_slot = tracker.get_slot("name")
#         email_slot = tracker.get_slot("email")
#         message_slot = tracker.get_slot("message")
#         dispatcher.utter_template(template="utter_thankYou")
#         return []