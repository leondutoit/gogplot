
import subprocess
import pandas as pd

def gogplot(df, expression):
    """
    Creates a ggplot2 plot from pandas DataFrame.
    In the plot expression, the DataFrame _must_ be referred to by the same name
    as the variable that stores DataFrame in python.
    E.g. gogplot(df, 'ggplot(df, aes(x, y)) + geom_line()')
    :param df: pandas DataFrame
    :param expression: ggplot2 plot specification
    """
    df_name = locals().keys()[0]
    df.to_csv("d.csv")
    get_plot_data = "library(ggplot2);%s<-read.csv('d.csv');" % df_name
    print_plot = "pdf(print(%s))" % expression
    plot = ''.join([get_plot_data, print_plot])
    subprocess.call(["R", "--slave", "-e", plot])
    subprocess.call(["open", "Rplots.pdf"])
    subprocess.call(["rm", "d.csv"])
    pass
