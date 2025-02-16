from flask import Flask, request, jsonify

app = Flask(__name__)

# מילון של תגובות הבוט
responses = {
    "start": "שלום! איך אני יכול לעזור לך היום?\n1. התאמת רמדי\n2. מידע כללי\n3. המלצות לחיזוק החיסון\n4. עזרה ראשונה\n5. תמיכה רגשית\n6. פנייה לליאור קלס\n7. אין כאן את מה שאני מחפש",
    "acute_or_chronic": "האם מדובר במצב חדש או בתופעה שחוזרת לאורך זמן?\n1. מצב חריף\n2. מצב כרוני\n3. אין כאן את מה שאני מחפש",
    "remedy": "מהי התלונה המרכזית שלך?\n1. חום גבוה\n2. שיעול\n3. כאב גרון\n4. כאבי שרירים\n5. נזלת וליחה\n6. פציעות וכוויות\n7. הקאות ושלשולים\n8. התקפי חרדה\n9. תגובות אלרגיות\n10. תסמינים אחרים",
    "treatment_guidance": "איך לתת את הרמדי בצורה נכונה?\n1. מינון ותדירות\n2. איך לעקוב אחרי השפעה\n3. מתי להחליף רמדי\n4. פנייה להומאופת"
}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", "").lower()
    
    # התאמת תגובה לפי השלב
    response_text = responses.get("start", "לא הבנתי, אנא נסה שוב.")
    
    if "1" in message:
        response_text = responses.get("acute_or_chronic")
    elif "2" in message:
        response_text = responses.get("remedy")
    elif "3" in message:
        response_text = responses.get("treatment_guidance")
    
    return jsonify({"reply": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
