# 📈 Stock Analysis System
A  full-stack web application for analyzing historical stock market data using candlestick charts with volume bars.

## 🚀 Features
* **Microservices-ready architecture**, separating the calculation backend from the visualization frontend.
* **Interactive UI:** Built with **Streamlit**, offering a seamless user experience.
* **High-Performance Backend:** Powered by **FastAPI** for asynchronous data processing and auto-generated API docs.
* **Advanced Visualization:** Interactive Candlestick and Volume charts using **Plotly** (zoom, pan, hover).

## 🛠️ Tech Stack
* **Frontend:** Streamlit, Plotly
* **Backend:** FastAPI, Uvicorn
* **Data Processing:** Pandas, NumPy
* **Communication:** HTTP REST API

## 📂 Project Structure
```text
├──Client                       # Frontend
│  ├──app.py                    # streamlit main application
│  ├──pages
│  │  ├──home.py
│  │  ├──stock.py
│  │  ├──screener.py
│  │  └──tabs
│  │     ├──general.py   
│  │     ├──chart.py     
│  │     └──data.py               
│  └──.streamlit
│     └──config.toml
├──Server                       # Backend
│  ├──server.py                 # server main entry file
│  ├──Routers
│  |  └── stock.py        
│  └──Repositories
│     └── stock.py
└── requirements.txt
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

<img width="1794" height="943" alt="Screenshot 2025-12-12 142850" src="https://github.com/user-attachments/assets/0d566bff-d847-4493-8749-392926a0565c" />

<img width="1896" height="928" alt="Screenshot 2025-12-15 221645" src="https://github.com/user-attachments/assets/56b21417-cbb5-4cfc-a238-5a5c07a85672" />

