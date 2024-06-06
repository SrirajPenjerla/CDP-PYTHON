# import pygal

# # Create a Pygal Worldmap object
# worldmap_chart = pygal.maps.world.World()

# # Set the title of the map
# worldmap_chart.title = 'Countries'

# # Add data to the map (country codes and corresponding values)
# worldmap_chart.add('Data', {
#     'us': 300,  # Example value for United States
#     'cn': 500,  # Example value for China
#     'in': 200,  # Example value for India
#     'gb': 150,  # Example value for United Kingdom
#     'fr': 100   # Example value for France
# })

# # Render the map to an SVG file or display it directly
# worldmap_chart.render_to_file('worldmap.svg')

# import agate

# # Create a sample table
# data = [
#     ('John', 'Male', 25),
#     ('Jane', 'Female', 30),
#     ('Doe', 'Male', 35),
#     ('Smith', 'Female', 40),
#     ('Emily', 'Female', 45)
# ]
# column_names = ['name', 'gender', 'age']
# table = agate.Table(data, column_names)

# # Group by 'gender' column
# grouped_table = table.group_by('gender').aggregate([
#     ('AVg Age', agate.Mean('age'))
# ])
# print(grouped_table)

# # Aggregate within each group (calculate average age)
# avg_age_by_gender = grouped_table

# # Print the average age by gender
# print(avg_age_by_gender)


# import agate

# # Create a sample table with data
# data = [
#     ['A', 'Category1', 10],
#     ['B', 'Category2', 20],
#     ['C', 'Category1', 15],
#     ['D', 'Category2', 25],
#     ['E', 'Category1', 5],
#     ['F', 'Category2', 30],
# ]

# # Define column names
# column_names = ['Name', 'Category', 'Value']

# # Create the table
# table = agate.Table(data, column_names)

# # Group by 'Category' column and calculate sum of 'Value' within each group
# grouped_table = table.group_by('Category').aggregate([
#     ('Sum_Value', agate.Sum('Value'))
# ])

# # Print the grouped table
# print("Grouped Table:")
# grouped_table.print_table()


# import agate
# from agatestats import StandardDevOutlier

# # Create a sample table
# data = [
#     ('John', 25),
#     ('Jane', 30),
#     ('Doe', 35),
#     ('Smith', 100),
#     ('Emily', 110),
#     ('Chris', 115)
# ]
# column_names = ['name', 'score']
# table = agate.Table(data, column_names)

# # Apply StandardDevOutlier method
# outliers = table.compute([('outlier', StandardDevOutlier('score'))])

# # Filter the outliers
# filtered_outliers = outliers.where(lambda row: row['outlier'] == True)

# # Print the outliers
# print(filtered_outliers)