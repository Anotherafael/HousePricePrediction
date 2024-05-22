## House Price Prediction

[Ir à descrição em português](https://github.com/Anotherafael/STUDY_HousePricePrediction/blob/main/README_PT-BR.md)

This web application utilizes a linear prediction model to analyze the [USA Real Estate Dataset](https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset), which is available on Kaggle.

The trained model can predict the price of a house based on criteria such as location, number of bedrooms, number of bathrooms, and lot size. It's important to note that the predictions are valid only for specific areas of California, 'cause the dataset is too large.

## How it Works

![Web demonstration](assets/home_page_interaction.gif "Web demonstration")

## Technologies

* **Python:** for backend development and machine learning model.
* **Numpy and Pandas:** for data preprocessing, feature engineering, and handling datasets.
* **Sklearn:** used for implementing the Random Forest regression model.
* **Matplotlib and Plotly:** for data visualization.
* **Flask:** for the web application.
* **Docker:** for containerizing the services.