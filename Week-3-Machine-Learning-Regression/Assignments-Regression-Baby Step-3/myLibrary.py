import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

class clsCommonTasks():

    def getTrain_Test_Split():
        dataSet = pd.read_csv("insurance_pre.csv")
        dataSet = pd.get_dummies(dataSet, drop_first = False)
        independent = dataSet[['age', 'bmi', 'children', 'sex_female', 'sex_male', 'smoker_no', 'smoker_yes']]
        dependent = dataSet[['charges']]
        x_Train, x_Test, y_Train, y_Test = train_test_split(independent, dependent, test_size = 0.3, random_state = 0)
        return x_Train, x_Test, y_Train, y_Test