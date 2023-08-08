import pandas as pd
import matplotlib.pyplot as plt

iris_df = pd.read_csv("Iris.csv")

# Create histograms for each numeric column
iris_df.hist(column=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"], bins=10)

# Set titles and labels for the histograms
plt.suptitle("Histograms of Iris Dataset")
plt.xlabel("Measurement")
plt.ylabel("Frequency")

# Display the histograms
plt.show()

# Create histograms of Sepal Length for each species
plt.hist(iris_df[iris_df["Species"] == "Iris-setosa"]["SepalLengthCm"], bins=10, label="Iris-setosa")
plt.hist(iris_df[iris_df["Species"] == "Iris-versicolor"]["SepalLengthCm"], bins=10, label="Iris-versicolor")
plt.hist(iris_df[iris_df["Species"] == "Iris-virginica"]["SepalLengthCm"], bins=10, label="Iris-virginica")

# Set titles and labels
plt.title("Histogram of Sepal Length for each Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")

# Show the legend
plt.legend()

# Display the histogram
plt.show()

# Create histograms of Petal Width for each species
plt.hist(iris_df[iris_df["Species"] == "Iris-setosa"]["PetalWidthCm"], bins=10, label="Iris-setosa")
plt.hist(iris_df[iris_df["Species"] == "Iris-versicolor"]["PetalWidthCm"], bins=10, label="Iris-versicolor")
plt.hist(iris_df[iris_df["Species"] == "Iris-virginica"]["PetalWidthCm"], bins=10, label="Iris-virginica")

# Set titles and labels
plt.title("Histogram of Petal Width for each Species")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")

# Show the legend
plt.legend()

# Display the histogram
plt.show()

# Create a histogram of Sepal Length and Width
plt.hist2d(iris_df["SepalLengthCm"], iris_df["SepalWidthCm"], bins=10, cmap="Blues")

# Set titles and labels
plt.title("Histogram of Sepal Length and Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")

# Add a colorbar
plt.colorbar(label="Frequency")

# Display the histogram
plt.show()

plt.hist2d(iris_df["PetalLengthCm"], iris_df["PetalWidthCm"], bins=10, cmap="Reds")

# Set titles and labels
plt.title("Histogram of Petal Length and Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")

# Add a colorbar
plt.colorbar(label="Frequency")

# Display the histogram
plt.show()

# Create histograms of Sepal Length for each species with stacked bars
plt.hist([iris_df[iris_df["Species"] == "Iris-setosa"]["SepalLengthCm"],
          iris_df[iris_df["Species"] == "Iris-versicolor"]["SepalLengthCm"],
          iris_df[iris_df["Species"] == "Iris-virginica"]["SepalLengthCm"]],
         bins=10, label=["Iris-setosa", "Iris-versicolor", "Iris-virginica"], stacked=True)

# Set titles and labels
plt.title("Histogram of Sepal Length for each Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")

# Show the legend
plt.legend()

# Display the histogram
plt.show()

import seaborn as sns
# Create histograms of Sepal Width for each species with density plot
sns.histplot(data=iris_df, x="SepalWidthCm", hue="Species", bins=10, kde=True)

# Set titles and labels
plt.title("Histogram of Sepal Width for each Species")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Density")

# Display the histogram
plt.show()

# Create histograms of Petal Length for each species with violin plot
sns.violinplot(data=iris_df, x="Species", y="PetalLengthCm")

# Set titles and labels
plt.title("Histogram of Petal Length for each Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")

# Display the histogram
plt.show()
