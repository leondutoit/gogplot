
import subprocess
import pandas as pd

def gogplot(df, expression):
    """
    Creates a ggplot2 plot from pandas DataFrame.
    In the plot expression, the DataFrame _must_ be referred to as `data`.
    E.g. gogplot(df, 'ggplot(data, aes(x, y)) + geom_line()')
    :param df: pandas DataFrame
    :param expression: ggplot2 plot specification
    """
    df.to_csv("d.csv")
    plot = "library(ggplot2);data<-read.csv('d.csv');pdf(print(" + expression + "))"
    subprocess.call(["R", "--slave", "-e", plot])
    subprocess.call(["open", "Rplots.pdf"])
    subprocess.call(["rm", "d.csv"])
    pass

