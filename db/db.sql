-- Create main student table
CREATE TABLE IF NOT EXISTS student_records (
    student_id TEXT PRIMARY KEY,
    name TEXT,
    program TEXT,
    gpa REAL,
    term_status TEXT,
    enrollment_status TEXT
);

-- Create issue log table
CREATE TABLE IF NOT EXISTS issue_log (
    issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    issue_description TEXT,
    date_logged TEXT
);

-- Sample query for Power BI
SELECT
    sr.program,
    sr.term_status,
    COUNT(il.issue_id) AS issue_count
FROM student_records sr
LEFT JOIN issue_log il ON sr.student_id = il.student_id
GROUP BY sr.program, sr.term_status;
