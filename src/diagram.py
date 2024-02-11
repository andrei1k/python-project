'''
This module provides functions for saving diagrams as html files
There are 2 types of diagrams - bar plot and line diagram
'''
import os
import itertools
from collections import defaultdict
from datetime import datetime
import plotly.graph_objects as go
from src.expense import Expense
from src.file_manager import OUTPUT_DIR

def save_spending_graph(expenses: list[Expense]) -> None:
    '''
    Generates and saves a spending graph based on the provided list of expenses.

    :param expenses: A list of Expense objects representing the expenses.

    :return: None. The function saves the generated graph as an HTML file.
    '''
    sorted_expenses = sorted(expenses, key = lambda expense: expense.date)
    y_cumulative_spending = list(itertools.accumulate
                                 (map(lambda expense: expense.amount, sorted_expenses)))
    x_date = map(lambda expense: expense.date, expenses)

    figure = go.Figure(data=go.Scatter(x=list(x_date),
                                       y=y_cumulative_spending, mode='lines+markers'))
    file_name = os.path.join(OUTPUT_DIR,
                             f'{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.html')
    figure.write_html(file_name)

def save_diagram_by_categories(expenses: list[Expense]) -> None:
    '''
     Generates and saves a bar plot depicting expenses grouped by categories.

    :param expenses: A list of Expense objects representing the expenses.

    :return: None. The function saves the generated bar plot as an HTML file.
    '''
    amount_category_pair = [(expense.amount, expense.category) for expense in expenses]
    amount_by_categories: defaultdict[str, float] = defaultdict(float)

    for amount, category in amount_category_pair:
        amount_by_categories[category] += amount

    figure = go.Figure(data=go.Bar(x=list(amount_by_categories.keys()),
                                   y=list(amount_by_categories.values())))
    file_name = os.path.join(OUTPUT_DIR, f'{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.html')
    figure.write_html(file_name)
