import re

CATEGORIES = {
    "Road Issues": ["pothole", "road", "crack", "traffic jam", "accident"],
    "Garbage & Sanitation": ["garbage", "waste", "trash", "dirty", "sewage"],
    "Water Supply": ["water", "pipeline", "leak", "drain"],
    "Electricity": ["power", "electricity", "transformer", "street light", "power cut"],
    "Public Safety": ["crime", "theft", "harassment", "unsafe"],
    "Pollution": ["smoke", "pollution", "noise", "air"],
}

def classify_complaint(text):
    text = text.lower()

    for category, keywords in CATEGORIES.items():
        for k in keywords:
            if re.search(r"\b" + re.escape(k) + r"\b", text):
                return category
    
    return "General Issue"

def summarize(text):
    if len(text) <= 80:
        return text
    return text[:80] + "..."
