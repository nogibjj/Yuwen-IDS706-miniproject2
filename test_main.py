from main import load_data, get_data_descriptive_stats

#load iris dataset
path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris_df = load_data(path)
# calculate descriptive statistics
statistics = get_data_descriptive_stats(iris_df)

#print("Descriptive Statistics for Iris Dataset: ")
#print(statistics)

# Add assertions to check if the calculated statistics match the expected values
assert statistics['Mean']['sepal_length'] == 5.843333333333334


