from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sys
sys.path.append('/Users/akhilakumaripuppala/rasa_database_prac/actions')
from database_connectivity import DataUpdate
from weather import Weather
from parks import Place

class ActionReceiveFName(Action):

    def name(self) -> Text:
        return "action_receive_fname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your first name {text}!")
        #dispatcher.utter_message(text=f"if you would like to provide last name please say |give last name|")
        dispatcher.utter_message(response="utter_ask_lname")
        return [SlotSet("fname", text)]

class ActionReceiveLName(Action):
    
    def name(self) -> Text:
        return "action_receive_lname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your last name {text}!")
        #dispatcher.utter_message(text=f"if you would like to provide feedback please say |give feedback|")
        dispatcher.utter_message(response="utter_ask_feedback")
        return [SlotSet("lname", text)]

class ActionReceiveFeedback(Action):
    
    def name(self) -> Text:
        return "action_receive_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your feedback as {text}!")
        dispatcher.utter_message(response="utter_save_data")
        return [SlotSet("feedback", text)]    
    
class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        fname = tracker.get_slot("fname")
        if not fname:
            dispatcher.utter_message(text="I don't know your first name.")
        else:
            dispatcher.utter_message(text=f"Your first name is {fname}!")
            
        lname = tracker.get_slot("lname")
        if not lname:
            dispatcher.utter_message(text="I don't know your last name.")
        else:
            dispatcher.utter_message(text=f"Your last name is {lname}!")
            
        feedbacked = tracker.get_slot("feedback")
        if not lname:
            dispatcher.utter_message(text="I don't know your last name.")
        else:
            dispatcher.utter_message(text=f"Your feedback is {feedbacked}!")
        return []

class ActionSaveFeedback(Action):
    
    def name(self) -> Text:
        return "action_save_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        fname = tracker.get_slot("fname")
        lname = tracker.get_slot("lname")
        feedbacked = tracker.get_slot("feedback")
        DataUpdate(fname,lname,feedbacked) 
        dispatcher.utter_message("Thanks for the valuable feedback.") 
        return []
 

class ActionSayweather(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.latest_message['text']
        temp=int(Weather(city)['temp']-273)
        dispatcher.utter_template("utter_temp",tracker,temp=temp)
        return []        

class ActionSayweather(Action):
    
    def name(self) -> Text:
        return "action_place_api"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        zipcode=tracker.latest_message['text']
        temp= Place(zipcode)
        dispatcher.utter_template("utter_places",tracker,temp=temp)
        return []     























# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List, Union
# #
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet
# #
# #
# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []

# import sys
# sys.path.append('/Users/akhilakumaripuppala/rasa_database_prac/actions')
# from database_connectivity import DataUpdate

# class ActionFirstName(Action):
#     def name(self) -> Text:
#         return "action_last_name"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#                  dispatcher.utter_message(response="utter_ask_lastN") 
#                  return [SlotSet('firstN',tracker.latest_message['text'])]
             
# class ActionFeedback(Action): 
#     def name(self) -> Text: 
#         return "action_feedback"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#         dispatcher.utter_message(response="utter_ask_feedback")   
#         return [SlotSet('lastN',tracker.latest_message['text'])]


# class ActionSubmit(Action): 
#     def name(self) -> Text: 
                      
#         return "action_submit"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#         DataUpdate(tracker.get_slot("firstN"), tracker.get_slot("lastN"),tracker.get_slot("feedback")) 
#         dispatcher.utter_message("Thanks for the valuable feedback. ") 
#         return []

# # class ActionFormInfo(FormAction): 
# #     def name(self) -> Text: 
                                    
# #         return "form_info"

# #     @staticmethod 
# #     def required_slots(tracker: Tracker) -> List[Text]: 
                        
# #         return ["firstN", "lastN","feedback"] 
# #     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]: 
# #         return {
# #                 "firstN": [ self.from_entity( entity="firstN",    
# #                 intent="FirstName"), ], 
# #                 "lastN": [self.from_text()], 
# #                 "feedback": [self.from_text()], }
# #     def submit( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> List[Dict]: 
# #         dispatcher.utter_message(template="utter_submit", Fname=tracker.get_slot("firstN"), Lname=tracker.get_slot("lastN"),fdbk=tracker.get_slot("feedback")) 
# #         return []