
import subprocess
import pandas as pd

def gogplot(df, expression):
    """
    Creates a ggplot2 plot from pandas DataFrame.
    :param df: pandas DataFrame
    :param expression: ggplot2 plot specification
    """
    df.to_csv("d.csv")
    plot = "library(ggplot2);d<-read.csv('d.csv');pdf(print(" + expression + "))"
    subprocess.call(["R", "--slave", "-e", plot])
    subprocess.call(["open", "Rplots.pdf"])
    subprocess.call(["rm", "d.csv"])
    pass
