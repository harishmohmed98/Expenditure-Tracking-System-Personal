import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )
    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        return cursor.fetchall()


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def insert_expense(expense_date, amount, category, notes):
    logger.info(
        f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def fetch_expense_summary(start_date, end_date, top_n=None, min_amount=None):
    logger.info(
        f"fetch_expense_summary called with start: {start_date}, end: {end_date}, top_n: {top_n}, min_amount: {min_amount}")
    query = '''SELECT category, SUM(amount) as total 
               FROM expenses WHERE expense_date BETWEEN %s and %s'''
    params = [start_date, end_date]

    if min_amount:
        query += " AND amount >= %s"
        params.append(min_amount)

    query += " GROUP BY category ORDER BY total DESC"

    if top_n:
        query += " LIMIT %s"
        params.append(top_n)

    with get_db_cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()


def fetch_monthly_expense_summary(top_n=None, min_amount=None):
    logger.info(f"fetch_monthly_expense_summary called with top_n: {top_n}, min_amount: {min_amount}")
    query = '''SELECT month(expense_date) as expense_month, 
                      monthname(expense_date) as month_name,
                      sum(amount) as total FROM expenses'''
    params = []

    if min_amount:
        query += " WHERE amount >= %s"
        params.append(min_amount)

    query += " GROUP BY expense_month, month_name ORDER BY total DESC"

    if top_n:
        query += " LIMIT %s"
        params.append(top_n)

    with get_db_cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()
