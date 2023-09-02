# Tutor Log Analyzer

## Overview

Tutor Log Analyzer is a desktop application built with Python's Tkinter library. It provides a quick and efficient way to process multiple Excel files containing tutor logs. The application scans these files, filters out specific subjects, and calculates the number of tutored students and the percentage of students tutored in each subject. Results are saved in a text file for further analysis.

## Features

- **Excel File Processing**: Load one or multiple Excel files to process.
  
- **Folder Browsing**: Option to browse and select an entire folder containing Excel files for batch processing.

- **Regex-based Filtering**: Utilizes regular expressions to filter classes based on the subjects like Math, Computer Science, Chemistry, and Physics.
  
- **Data Aggregation**: Calculates the number of tutored sessions and the average percentage of students tutored across multiple files.

- **Output**: Saves the processed counts and percentages in a text file.

## Libraries Used

- **Tkinter**: Python's standard GUI (Graphical User Interface) package.
  
- **Pandas**: Data analysis and manipulation library.
  
- **os**: In-built Python library for interacting with the operating system.

