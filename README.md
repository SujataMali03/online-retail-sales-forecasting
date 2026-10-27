\# Online Retail Sales Analysis and Revenue Forecasting



\## Project Overview

This project analyzes online retail transaction data to understand sales trends, identify top-performing countries and products, and forecast revenue for the next seven days using machine learning.



An interactive dashboard was developed using Streamlit to present the analysis, model results, and revenue forecast.



\## Objectives

\- Clean and prepare retail transaction data.

\- Analyze daily revenue trends.

\- Identify top countries and products by revenue.

\- Develop features for time-series forecasting.

\- Train and evaluate a Random Forest regression model.

\- Compare model performance against a baseline.

\- Display insights through an interactive dashboard.



\## Technologies Used

\- Python

\- Pandas and NumPy

\- Matplotlib and Seaborn

\- Scikit-learn

\- Streamlit

\- Git and GitHub



\## Project Workflow

1\. Data collection and exploration

2\. Data cleaning and preprocessing

3\. Exploratory Data Analysis (EDA)

4\. Feature engineering

5\. Machine learning model training

6\. Model evaluation

7\. Seven-day revenue forecasting

8\. Interactive dashboard deployment



\## Model Evaluation



The Random Forest model was evaluated using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE), and compared with a previous-day revenue baseline.



| Metric | Random Forest | Baseline |

|---|---:|---:|

| MAE | 14,632.98 | 24,946.26 |

| RMSE | 24,725.52 | 33,145.56 |



The Random Forest model achieved lower MAE and RMSE than the baseline on the chronological test set.



\## Live Dashboard

\[Open the Streamlit Dashboard](https://online-retail-sales-forecasting-yane9ppkct9nsjgjwaqsvx.streamlit.app/)



\## GitHub Repository

\[View Source Code](https://github.com/SujataMali03/online-retail-sales-forecasting)



\## Dataset

The project uses the Online Retail dataset, which contains transaction records from a UK-based online retailer between December 2010 and December 2011.



Original dataset source:  

https://archive.ics.uci.edu/dataset/352/online+retail



\## Limitations

\- The dataset represents historical transactions from 2010–2011.

\- Historical patterns may not represent current retail demand.

\- The forecast is a machine learning estimate, not a guarantee of future revenue.

\- Results depend on the quality and coverage of the available data.



\## Future Improvements

\- Evaluate additional forecasting models.

\- Incorporate holidays, promotions, and seasonal factors.

\- Retrain the model using recent retail data.

\- Add interactive date filters and product-level insights.



\## Author

Sujata Mali



B.Sc. Data Science Student



