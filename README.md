# Traffic Accommodation Level Prediction App

![Traffic Background](https://cdn.create.vista.com/api/media/medium/318011570/stock-photo-softly-blurred-photo-roads-summer-riding-machines?token=)

## 🚦 Overview

This project is a **Streamlit web application** that predicts the traffic accommodation level based on various road and traffic parameters. Users can input key features such as speed, volume, and commercial vehicle counts to estimate the current traffic range (e.g., low, moderate, high, extremely high) using pre-trained machine learning models.

## ✨ Features

- **User-friendly web interface** built with Streamlit
- **Multiple model support**: Random Forest, Logistic Regression, Decision Tree
- **Instant predictions** of traffic range and descriptive level
- **Custom UI** with stylish background and CSS
- **Interactive data input** for real-time inference

## 🏗️ App Structure

- `streamlit_app.py`: Main app file – handles UI, input collection, model loading, prediction, and result display.
- `rf_model.pkl`, `log_model.pkl`, `dec_model.pkl`: Pre-trained machine learning models (Random Forest, Logistic Regression, Decision Tree).
- `app/styles.css`: Custom CSS for enhanced UI appearance.
- `traffic_prediction.ipynb`: Jupyter Notebook for data analysis, EDA, and model training.

## 📊 Input Parameters

- **85th Percentile Speed** (`pc85th_kmh`)
- **12 Hour Volume** (`volume_12h`)
- **24 Hour Volume** (`volume_24h`)
- **Commercial Vehicle Volume** (`comm_vhcl`)
- **Peak Volume** (`peakvol`)

## 🧑‍💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Yaswanth-pati/traffic-management-optimization.git
cd traffic-management-optimization
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Model Files

Ensure the following files are present in the root directory:
- `rf_model.pkl`
- `log_model.pkl`
- `dec_model.pkl`

> **Tip:** Retrain or export models using `traffic_prediction.ipynb` if needed.

### 4. Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

The app will open in your web browser.

## 📂 Project File Structure

```
traffic-management-optimization/
│
├── app/
│   └── styles.css
├── rf_model.pkl
├── log_model.pkl
├── dec_model.pkl
├── streamlit_app.py
├── traffic_prediction.ipynb
├── requirements.txt
└── README.md
```

## 🏷️ Prediction Categories

- **Low**: Less than 40 km/h
- **Moderate**: 40–50 km/h
- **High**: 50–60 km/h
- **Extremely High**: More than 60 km/h

## 📈 Model Training & Data

- See `traffic_prediction.ipynb` for exploratory data analysis, feature engineering, and model training steps.
- Models are trained on traffic datasets with relevant features.

## 🚩 Troubleshooting

- **Model not found:** Make sure `.pkl` files are in the root directory.
- **Styling not applied:** Check `app/styles.css` exists and paths are correct.
- **Background image not loading:** Verify internet connection or replace with a local image in the CSS.

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📜 License

[MIT License](LICENSE)

---

**Developed by [Yaswanth-pati](https://github.com/Yaswanth-pati) and contributors.**
