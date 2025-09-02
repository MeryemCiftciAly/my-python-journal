# Expense Claims Automation with Python

## Objective
This project demonstrates how a very common office workflow handling time and expense claims can be **automated with Python**.  

The idea is simple: instead of manually cleaning, categorizing, and preparing spreadsheets, you can drop in any expense file (.xlsx or .csv) and let Python handle the repetitive tasks.  

For this particular dataset:

- The data was already mostly clean, with only **missing items** to handle.
- In real-world cases, the same Python workflow could be extended to handle **messy or inconsistent datasets**.

---

## Step 1: Interactive Google Colab Demo (Cleaning & Categorization)
Explore the automated workflow in action. You can run this demo in Google Colab (view-only) or make a copy to experiment in your own Google Drive.  

**Workflow in Google Colab:**

1. **Input Data** → An expense claims Excel file.  
2. **Cleaning** → Handle missing values (minimal in this case).  
3. **Categorization** → Group expenses based on business needs:  
   - By **year** and **month**  
   - By **status** (e.g., Approved, Pending)  
   - By **currency**  
   - By **amount**  
4. **Output** → A single automated Excel workbook with **three tabs**:  
   - Tab 1: Aggregated/Categorized Expenses    
   - Tab 2: Aggregated/Categorized Expenses  
   - Tab 3: Structured view **similar to a PivotTable layout** for further insights  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aqRNsm6KMZVxQ07LoNU97_tDhksFIriX?usp=sharing&utm_source=chatgpt.com)

---

## Step 2: Tableau Dashboard
Once the Python workflow has generated the structured spreadsheets, you can visualize and explore the data in Tableau.  

- **Tableau Dashboard README & User Guide / Guided Analysis**  
  [Link to Tableau README & Dashboard Guide]()

---

## Why This Matters
- Saves time by **automating repetitive expense report preparation**.  
- Produces spreadsheets already organized into a **PivotTable-like structure**, making them easier to analyze.  
- Provides a solid foundation for further use in **Power BI, Tableau, or other BI tools**.  

---

## Repository Contents
- `scripts/clean_expenses.py` → Python script version of the workflow  
- `requirements.txt` → Python dependencies  
- `data` → dataset for reference  
- `README.md` → Project overview (this file)  

---

☺🌴 This project shows how **simple automation with Python** can transform a routine administrative task into a streamlined, analysis-ready process.

---

## Show & Tell / Job Search - September 2025
This project is part of my **show and tell of skills** as I am currently **job searching as of September 2nd, 2025**.  

If you would like me to be part of your team, or if you are an **individual or SME** looking to collaborate on your **data-driven projects**, or if you are a **recruiter or company** seeking to hire someone for a **data analytics role**, please **contact me**. I would be happy to discuss how I can contribute to your projects or team.
