# Hospital In-patient Diagnosis Analysis

## Overview

This project focuses on the exploratory data analysis (EDA) of hospital in-patient diagnosis data using Python. The aim of the project is to analyze trends in hospital diagnoses across different age groups, genders, years, and places of residence to identify meaningful healthcare patterns and insights.

The dataset contains ICD-10 diagnosis categories along with demographic and patient distribution information. Through preprocessing, cleaning, aggregation, and visualization, the project provides an overview of how diseases are distributed among different population groups.

---

# Project Objectives

The primary objectives of this project are:

* Perform data cleaning and preprocessing on hospital diagnosis data
* Simplify and group diagnosis categories for better analysis
* Analyze patient diagnosis trends across:

  * Age groups
  * Gender
  * Residence
  * Year
* Create visualizations to identify healthcare patterns and distributions
* Support healthcare-related exploratory research using data-driven insights

---

# Dataset Description

## Dataset Citation

The dataset used in this project was obtained from the [Destatis Website]([https://www-genesis.destatis.de/genesis/](https://www-genesis.destatis.de/genesis/online?operation=sprachwechsel&language=en)). It contains hospital in-patient diagnosis information including:
 
* ICD-10 diagnosis codes
* Diagnosis categories
* Patient residence
* Gender
* Year of diagnosis
* Age-group based patient distributions

The preprocessing pipeline restructures and simplifies the raw dataset for easier analysis.

---

# Methodology

## 1. Data Preprocessing

The preprocessing pipeline was implemented in `preprocessing.py`.

### Main preprocessing steps:

### Column Renaming

Several complex column names were renamed into simplified and readable labels such as:

* `Diagnosis of hospital in-patients (main diagnosis)` → `Diagnosis`
* `Patient's place of residence` → `Residence`
* `ICD code columns` → `Codes`

### Age Group Aggregation

Fine-grained age ranges were merged into broader groups using mean aggregation:

| Original Age Groups         | New Group |
| --------------------------- | --------- |
| Infants, 5–10, 10–15, 15–18 | 1 to 18   |
| 18–20, 20–25, 25–30         | 18 to 30  |
| 30–35, 35–40, 40–45, 45–50  | 30 to 50  |
| 50–55, 55–60, 60–65, 65–70  | 50 to 70  |
| 70–75, 75–80, 80–85, 85–90  | 70 to 90  |

### Diagnosis Simplification

Long ICD diagnosis labels were grouped into simplified medical categories such as:

* Infections
* Respiratory
* Circulatory
* Metabolic
* Nervous System
* Musculoskeletal
* Blood Disorders
* Digestive Diseases
* Malignant Neoplasms

### Final Feature Selection

The final processed dataset includes:

* Diagnosis
* Residence
* Year
* Gender
* Aggregated age groups

---

# Exploratory Data Analysis (EDA)

The project uses the following Python libraries for analysis and visualization:

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

### Visualizations Included

The notebook contains visual analysis such as:

* Diagnosis distribution plots
* Gender-wise diagnosis comparisons
* Age-group disease analysis
* Year-wise trend analysis
* Correlation analysis
* Distribution and count plots

Interactive visualizations were also created using Plotly for enhanced exploration.

---

# Key Research Questions

The project attempts to answer the following research questions:

1. Which diagnosis categories are most common among hospital in-patients?

2. How do diagnosis trends vary across different age groups?

3. Are there noticeable differences in diagnoses between male and female patients?

4. Which diseases are more prevalent in specific residential areas?

5. How have diagnosis patterns changed over time?

6. Which age groups are most vulnerable to particular diseases?

---

# Technologies Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn

---

# Repository Structure

```bash
Hospital-In-patient-Diagnosis/
│
├── bin/
│   ├── hospital_in-patient_diagnosis.ipynb
│   └── preprocessing.py
│
├── data/
│   ├── hospital_dataset.csv
│
├── docs/
│   ├── description.txt
│
├── CITATION.cff
├── CONDUCT.md
├── LICENSE
├── README.md
└── requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/AlinaImtiaz018/Hospital-In-patient-Diagnosis.git
```

Navigate to the project folder:

```bash
cd Hospital-In-patient-Diagnosis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```bash
hospital_in-patient_diagnosis.ipynb
```

---

# Conclusion

This project demonstrates how exploratory data analysis can be applied to healthcare datasets to uncover meaningful patterns in hospital diagnoses. By preprocessing and aggregating demographic information, the analysis provides insights into disease prevalence across different age groups, genders, and residential areas.

The findings from this project can support healthcare researchers and policymakers in understanding population health trends and identifying areas that may require targeted medical attention or resource allocation.

---

# Future Improvements

Possible future extensions of the project include:

* Predictive modeling for disease forecasting
* Time-series analysis of diagnosis trends
* Interactive dashboards using Streamlit or Dash
* Integration of machine learning models
* Advanced statistical analysis and clustering

---

## Contact Information

For inquiries, please contact [Alina Imtiaz](mailto:alinaimtiaz097@gmail.com).

## License

This project is licensed under the [MIT License](LICENSE).

## Citation

The work must be cited as [Citation File](CITATION.cff).

## Code of Conduct

To review the software's code of conduct, please visit the [Code of Conduct](CONDUCT.md).
