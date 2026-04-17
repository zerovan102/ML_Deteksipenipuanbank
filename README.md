# ML_Deteksipenipuanbank

## 🏦 Bank Fraud Detection Machine Learning Project

Proyek machine learning untuk mendeteksi transaksi penipuan (fraud) di perbankan menggunakan teknik clustering dan klasifikasi.

---

## 📋 Deskripsi Proyek

Proyek ini mengembangkan sistem deteksi penipuan bank menggunakan berbagai algoritma machine learning:

- **Clustering**: Mengidentifikasi pola dan kelompok transaksi mencurigakan
- **Klasifikasi**: Memprediksi apakah suatu transaksi merupakan fraud atau legitimate

---

## 📁 Struktur Direktori

```
ML_Deteksipenipuanbank/
├── BMLP_Wahid-Ivan-Saputra/
│   ├── [Clustering]_Submission_Akhir_BMLP_Wahid_Ivan_Saputra.ipynb
│   ├── [Klasifikasi]_Submission_Akhir_BMLP_Wahid_Ivan_Saputra.ipynb
│   ├── ml_project.ipynb
│   ├── generate_submission_files.py
│   ├── organize.py
│   ├── decision_tree_model.h5
│   ├── fraud_detection_pipeline.pkl
│   ├── model_clustering
│   ├── test.txt
│   └── README.md
│
├── web_app/
│   ├── main.py
│   └── static/
│       ├── index.html
│       ├── script.js
│       └── style.css
│
└── README.md (file ini)
```

---

## 🔧 Komponen Proyek

### 1. **Machine Learning Models** (`BMLP_Wahid-Ivan-Saputra/`)

- **Clustering Model**: Mengelompokkan pola transaksi
- **Classification Model**: Decision tree untuk prediksi fraud
- **Pipeline**: Fraud detection pipeline yang terintegrasi

### 2. **Web Application** (`web_app/`)

- **Backend**: Flask (main.py)
- **Frontend**: HTML, CSS, JavaScript
- Interface untuk testing dan visualisasi hasil

---

## 📊 Dataset & Features

Model dilatih menggunakan dataset transaksi bank dengan features seperti:

- Jumlah transaksi (Amount)
- Waktu transaksi (Time)
- Karakteristik PCA
- Label fraud/legitimate

---

## 🚀 Cara Menggunakan

### Prerequisites

```bash
pip install flask
pip install scikit-learn
pip install pandas numpy
pip install tensorflow keras  # Jika menggunakan deep learning
```

### Menjalankan Notebook

```bash
jupyter notebook BMLP_Wahid-Ivan-Saputra/ml_project.ipynb
```

### Menjalankan Web App

```bash
cd web_app
python main.py
# Akses di http://localhost:5000
```

---

## 📈 Model Performance

- **Clustering**: Mengidentifikasi anomali dan kelompok fraud
- **Classification**: High precision dan recall untuk deteksi fraud
- **Pipeline**: End-to-end fraud detection system

---

## 👨‍💻 Author

**Wahid Ivan Saputra**

- GitHub: [zerovan102](https://github.com/zerovan102)
- Project: ML Bank Fraud Detection

---

## 📝 License

Project ini tersedia untuk keperluan edukasi dan penelitian.

---

## 🔗 Links

- [Repository GitHub](https://github.com/zerovan102/ML_Deteksipenipuanbank)
- Submission: BMLP (Bootcamp Machine Learning Practitioner)

---

**Last Updated**: April 2026
