import json
import os


def get_student_info(student_id: str) -> dict:
    """
    傳回給定學生 ID 的學生個人資料。
    如果未找到學生，則引發 ValueError 並顯示錯誤訊息。
    """
    for student in students_data:
        if student["student_id"] == student_id:
            return student
    raise Exception(f"學號 {student_id} 找不到.")


def add_course(student_id: str, course_name: str, course_score: float) -> None:
    """
    新增指定學生的課程及其分數。
    如果未找到學生，則引發 ValueError 並顯示錯誤訊息。
    使用斷言確保課程名稱和分數不是空字串。
    """
    assert course_name.strip() and course_score, "課程名稱或分數不可空白."
    assert course_name.strip(), "課程名稱不可空白."
    assert course_score, "課程分數不可空白."

    for student in students_data:
        if student["student_id"] == student_id:
            student["courses"].append(
                {"name": course_name, "score": float(course_score)}
            )
            print("=>課程已成功新增。")
            return
        raise ValueError(f"學號 {student_id} 找不到.")


def calculate_average_score(student_data: dict) -> float:
    """
    計算並傳回學生所有課程的平均分數。
    如果學生沒有課程，則回傳 0.0。
    """
    if not student_data["courses"]:
        return 0.0

    total_score = sum(course["score"] for course in student_data["courses"])
    return total_score / len(student_data["courses"])


# 檢查文件是否存在
file_path = "students.json"
if os.path.isfile(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        students_data = json.load(f)
else:
    print("指定的 JSON 檔案不存在。")
    exit()

while True:
    print("***************選單***************")
    print("1. 查詢指定學號成績")
    print("2. 新增指定學號的課程名稱與分數")
    print("3. 顯示指定學號的各科平均分數")
    print("4. 離開")
    print("**********************************")
    choice = input("請選擇操作項目：")
    if choice == "1":
        student_id = input("請輸入學號: ")
        try:
            student_info = get_student_info(student_id)
            data = json.dumps(student_info, indent=2, ensure_ascii=False)
            print("=>學生資料:", data)
        except Exception as e:
            print("=>發生錯誤:", e)
    elif choice == "2":
        student_id = input("請輸入學號: ")
        course_name = input("請輸入要新增課程的名稱: ")
        course_score = input("請輸入要新增課程的分數: ")
        try:
            add_course(student_id, course_name, course_score)
        except AssertionError as ae:
            print("=>其它例外:", ae)
        except ValueError as e:
            print(f"=>發生錯誤:{e}")
    elif choice == "3":
        student_id = input("請輸入學號: ")
        try:
            student_info = get_student_info(student_id)
            average_score = calculate_average_score(student_info)
            print("=>各科平均分數:", average_score)
        except Exception as e:
            print("=>發生錯誤:", e)
    elif choice == "4":
        print("=>程式結束。")
        break
    else:
        print("=>請輸入有效的選項。")
