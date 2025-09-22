# Svara Reply Classifier

This project provides a **FastAPI service** that classifies short text replies into **positive**, **neutral**, or **negative** sentiment categories.  
The service wraps a trained Logistic Regression model (with TF-IDF features) and exposes a `/predict` endpoint.

---

## 🚀 Features
- `/predict` endpoint for reply sentiment classification  
- Input: JSON with a text string  
- Output: JSON with predicted label and confidence score  
- Swagger UI for interactive testing  
- Optional Docker support for containerized deployment  

---

## ⚙️ Requirements

Make sure you have installed:
- **Python 3.8+**
- **pip** (Python package manager)
- (Optional) **Docker** if you want to run inside a container

Python dependencies (already included in `requirements.txt`):
- fastapi  
- uvicorn  
- scikit-learn  
- joblib  
- numpy  
- pandas  

---

## 🛠️ Installation & Setup

### 1. Clone this repository
```bash
git clone https://github.com/TannaPrasanthkumar/svara-reply-classifier.git
cd svara-reply-classifier
```
###2. Create and activate a virtual environment
```bash
# On Mac/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```
### 3. Install packages
```bash
pip install -r requirements.txt
```
### 4. Start the FastAPI server
``` bash
uvicorn app:app --reload
``` 
Now your API is running at:

cpp
http://127.0.0.1:8000
📬 Example Usage
Using curl
``` bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "Looking forward to the demo!"}'
```
Response:

json
{
  "label": "positive",
  "confidence": 0.87
}
Using Swagger UI
Open http://127.0.0.1:8000/docs in your browser and test the /predict endpoint interactively.
http://127.0.0.1:8000/docs
📄 License
This project is for educational/demo purposes.
