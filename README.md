# Medical Examination Data Visualizer

This project focuses on visualizing and making calculations from medical examination data using the popular data visualization library Matplotlib, statistical visualization library Seaborn, and data manipulation library Pandas. The dataset used in this project contains information about body measurements, blood tests, and lifestyle choices of patients, allowing us to explore the relationship between cardiac disease and various factors.

## Dataset Description

The dataset consists of patient records, where each row represents an individual patient and each column represents different features such as age, height, weight, gender, blood pressure, cholesterol levels, glucose levels, smoking habits, alcohol intake, physical activity, and the presence or absence of cardiovascular disease. Here are the details of the dataset variables:

- Age: Objective Feature (integer, days)
- Height: Objective Feature (integer, cm)
- Weight: Objective Feature (float, kg)
- Gender: Objective Feature (categorical code)
- Systolic Blood Pressure: Examination Feature (integer)
- Diastolic Blood Pressure: Examination Feature (integer)
- Cholesterol: Examination Feature (1: normal, 2: above normal, 3: well above normal)
- Glucose: Examination Feature (1: normal, 2: above normal, 3: well above normal)
- Smoking: Subjective Feature (binary)
- Alcohol Intake: Subjective Feature (binary)
- Physical Activity: Subjective Feature (binary)
- Presence or Absence of Cardiovascular Disease: Target Variable (binary)

File Name: `medical_examination.csv`

## Project Tasks

The project tasks are as follows:

1. Create a chart displaying the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables, categorized by patients with cardio=1 and cardio=0 in different panels.

2. Add an "overweight" column to the dataset. Determine if a person is overweight by calculating their Body Mass Index (BMI) using weight in kilograms and height in meters. If the BMI value is greater than 25, set the "overweight" value to 1; otherwise, set it to 0.

3. Normalize the data by mapping the values of cholesterol and gluc to binary values, where 0 represents "normal" and 1 represents "above normal." If the value of cholesterol or gluc is greater than 1, set it to 1; otherwise, set it to 0.

4. Convert the data into long format and create a chart using Seaborn's `catplot()` function. Split the dataset by the "Cardio" variable, creating one chart for each "cardio" value. 

5. Clean the data by filtering out incorrect patient segments based on specific conditions:
   - Keep the data where diastolic pressure is lower than or equal to systolic pressure (ap_lo <= ap_hi).
   - Keep the data where height is between the 2.5th percentile and 97.5th percentile.
   - Keep the data where weight is between the 2.5th percentile and 97.5th percentile.

6. Create a correlation matrix using the cleaned dataset and plot it using Seaborn's `heatmap()` function. The upper triangle of the correlation matrix should be masked to enhance readability.

## Project Files

The project includes the following files:

- `medical_data_visualizer.py`: The main Python script containing the code for medical examination data visualization and analysis.
- `medical_examination.csv`: The CSV file containing the dataset used for analysis.
- `test_module.py`: The unit test file that ensures


## Running the Unit Tests

To validate the correctness of the implemented code, unit tests are provided in the `main.py` file.

The unit tests will be executed, and the test results will be displayed, indicating whether each test has passed or failed.

## Conclusion

The Medical Examination Data Visualizer project provides an opportunity to explore the relationships between various factors and cardiovascular disease using data visualization techniques. By running the code and reviewing the generated charts, you will gain insights into the dataset's characteristics, correlations between variables, and the impact of lifestyle choices on cardiovascular health.

Note: Ensure that you have Pandas, Matplotlib, and Seaborn installed on your system before running the code or the unit tests. 
