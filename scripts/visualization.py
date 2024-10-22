# visualization.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

SAVE_DIR = 'reports/figures/'
DPI_VALUE = 900

def save_and_show_plot(fig: plt.Figure, filename: str) -> None:
    """
    Save a figure as an image and display it.
    """
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    fig.savefig(os.path.join(SAVE_DIR, filename), format='jpeg', dpi=DPI_VALUE)
    plt.show()

def plot_histogram(df: pd.DataFrame, column: str, title: str, xlabel: str, filename: str) -> None:
    """
    Plot and save a histogram for a specified column.
    """
    fig = plt.figure(figsize=(8, 6))
    sns.histplot(df[column], bins=20, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    save_and_show_plot(fig, filename)

def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str, filename: str) -> None:
    """
    Plot and save a scatter plot for two specified columns.
    """
    fig = plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x_col, y=y_col, data=df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    save_and_show_plot(fig, filename)
