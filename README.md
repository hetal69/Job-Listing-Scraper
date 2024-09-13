# Job Listings Scraper for Glassdoor

The "Job Listings Scraper for Glassdoor" is a Python-based project that automates the extraction of job data from Glassdoor. Using Selenium for web automation, the script navigates through job listings and extracts relevant information based on user-defined search criteria. The data is then stored in a CSV file for easy analysis.

**Key Features:**

   **Web Scraping & Automation:**
   Utilizes Selenium to automate navigation and data extraction from Glassdoor’s website. 
   Includes efficient page handling and dynamic scraping across multiple pages.
   
   **Data Extraction & Analysis:**
   Extracts key details such as company name, job title, location, salary estimate, and   
   job description.
   Handles job descriptions with HTML parsing and error management for robust extraction.

   **Data Cleaning & Processing:**
   Uses Pandas to clean and process data, including removing duplicates, handling salary   
   ranges, and calculating average salaries.
   Cleans and organizes company names, ratings, job titles, and seniority levels.

   **File Export & Reporting:**
   Exports scraped job data to CSV format for further analysis.
   Prepares cleaned datasets for job distribution analysis by location, industry, and job     category.

**Tools & Libraries:**

   **Python:** For scripting and data management.
   **Selenium:** For web scraping and browser automation.
   **Pandas:** For data cleaning and CSV file handling.

**How It Works:**

   **Script Setup:** Configures Selenium to open a browser, handle user inputs, and set search parameters for jobs.
   **Job Search & Scraping:** The script navigates to Glassdoor page (https://www.glassdoor.com/Job/index.htm) and iterates over job listings, extracting data and handling pop-ups or navigational elements.
   **Data Processing:** Data is cleaned and transformed, removing duplicates and preparing the dataset for analysis.
   **CSV Export:** The job data is saved into a CSV file, making it accessible for future analysis.

**Data Insights:**

   Analyze job distributions, salary estimates, and company information to derive insights on industry trends.
   Simplified job titles and seniority levels provide a clearer understanding of job market segments.
