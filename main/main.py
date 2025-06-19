import pandas as pd
import sqlite3
from datetime import datetime

# --- Database connection ---
conn = sqlite3.connect("student_records.db")
cursor = conn.cursor()

# --- Load student data from DB ---
def load_data():
    query = "SELECT * FROM student_records;"
    df = pd.read_sql_query(query, conn)
    return df

# --- Identify discrepancies ---
def detect_issues(df):
    issues = []

    for index, row in df.iterrows():
        if pd.isna(row['program']) or pd.isna(row['term_status']):
            issues.append((row['student_id'], 'Missing Program or Term Status'))
        elif row['gpa'] < 2.0 and row['term_status'] != 'At Risk':
            issues.append((row['student_id'], 'Low GPA but not flagged'))
        elif row['enrollment_status'] == 'Dropped' and row['term_status'] != 'Inactive':
            issues.append((row['student_id'], 'Dropped student marked as Active'))
    
    return issues

# --- Log issues to DB ---
def log_issues(issues):
    for student_id, issue in issues:
        cursor.execute("""
            INSERT INTO issue_log (student_id, issue_description, date_logged)
            VALUES (?, ?, ?)
        """, (student_id, issue, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

# --- Main Execution ---
if __name__ == "__main__":
    df = load_data()
    issues = detect_issues(df)
    log_issues(issues)
    print(f"Issues logged: {len(issues)}")
