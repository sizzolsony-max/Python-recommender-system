# 🎯 Product Recommendation System (Python + Streamlit)

This project is a **Product Recommendation System** that suggests items to users based on their interaction history.  
The system uses **Cosine Similarity** to match users with products that similar users prefer.

---

## 🚀 Features

✔ Recommends personalized items based on user–item ratings  
✔ Uses Cosine Similarity to compute user similarity  
✔ Simple and interactive **Streamlit web interface**  
✔ Lightweight, fast — no deep learning model required  

---

## 🧠 How It Works

1. A user–item rating matrix is created from sample data
2. Cosine similarity is computed between users
3. For any selected user:
   - Find the most similar users
   - Recommend items those users have rated highly but the selected user hasn’t seen yet

---

## 📂 Project Structure

```text
Python-recommender-system/
├─ app.py               # Main Streamlit recommendation system app
├─ requirements.txt     # Python dependencies
└─ README.md            # Project documentation
```

---

## 🛠 Tech Stack

| Category | Technology |
|---------|------------|
| Language | Python |
| Web Framework | Streamlit |
| ML / Recommendation | Cosine Similarity |
| Libraries | Pandas, Scikit-learn |

---

## ▶️ How to Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

App will open automatically in your browser at:

```
http://localhost:8501
```

---

## 🌐 Live Deployment

🔗 **Live App:**  
👉 https://python-recommender-system-m3yj8gew6cmd37jgna7xq9.streamlit.app/#product-recommendation-system

🔗 **GitHub Repository:**  
👉 https://github.com/sizzolsony-max/Python-recommender-system

---

## 🧩 Example Output

Type a user ID and the app will recommend items that similar users liked but the selected user hasn’t rated yet.

---

## 👨‍💻 Author

Sijol soni sahoo – Python & Machine Learning Developer**  
📌 Open to internships and full-time roles in Data / Python / AI  

---
