# Expenditure Tracking System - Personal

## Description
This is a Python-based web application that tracks and analyzes expenses. This version is designed for **personal use** but can be easily modified into a **commercial office version** for business expense tracking.

## Project Structure
- **frontend/**: Contains the Streamlit application code for the user interface.
- **backend/**: Contains the FastAPI backend server code that handles data processing and storage.
- **tests/**: Contains test cases for both frontend and backend to ensure reliability.
- **requirements.txt**: Lists the required Python packages for setting up the application.
- **README.md**: Provides an overview and setup instructions for the project.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/expense-management-system.git
cd expense-management-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI Server
```bash
uvicorn server.server:app --reload
```

### 4. Run the Streamlit Application
```bash
streamlit run frontend/app.py
```

## Features
- **Expense Entry:** Add and update personal expenses.
- **Expense Analytics:** View expenses by category and time period.
- **Visual Charts & Reports:** Get graphical insights into spending habits.
- **Modular Design:** Easily adaptable for office or commercial expense tracking.

## Future Enhancements
- **User Authentication:** Secure login for multiple users.
- **Multi-Currency Support:** Track expenses in different currencies.
- **Export Reports:** Download expense summaries as PDFs or CSV files.

For contributions and support, feel free to submit issues or pull requests!

