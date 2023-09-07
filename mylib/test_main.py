from main import load_data, get_data_descriptive_stats

#load iris dataset
path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris_df = load_data(path)
# calculate descriptive statistics
statistics = get_data_descriptive_stats(iris_df)

print("Descriptive Statistics for Iris Dataset: ")
print(statistics)

# Add assertions to check if the calculated statistics match the expected values for the Iris dataset
assert statistics['Mean']['sepal_length'] == 5.843333333333335
assert statistics['Mean']['sepal_width'] == 3.057333333333334
assert statistics['Mean']['petal_length'] == 3.7580000000000027
assert statistics['Mean']['petal_width'] == 1.199333333333334

