# 3D Sentence Embedding Visualizer

A mini-project that visualizes semantic relationships between sentences using  
**Sentence-Transformers**, **PCA**, and **interactive 3D plots** inside JupyterLab.

The goal is to understand how embeddings work internally and how semantic meaning
forms geometric structure in high-dimensional space.

---

## 🚀 Features

- Converts sentences into 384-dimensional embeddings  
- Reduces embeddings to 3D using PCA  
- Interactive 3D visualization (rotate, zoom, explore)  
- Shows semantic clusters (food, AI, music, animals, etc.)  

---

## 📦 Installation

```bash
git clone https://github.com/davie2009kh/embedding-visualizer.git
cd embedding-visualizer
pip install -r requirements.txt
```

---

## 🧠 How It Works

1. Embeddings generated using `all-MiniLM-L6-v2`  
2. PCA reduces dimensionality from 384 → 3  
3. A 3D scatterplot visualizes sentence meaning  
4. `%matplotlib widget` enables full interactivity  

---

## 🗂 Project Structure

```
embedding-visualizer/
├── main.py
├── README.md
└── requirements.txt
```

---

## 📚 Technologies Used

- Python 3  
- Sentence-Transformers  
- scikit-learn  
- Matplotlib  
- JupyterLab  
- ipywidgets  

---

## ✨ Author

Created by **Davit Ghazaryan**
