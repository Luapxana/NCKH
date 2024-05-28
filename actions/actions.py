# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, Any, Dict, List
class ActionWhoami(Action):
    def name(self) -> Text:
        return "whoami"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I made this!")

        return []



class ActionWhoami(Action):
    def name(self) -> Text:
        return "action_thanks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="It's my pleasure to help you here.")

        return []

class ActionWhoami(Action):
    def name(self) -> Text:
        return "action_sorry"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="It's fine.")

        return []

class Action11(Action): #Câu 1.1
    def name(self) -> Text:
        return "action_1.1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Quy chế học vụ quy định về công tác học vụ dành cho sinh viên trình độ đại học chính quy bao gồm: Chương trình đào tạo(CTĐT), thời gian học tập, tổ chức đào tạo, đánh giá kết quả học tập, cấp bằng tốt nghiệp và những quy định khác đối với sinh viên.")

        return []

class Action21(Action): #Câu 2.1
    def name(self) -> Text:
        return "action_2.1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Có thể xây dựng kế hoạch học tập dựa vào KHHT toàn khóa được cung cấp, vào htql để xây dựng theo hướng dẫn")

        return []
# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
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
