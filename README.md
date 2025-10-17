# 📰 Fake News Detector Web App

A **modern web-based application** that predicts whether a given news title is **FAKE** or **REAL** using **Python, Flask, and Naive Bayes**.  
The model is trained using the **[Fake and Real News Dataset by Clément Bisaillon](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)**.

---

## 🎯 Features

- Input news titles via a **clean, responsive web interface**.
- Predicts **FAKE** or **REAL** news with a **confidence probability bar**.
- Color-coded results:
  - 🔴 **FAKE**
  - 🟢 **REAL**
- Built with **Bootstrap 5** for a modern UI.
- Probability bar visually shows the model's confidence.

---

## 📸 Screenshots

### **1. Fake Page**
![Fake Page](D:\fake news\images\fake.png)

### **2. Raal Result**
![Real Result](D:\fake news\images\real.png)

> Make sure to place your screenshots in an `images` folder or update the paths.

---

## 🗂 Dataset

- **Dataset Used:** [Fake and Real News Dataset by Clément Bisaillon](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)  
- **Files Required:** `Fake.csv` and `True.csv`  
- **Columns Used:** 
  - `title` – news headline  
  - `label` – `FAKE` or `REAL`  
- Place both CSV files in the **same folder** as the Python script.

---

## ⚙️ Installation

1. Install **Python 3** if not already installed.  
2. Install required packages:

```bash

pip install flask pandas scikit-learn

---

## 🚀 How to Run

Run the Python script: 
python fake_news_detector_ui.py

---

Open your browser and go to:

http://127.0.0.1:5000/

---

Enter a news title and click **Check News**.  

The app will display:
- **Result:** FAKE or REAL  
- **Probability:** Model confidence in percentage (shown with a progress bar)

---

## 🔍 Notes

- Currently uses **news titles** for classification. Using the full article text may improve accuracy.  
- Confidence probability bar indicates **how certain the model is**.  
- Accuracy depends on the dataset quality and size.  

---

## 💡 Optional Improvements

- Highlight **suspicious words** in the news.  
- Add **file upload** or **URL input**.  
- Keep a **history of previous checks**.  
- Enhance UI further with **cards, shadows, or animations**.

---



