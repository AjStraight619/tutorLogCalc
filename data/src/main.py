import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

# Define file_paths as a global variable
file_paths = []

def save_output_to_txt(tutored_counts):
    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if output_file_path:
        with open(output_file_path, "w") as file:
            file.write("Subject_General\tSubject\tTutored\tTutored Percentage\n")
            for _, row in tutored_counts.iterrows():
                file.write(f"{row['Subject_General']}\t{row['Subject']}\t{row['Tutored']}\t{row['Tutored Percentage']:.2f}%\n")

def process_excel_files():
    global file_paths # Access the global file_paths variable
    result_list = []
    for file_path in file_paths:
        data = pd.read_excel(file_path, usecols=['Subject'])

        # Define the pattern for filtering the desired subjects and sections
        pattern = r'(Math\s*\d+)|(Computer Science\s*\d+)|(CS\s*\d+)|(Chemistry\s*\d+)|(Physics\s*\d+)|(Phys\s*\d+)'

        # Filter rows with subjects containing any of the specified patterns
        matched_classes = data[data['Subject'].str.contains(pattern, case=False, na=False)]

        # Count the number of occurrences of each subject and store in a new dataframe
        class_counts = matched_classes['Subject'].value_counts().reset_index()
        class_counts.columns = ['Subject', 'Tutored']

        # Calculate the total number of students for each subject (ignoring the section number)
        total_students = matched_classes['Subject'].str.extract(r'([A-Za-z]+)\s*\d+', expand=False).value_counts().reset_index()
        total_students.columns = ['Subject_General', 'Total Students']

        # Extract the general subject from the subject column
        class_counts['Subject_General'] = class_counts['Subject'].str.extract(r'([A-Za-z]+)\s*\d+', expand=False)

        # Merge the class counts and total students dataframes
        merged_df = pd.merge(class_counts, total_students, on='Subject_General')

        # Calculate the percentage of students tutored in each subject and store in a new column
        merged_df['Tutored Percentage'] = merged_df['Tutored'] / merged_df['Total Students'] * 100

        # Append the matched classes to the result list
        result_list.append(merged_df)

    # Concatenate all the dataframes in the result list into a single dataframe
    combined_result = pd.concat(result_list, axis=0, ignore_index=True)

    # Aggregate the tutored counts and percentages by subject
    tutored_counts = combined_result.groupby(['Subject_General', 'Subject']).agg({'Tutored': 'sum', 'Tutored Percentage': 'mean'}).reset_index()

    # Display the tutored counts and percentages
    print(tutored_counts)
    save_output_to_txt(tutored_counts)
def browse_file():
    global file_paths # Access the global file_paths variable
    new_file_paths = filedialog.askopenfilenames(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    if new_file_paths:
        file_paths.extend(new_file_paths) # Append the new file paths to the global file_paths list

def browse_folder():
    global file_paths # Access the global file_paths variable
    folder_path = filedialog.askdirectory()
    if folder_path:
        new_file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx') or f.endswith('.xls')]
        if new_file_paths:
            file_paths.extend(new_file_paths) # Append the new file paths to the global file_paths list

# Create Tkinter
root = tk.Tk()
root.title("Tutor Log Analyzer")

# Create browse buttons
browse_file_button = tk.Button(root, text="Browse Excel File", command=browse_file)
browse_file_button.pack(padx=20, pady=10)

browse_folder_button = tk.Button(root, text="Browse Folder", command=browse_folder)
browse_folder_button.pack(padx=20, pady=10)

# Create process button
process_button = tk.Button(root, text="Process Files", command=process_excel_files)
process_button.pack(padx=20, pady=10)
root.mainloop()



