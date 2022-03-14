# Innis-Classification-Project

This repo is the compliation of work done to explore the reasons for churn in the telco dataset using statistical exploration and classification methods. 

## About the Project

### Project Goals

The goal of this project is to identify which customers may churn, the key drivers of that churn, and possible areas of focus for Telco to increase it's customer retention.

### Project Description

In the competitive market of telecommunications retaining customers is paramount. The loss of customers can account for billions in revenue. Understanding why customers churn (terminate their contract) can help Telco get ahead of the situation and reach out to customers who have a high potential to churn. Understanding the drivers of churn can help Telco understand the areas in which they can make the biggest impact in persuading these customers to continue their contracts. In this project I will analyse some potential drivers of churn and create models to predict which customers did churn.  

### Initial Questions

1) Do those who churn pay a higher monthly charge?

2) Does the amount of extras i.e. streaming, tech support, device protection affect churn?

3) Does Tenure affect churn?

4) Does having a partner or dependents affect churn?

### Data Dictionary

Variable | Meaning |
:-: | :-- |
Churn | Whether a customer continued subscription with the company
service_count | Count of service subscribed: internet_ service, phone service, mulitple lines, online security, online backup, device protection, tech support, streaming tv, streaming movies
gender | Gender of customer
senior_citizen | Whether a customer is concidered a senior citizen
partner | Whether a customer has a partner or not
dependents | Whether a customer has dependents or not
tenure | How long a customer has been with the company
phone_service | Whether a customer is subscribed to a phone service
multiple_lines | Whether a customer is subscribed to multiple phon lines
online_security | Whether a customer is subscribed to online security
online_backup | Whether a customer is subscribed to online backup
device_protection | Whether a customer is subscribed to device protection
tech_support | Whether a customer is subscribed to tech support
streaming_tv | Whether a customer is subscribed to streaming TV
streaming_movies | Whether a customer is subscribed to streaming Movies
paperless_billing | Whether a customer has paperless billing
monthly_charges | What the customer pays monthly
total_charges | The total a customer has paid over thier individual tenure
contract_type | What type of contract the customer has: One year, Two years, or month to month
payment_type | How the customer pays their bill: Bank transfer, Credit Card, Electronic Transfer, or Mail Check
internet_service_type | What type of internet service a customer has: Fiber optic, DSL, None

### Steps to Reproduce

1. A locally stored env.py file containing hostname, username and password for the mySQL database containing the telco_churn is needed.

2. Data Science Libraries needed: pandas, numpy, matplotlib.pyplot, seaborn, scipy.stats, sklearn

3. All files in the repo should be cloned to reproduce this project.

4. Ensuring .gitignore is setup to protect env.py file data.

## Plan of Action

### Wrangle

#### Modules

** Acquire **

1) Create and test acquire functions

2) Add functions to acquire.py module

3) Import acquire.py functions and test in notebook

** Prepare **

1) Create and test prepare fucntions

2) Add functions to prepare.py module

3) Import prepare.py functions and test in notebook

** Missing Values **

1) Explore data for missing values (11 found in total charges)

2) Add code to prepare function to remove values

3) Test function in notebook

#### Data Split

1) Write code needed to split data into train, validate and test

2) Add code to prepare function and test in notebook

#### Explore

** Questions to Answer **

1) Do those who churn pay a higher monthly charge?

2) Does the amount of extras i.e. streaming, tech support, device protection affect churn?

3) Does Tenure affect churn?

4) Does having a partner or dependents affect churn?

** Explore through visualizations ** 

1) Create visualizations exploring each question

** Statistics tests **

1) Run statistics test relevant to each question

** Summary ** 

1) Create a summary that answers exploritory questions

#### Modeling

1) Evaluate which metrics best answer each question

2) Evaluate a basline meteric used to compare models to the most present target variable

3) Develop models to predict whether a customer churns or not

4) Fit the model to Train data

5) Evaluate on Validate data to ensure no overfitting

6) Evaluate top model on test data

#### Report

1) Create report ensuring well documented code and clear summary of findings as well as next steps to improve research