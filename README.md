## Banglore House Price Prediction

This web application utilizes a linear prediction model to analyze the Bengaluru Houses Price dataset, which can be accessed on [Kaggle](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data). Additionally, it draws inspiration from a project by Dhaval Patel featured on his YouTube channel, codebasics.

The trained model can predict the price of a house based on criteria such as location, number of bedrooms, number of bathrooms, and lot size. It's important to note that the predictions are valid only for specific areas of Bangalore, India.

## Summary

- [How it Works](#how-it-works)
- [Technologies](#technologies)
- [How to Install](#how-to-install)

## How it Works

The homepage displays default values for each input field. You can enter new values and click the 'Estimate Price' button. The system will then generate a prediction for the house price based on your inputs.
<img src="/assets/home_page.png" alt="showing the home page"/>
<img src="/assets/home_page_prediction.png" alt="Showing the home page predicting the inputs"/>

## Technologies

* **Python:** a versatile programming language widely used in data science, web development, and automation.
* **Numpy and Pandas:** used for data preprocessing, feature engineering, and handling datasets.
* **Matplotlib and Plotly:** data visualization libraries, with Matplotlib providing basic plotting capabilities and Plotly offering interactive and sophisticated visualizations.
* **Sklearn LinearRegression:** used for implementing linear regression models in machine learning projects.
* **Jupyter Notebook and VSCode:** development environments commonly used for Python coding, with Jupyter Notebook focusing on interactive data analysis and VSCode being a general-purpose code editor.
* **Flask:** a lightweight and flexible web framework in Python used for building web applications.
* **HTML, CSS, and JS:** front-end technologies essential for creating web pages, with HTML for structure, CSS for styling, and JavaScript for interactivity.

## How to Install

1. Install [Python](https://www.python.org/)
2. Install the libraries
```
pip install -r requirements.txt
```
3. Navigate to the server folder in the terminal and execute the Python server application.
```
python server.py
```
4. Open the index.html file in the client folder using your preferred browser (Chrome, Edge, Brave, etc.).
5. Enjoy it! 😊