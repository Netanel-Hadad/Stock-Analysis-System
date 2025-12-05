# 📈 Stock Analysis System
A  full-stack web application for analyzing historical stock market data.
Built with a **Microservices-ready architecture**, separating the calculation backend from the visualization frontend.

## 🚀 Features
* **Interactive UI:** Built with **Streamlit**, offering a seamless user experience with date pickers and dynamic inputs.
* **High-Performance Backend:** Powered by **FastAPI** for asynchronous data processing and auto-generated API docs.
* **Advanced Visualization:** Interactive Candlestick and Volume charts using **Plotly** (zoom, pan, hover).

## 🛠️ Tech Stack

* **Frontend:** Streamlit, Plotly
* **Backend:** FastAPI, Uvicorn
* **Data Processing:** Pandas, NumPy
* **Communication:** HTTP REST API

## 📂 Project Structure
```text
├──Client
│  └── main_page.py       # Frontend
├──Server
│  ├──server.py           # Backend
│  ├──Routers/
│  |  └── stock.py        # API Routes handling
│  └──Repositories
│     └── stock.py        # Data Fetching
└── requirements.txt      # Project dependencies
````

## ⚙️ Installation & Setup
1. Clone or download the repository
2. Install dependencies
````text
pip install -r requirements.txt
````

## 🏃‍♂️ How to Run
Since the system consists of a separate Frontend and Backend, you need to run them in parallel (using two terminal windows).
### Step 1: Start the Backend Server
Open a terminal and run:
````text
uvicorn server:app --reload
````
The API will start at http://localhost:8000.

You can view the API Documentation at http://localhost:8000/docs.

### Step 2: Start the Frontend App
Open a new terminal window and run:
````text
streamlit run main_page.py
````
The application will open automatically in your browser (usually at http://localhost:8501).

## 📷 Screenshots
<img width="716" height="437" alt="Screenshot 2025-12-05 141844" src="https://github.com/user-attachments/assets/62d96ce5-e758-4f3e-8795-d9fb9dd0cac1" />

<img width="1893" height="906" alt="Screenshot 2025-12-05 141657" src="https://github.com/user-attachments/assets/2d3e86ed-450f-4c17-9536-68076a0ff44f" />

<img width="1887" height="902" alt="Screenshot 2025-12-05 141733" src="https://github.com/user-attachments/assets/99adf668-658e-4495-8b2b-874162630cb9" />
