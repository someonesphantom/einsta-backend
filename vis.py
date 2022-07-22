import matplotlib.pyplot as plt
import pandas as pd

def bar(file):
    data = pd.read_csv(file)
    df = pd.DataFrame(data)
    print("Columns of the file: ", list(df.columns))
    x=input("Enter column for x-axis:")
    X = list(df.loc[:,x])
    plt.xlabel(x)
    print("Columns of the file: ", list(df.columns))
    y=input("Enter column for y-axis:")
    Y = list(df.loc[:,y])
    plt.ylabel(y)
    print("Bar graph displayed")
    plt.bar(X, Y, color='g')
    # plt.savefig("output.jpg")
    # plt.show()

def scatter(file):
    data = pd.read_csv(file)
    df = pd.DataFrame(data)
    print("Columns of the file: ", list(df.columns))
    x=input("Enter column for x-axis:")
    X = list(df.loc[:,x])
    print("List of values:", X)
    plt.xlabel(x)
    print("Columns of the file: ", list(df.columns))
    y=input("Enter column for y-axis:")
    Y = list(df.loc[:,y])
    plt.ylabel(y)
    print("Scatter plot displayed")
    plt.scatter(X, Y, color='g')
    # plt.savefig("scatter.jpg")
    plt.show()

def hist(file):
    data = pd.read_csv(file)
    df = pd.DataFrame(data)
    print("Columns of the file: ", list(df.columns))
    x = input("Enter column:")
    X = (df.loc[:, x])
    plt.xlabel(x+" (binned)")
    plt.ylabel("count of "+x)
    print("Histogram displayed")
    plt.hist(X, bins=21)
    # plt.savefig("hist.jpg")
    plt.show()

def time(file):
    data = pd.read_csv(file)
    df = pd.DataFrame(data)
    print("Columns of the file: ", list(df.columns))
    x = input("Enter xcol:")
    df=df.set_index(x)
    plt.xlabel(x)
    y = input("Enter column:")
    Y = df.loc[:, y]
    plt.ylabel(y)
    print("Time Series displayed")
    plt.plot(Y,marker="o")
    plt.tight_layout()
    # plt.savefig("time.jpg")
    plt.show()

file=input("Enter file path with name:")
time(file)