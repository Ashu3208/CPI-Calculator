import pandas as pd

def convert_grade_to_points(grade):
    grade_points = {
        'A': 10, 'B+': 9, 'B': 8, 'C+': 7, 'C': 6, 'D+': 5, 'D': 4, '0': 0
    }
    return grade_points.get(grade, 0)

def calculate_cpi(grades, credits):
    total_credits = sum(credits)
    weighted_grades_sum = sum(credits[i] * convert_grade_to_points(grade) for i, grade in enumerate(grades))
    
    if total_credits == 0:
        return 0.0
    else:
        return weighted_grades_sum / total_credits

if __name__ == "__main__":
    # Replace "path/to/your/excel_file.xlsx" with the actual path to your Excel file.
    excel_file_path = "path/to/your/excel_file.xlsx"

    df = pd.read_excel(excel_file_path)

    grades = df['Grades'].tolist()
    credits = df['Credits'].tolist()

    # Calculate the CPI
    cpi = calculate_cpi(grades, credits)

    print(f"The CPI is: {cpi:.2f}")
