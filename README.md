# 🏙️ CitySense360 - AI-Powered Smart City Intelligence Platform

CitySense360 is an integrated smart-city AI platform that combines traffic analytics, CCTV detection, complaint classification, chatbot support, and agent-based decision reasoning into one unified system.

The project demonstrates how AI can support data-driven urban governance through:

- 🤖 Machine Learning & Deep Learning

- 👁 Computer Vision (YOLOv8)

- 🧠 NLP & RAG Chatbot

- 🧩 Multi-Agent workflows

- 🌐 FastAPI microservices

- 🐳 Docker-based deployment

---

## 🚀 Key Features

#### 🚦 Traffic Congestion Prediction

Predicts future vehicle counts using a trained neural network model.

#### 🎥 CCTV AI Detection

Detects people, vehicles and objects in uploaded images using YOLOv8.

#### 📝 Complaint Analyzer (NLP)

Automatically classifies citizen complaints into relevant departments.

#### 💬 RAG-Powered City Chatbot

Answer questions using uploaded city policy / document knowledge.

#### 🤖 Multi-Agent Decision Engine

Simulated planner → data → report generation pipeline.

#### 🌐 Cloud-Ready API (FastAPI)

Expose AI services to other systems via HTTP endpoints.

#### 🐳 Containerization (Docker)

Deploy safely on any machine or cloud provider.

---

## 🏗️ Architecture Overview

```
Streamlit Dashboard
        │
        ▼
FastAPI Service (Docker)
        │
        ├── Traffic Prediction (LSTM)
        ├── Complaint Classifier (NLP)
        ├── CCTV Detector (YOLOv8)
        └── RAG Chatbot
```


The frontend communicates with backend services through REST APIs — enabling modular scaling.

---

## 📁 Project Structure

```
CitySense360/
│
├── app/
│   ├── dashboard.py
│   ├── traffic_model.py
│   ├── cctv_detection.py
│   ├── complaint_analyzer.py
│   └── rag_chatbot.py
│
├── api/
│   └── main.py
│
├── agents/
│   └── city_agents.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🛠️ Local Setup

### 1️⃣ Clone repository
```
git clone https://github.com/your-username/citysense360.git
cd citysense360
```
### 2️⃣ Create virtual environment
```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
### 3️⃣ Install dependencies
```
pip install -r requirements.txt

```
### ▶️ Run Dashboard (Streamlit)
```
streamlit run app/dashboard.py
```
### 🌐 Run API (FastAPI)
```
uvicorn api.main:app --reload
```
Open in browser:
```
http://127.0.0.1:8000
```
Example endpoint:
```
/predict/traffic?v1=30&v2=50&v3=70
```

---

## 🐳 Docker Deployment

#### Build
```
docker build -t citysense360
```
#### Run
```
docker run -p 8000:8000 citysense360
```
#### Access
```
http://localhost:8000
```

---

## 🌍 Cloud Deployment (Render)

1. Push project to GitHub
2. Create Web Service → Docker
3. Select branch: main
4. Deploy

Your live API URL will look like:
```
https://citysense360-api.onrender.com/
```

---

## 🧪 API Endpoints

| Method | Endpoint           | Description                |
| ------ | ------------------ | -------------------------- |
| GET    | `/`                | API status                 |
| GET    | `/predict/traffic` | Predict next vehicle count |

---

## 🧠 Technology Stack

- **Python**
- **Streamlit**
- **FastAPI**
- **YOLOv8**
- **LSTM (Traffic Forecasting)**
- **Transformers / sentence-embedding (Chatbot)**
- **Docker**

---

## 📌 Future Enhancements

- Real-time video CCTV feed
- Road-defect segmentation
- Multi-user dashboard with authentication
- Kubernetes deployment

---

## 👨‍💻 Author

**Joshua S**

