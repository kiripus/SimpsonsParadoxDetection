import pandas as pd
filename = "../input/duolingo_learning_traces.csv"
attributes_to_convert = ["learning_language", "ui_language"]

if __name__ == '__main__':
    df = pd.read_csv(filename)
    for attribute in attributes_to_convert:
        df[attribute] = df[attribute].astype("category")
        df[attribute] = df[attribute].cat.codes
    df.to_csv(filename[:-4] + "(1).csv", index=False)
