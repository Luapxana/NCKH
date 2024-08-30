# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import datetime as dt
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
    

class ActionDateTime(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        now = dt.datetime.now()
        hour = now.hour
        minute = now.minute
        day = now.day
        month = now.month
        year = now.year
        dispatcher.utter_message("Bây giờ là "+hour+" giờ "+minute+" phút ngày "+day+" tháng "+month+" năm "+year)

        return []



#Action đổi điểm học phần
class ActionCompare(Action):
    def name(self) -> Text:
        return "action_diemhp"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        n = next(tracker.get_latest_entity_values("diemso"), None)

        if n is not None:
            try:
                diem = float(n)
                dispatcher.utter_message("Điểm học phần của bạn là: {diem}")
                if 9.0 <= diem <= 10.0:
                    dispatcher.utter_message("Bạn đã được điểm A cho học phần đó")
                elif 8.0 <= diem <= 8.9: 
                    dispatcher.utter_message("Bạn đã được điểm B+ cho học phần đó")
                elif 7.0 <= diem <= 7.9: 
                    dispatcher.utter_message("Bạn đã được điểm B cho học phần đó")
                elif 6.5 <= diem <= 6.9: 
                    dispatcher.utter_message("Bạn đã được điểm C+ cho học phần đó")
                elif 5.5 <= diem <= 6.4: 
                    dispatcher.utter_message("Bạn đã được điểm C cho học phần đó")
                elif 5.0 <= diem <= 5.4: 
                    dispatcher.utter_message("Bạn đã được điểm D+ cho học phần đó")
                elif 4.0 <= diem <= 4.9: 
                    dispatcher.utter_message("Bạn đã được điểm D cho học phần đó")
                elif 0.0 <= diem <= 4.0: 
                    dispatcher.utter_message("Bạn đã bị điểm F (rớt môn)bcho học phần đó, hãy đăng ký học lại để cải thiện nhé.")
                else:
                    dispatcher.utter_message("Số điểm bạn nhập vào không hợp lệ, xin hãy nhập lại")
            except ValueError:
                dispatcher.utter_message("Xin lỗi, tôi không hiểu số điểm học phần của bạn.")
        else:
            dispatcher.utter_message("Xin lỗi, tôi không nhận dạng được số điểm học phần trong câu hỏi của bạn.")
        return []

# Action xếp loại điểm học kỳ
class ActionCompare(Action):
    def name(self) -> Text:
        return "action_diemhp"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        n = next(tracker.get_latest_entity_values("diemso"), None)

        if n is not None:
            try:
                diem = float(n)
                dispatcher.utter_message("Điểm trung bình học kỳ của bạn là: {diem}")
                if 3.60 <= diem <= 4.00:
                    dispatcher.utter_message("Chúc mừng bạn đã được xếp loại xuất sắc trong học kỳ này")
                elif 3.59 <= diem <= 3.20:
                    dispatcher.utter_message("Bạn được xếp loại giỏi trong học kỳ này")
                elif 2.50 <= diem <= 3.19:
                    dispatcher.utter_message("Bạn được xếp loại khá trong học kỳ này")
                elif 2.00 <= diem <= 2.49:
                    dispatcher.utter_message("Bạn được xếp loại trung bình trong học kỳ này")
                elif 1.00 <= diem <= 1.99:
                    dispatcher.utter_message("Xếp loại của bạn trong học kỳ này là yếu.")
                elif 0.00 <= diem <= 0.99:
                    dispatcher.utter_message("Bạn bị xếp loại kém trong học kỳ này!")
                else:
                    dispatcher.utter_message("Số điểm bạn nhập vào không hợp lệ, xin hãy nhập lại")
                if 0.00 <= diem <= 2.50:
                    dispatcher.utter_message("Kết quả này có thể ảnh hưởng đến kết quả tốt nghiệp của bạn! Hãy cố gắng cải thiện điểm số nhé")
            except ValueError:
                dispatcher.utter_message("Xin lỗi, tôi không hiểu số điểm trung bình học kỳ của bạn.")
        else:
            dispatcher.utter_message("Xin lỗi, tôi không nhận dạng được số điểm trung bình học kỳ trong câu hỏi của bạn.")
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
