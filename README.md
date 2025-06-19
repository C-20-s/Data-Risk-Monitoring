<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  
</head>
<body>

  <h1>📊 Reference Data Risk Monitoring & Issue Resolution Tracker</h1>

  <p>This project helps detect and log mismatches in student academic records (entry, dropout, GPA issues) using Python and SQL. The outputs are prepared for use in Power BI dashboards for risk analysis and early intervention.</p>

  <h2>🔧 Tools Used</h2>
  <ul>
    <li>Python (Pandas, SQLite3)</li>
    <li>SQL (SQLite)</li>
    <li>Power BI (for dashboards)</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <ul>
    <li><code>main.py</code> – Python script to run validations and log issues</li>
    <li><code>sql_queries.sql</code> – SQL code to create tables and query data</li>
    <li><code>student_records.db</code> – SQLite database (auto-created)</li>
  </ul>

  <h2>▶️ How to Run</h2>

  <h3>1. Setup your environment</h3>
  <p>Ensure you have Python 3.x installed. Install pandas if not already available:</p>
  <pre>pip install pandas</pre>

  <h3>2. Initialize the database</h3>
  <p>Run the <code>CREATE TABLE</code> statements in <code>sql_queries.sql</code> using a SQLite client or add them inside <code>main.py</code> for first-time setup.</p>
  <p>Optionally, insert mock student data into <code>student_records</code>.</p>

  <h3>3. Run the tracker</h3>
  <p>Execute the Python script to find and log data quality issues:</p>
  <pre>python main.py</pre>
  <p>This will populate the <code>issue_log</code> table with detected mismatches.</p>

  <h3>4. Analyze in Power BI</h3>
  <p>Use the following SQL query from <code>sql_queries.sql</code> to get summary output:</p>
  <pre>
SELECT
    sr.program,
    sr.term_status,
    COUNT(il.issue_id) AS issue_count
FROM student_records sr
LEFT JOIN issue_log il ON sr.student_id = il.student_id
GROUP BY sr.program, sr.term_status;
  </pre>
  <p>Load this result into Power BI to create visuals like:</p>
  <ul>
    <li>Bar chart: Program vs. Issue Count</li>
    <li>Filters: GPA range, term status</li>
    <li>Conditional formatting: Highlight high-risk programs</li>
  </ul>

  <h2>✅ Validation Rules</h2>
  <ul>
    <li>Missing program or term status</li>
    <li>GPA &lt; 2.0 not flagged as "At Risk"</li>
    <li>Dropped students still marked "Active"</li>
  </ul>

  <div class="note">
    <strong>Note:</strong> This setup uses SQLite for simplicity. For larger systems, consider PostgreSQL or MySQL. You can also schedule the Python script using CRON or Airflow.
  </div>

</body>
</html>
