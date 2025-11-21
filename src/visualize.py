import matplotlib.pyplot as pplt

def plot_efficiency_hist(df):
    plt.hist(df["efficiency"], bins=20)
    plt.xlabel("Efficiency")
    plt.ylabel("Frequency")
    plt.title("Honeybee Pollen-to-Honey Efficiency")
    plt.show()