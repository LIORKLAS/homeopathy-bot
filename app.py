from flask import Flask, request, jsonify

app = Flask(__name__)

# מילון של תגובות הבוט
responses = {
    "start": "שלום! איך אני יכול לע
