"""
This module provides functions for saving diagrams as html files
There are 2 types of diagrams - bar plot and line diagram
"""
import os
import plotly.graph_objects as go
import itertools
from collections import defaultdict
from src.expense import Expense
from src.file_manager import OUTPUT_DIR
from datetime import datetime

def draw_spending_graph(expenses: list[Expense]) -> None:
    sorted_expenses = sorted(expenses, key = lambda expense: expense.date)
    y_cumulative_spending = list(itertools.accumulate(map(lambda expense: expense.amount, sorted_expenses)))
    x_date = map(lambda expense: expense.date, expenses)
    
    figure = go.Figure(data=go.Scatter(x=list(x_date), y=y_cumulative_spending, mode='lines+markers'))
    file_name = os.path.join(OUTPUT_DIR, f'{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.html')
    figure.write_html(file_name)

def draw_diagram_by_categories(expenses: list[Expense]) -> None:
    amount_category_pair = [(expense.amount, expense.category) for expense in expenses]
    amount_by_categories: defaultdict[str, float] = defaultdict(float)
    
    for amount, category in amount_category_pair:
        amount_by_categories[category] += amount

    figure = go.Figure(data=go.Bar(x=list(amount_by_categories.keys()), y=list(amount_by_categories.values())))
    file_name = os.path.join(OUTPUT_DIR, f'{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.html')
    figure.write_html(file_name)