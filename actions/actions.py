# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import datetime as dt
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Text, Any, Dict, List


class ActionDateTime(Action): #Action cho biết thời gian

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

class ActionConvertGrade(Action): #Action quy đổi điểm số sang điểm chữ
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


class ActionInquireGrade(Action): #Action để xếp loại học kỳ dựa trên đtbhk và đrl
    def name(self) -> str:
        return "action_xep_loai"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: dict) -> list:
        
        gpa = tracker.get_slot('gpa')
        drl = tracker.get_slot('drl')
        gpa = float(gpa)
        drl = float(drl)
        # Phân loại điểm trung bình
        if gpa >= 3.6 and drl >= 90:
            classification = 'Xuất sắc'
        elif gpa >= 3.2 and drl >= 80:
            classification = 'Giỏi'
        elif gpa >= 2.5 and drl >= 70:
            classification = 'Khá'
        elif gpa >= 2 and drl >= 60:
            classification = 'Trung bình'
        elif gpa >= 1 and drl >= 50:
            classification = 'Yếu'
        else:
            classification = 'Kém'
        dispatcher.utter_message(text=f"Điểm trung bình học kỳ {gpa} và điểm rèn luyện {drl} được xếp loại {classification}.")
        if classification == 'Yếu' or classification == 'Kém':
            dispatcher.utter_message("Kết quả này có thể ảnh hưởng đến kết quả tốt nghiệp của bạn (Yêu cầu tốt nghiệp điểm TBTL phải từ 2.0 trở lên)")
        return []



class ActionPeriod(Action): #Action để trả lời thời gian các tiết học (1-9)
    def name(self) -> str:
        return "action_tiet_hoc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        tiet = tracker.get_slot('tiet')
        tiet = float(tiet)
        if tiet == 1:
            start_time = "07:00"
            end_time =  "07:50"
        elif tiet == 2: 
            start_time = "07:50"
            end_time =  "08:40"
        elif tiet == 3: 
            start_time = "08:50"
            end_time =  "09:40"
        elif tiet == 4: 
            start_time = "09:50"
            end_time =  "10:40"
        elif tiet == 5: 
            start_time = "10:40"
            end_time =  "11:30"
        elif tiet == 6: 
            start_time = "13:30"
            end_time =  "14:20"
        elif tiet == 7: 
            start_time = "14:20"
            end_time =  "15:10"
        elif tiet == 8: 
            start_time = "15:20"
            end_time =  "16:10"
        else: 
            start_time = "16:10"
            end_time =  "17:00"
        dispatcher.utter_message(text=f"Thời gian tiết {tiet} là từ {start_time} đến {end_time}.")
        return []

class ActionWarning(Action): #Action để kiểm tra cảnh báo học vụ
    def name(self) -> str:
        return "action_canh_bao_hoc_vu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
    
        year = int(tracker.get_slot('year'))
        gpa = float(tracker.get_slot('gpa'))
        credit = int(tracker.get_slot('credit'))
        pass_credit = int(tracker.get_slot('pass_credit'))
        debt = int(tracker.get_slot('debt'))

        if year == 1:
            threshold = 1.2
        else: 
            threshold = 1.8
        pass_percentage = pass_credit/credit
        
        if gpa < threshold:
            dispatcher.utter_message("Bạn bị cảnh báo học vụ do điểm trung bình học kỳ của bạn quá thấp!")
        elif pass_percentage < 0.5:
            dispatcher.utter_message(text = r"Bạn bị cảnh báo học vụ do số tín chỉ đạt yêu cầu không đủ 50% số tín chỉ bạn đã đăng ký")
        elif debt > 24:
            dispatcher.utter_message("Bạn bị cảnh báo học vụ do đã nợ quá 24 tín chỉ (tính từ đầu khóa học của bạn)")
        else:
            dispatcher.utter_message("Bạn không bị cảnh báo học vụ trong học kỳ này! Hãy cố gắng phát huy nhé!")
        return[ SlotSet("year", None),
                SlotSet("gpa", None),
                SlotSet("credit", None),
                SlotSet("pass_credit", None),
                SlotSet("debt", None)]
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
