import pandas as pd 
filename = "../input/ds_salaries(1).csv"
target_variable = "salary_in_usd"

if __name__ == '__main__':
    df = pd.read_csv(filename)
    df[target_variable] -= df[target_variable].min()
    df[target_variable] /= df[target_variable].max()
    df.to_csv(filename[:-4] + ".csv", index=False)