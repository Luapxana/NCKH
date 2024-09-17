# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import datetime as dt
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, Any, Dict, List


class ActionDateTime(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        now = dt.datetime.now()
        hour = now.hour
        hour = str(hour)
        minute = now.minute
        minute = str(minute)
        day = now.day
        day = str(day)
        month = now.month
        month = str(month)
        year = now.year
        year = str(year)
        dispatcher.utter_message("Bây giờ là "+hour+" giờ "+minute+" phút ngày "+day+" tháng "+month+" năm "+year)

        return []

class ActionConvertGrade(Action):
    def name(self) -> str:
        return "action_diemchu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        grade = tracker.get_slot('diemso')
        grade = float(grade) if grade else 0.0

        # Định nghĩa điểm chữ tương ứng
        if grade >= 9.0:
            grade_letter = 'A'
        elif grade >= 8.0:
            grade_letter = 'B+'
        elif grade >= 7.0:
            grade_letter = 'B'
        elif grade >= 6.5:
            grade_letter = 'C+'
        elif grade >= 6.0:
            grade_letter = 'C+'
        elif grade >= 5.0:
            grade_letter = 'D+'
        elif grade >= 4.0:
            grade_letter = 'D'   
        else:
            grade_letter = 'F'

        dispatcher.utter_message(text=f"Điểm học phần {grade} sẽ tương đương với điểm chữ {grade_letter}.")
        return []

class ActionConvertGrade(Action):
    def name(self) -> str:
        return "action_diemchu1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        grade = tracker.get_slot('diemso1')
        grade = float(grade) if grade else 0.0

        # Định nghĩa điểm chữ tương ứng
        if grade >= 9.0:
            grade_letter = 'A'
        elif grade >= 8.0:
            grade_letter = 'B+'
        elif grade >= 7.0:
            grade_letter = 'B'
        elif grade >= 6.5:
            grade_letter = 'C+'
        elif grade >= 6.0:
            grade_letter = 'C+'
        elif grade >= 5.0:
            grade_letter = 'D+'
        elif grade >= 4.0:
            grade_letter = 'D'   
        else:
            grade_letter = 'F'

        dispatcher.utter_message(text=f"Điểm học phần {grade} sẽ tương đương với điểm chữ {grade_letter}.")
        return []

class ActionInquireGrade(Action):
    def name(self) -> str:
        return "action_diemhk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        gpa = tracker.get_slot('gpa')
        gpa = float(gpa) if gpa else 0.0

        # Phân loại điểm trung bình
        if gpa >= 3.6:
            classification = 'Xuất sắc'
        elif gpa >= 3.2:
            classification = 'Giỏi'
        elif gpa >= 2.5:
            classification = 'Khá'
        elif gpa >= 2:
            classification = 'Trung bình'
        elif gpa >= 1:
            classification = 'Yếu'
        else:
            classification = 'Kém'
        dispatcher.utter_message(text=f"Điểm trung bình học kỳ {gpa} được xếp loại {classification}.")
        if classification == 'Yếu' or classification == 'Kém':
            dispatcher.utter_message("Kết quả này có thể ảnh hưởng đến kết quả tốt nghiệp của bạn (Yêu cầu tốt nghiệp điểm TBTL phải từ 2.0 trở lên)")
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
