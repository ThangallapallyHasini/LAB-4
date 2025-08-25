import csv

def analyze_csv_file(file_path):
    """
    Analyzes a CSV file and returns:
    - Total number of rows
    - Number of empty rows
    - Total number of words
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
        
        total_rows = len(rows)
        empty_rows = 0
        total_words = 0
        
        for row in rows:
            # Check if row is empty
            if not row or all(cell.strip() == '' for cell in row):
                empty_rows += 1
            
            # Count words in each cell
            for cell in row:
                if cell.strip():
                    words = cell.split()
                    total_words += len(words)
        
        return {
            'total_rows': total_rows,
            'empty_rows': empty_rows,
            'total_words': total_words
        }
        
    except FileNotFoundError:
        print("❌ File not found! Please check the file path.")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None

def main():
    print("CSV File Analyzer")
    print("=" * 20)
    
    while True:
        # Get file path from user
        file_path = input("\nEnter CSV file path (or 'quit' to exit): ").strip()
        
        if file_path.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not file_path:
            print("Please enter a valid file path")
            continue
        
        # Analyze the CSV file
        results = analyze_csv_file(file_path)
        
        if results:
            print("\n📊 Analysis Results:")
            print("-" * 20)
            print(f"📈 Total Rows: {results['total_rows']}")
            print(f"🚫 Empty Rows: {results['empty_rows']}")
            print(f"📚 Total Words: {results['total_words']}")
            print(f"📝 Non-empty Rows: {results['total_rows'] - results['empty_rows']}")
            print("-" * 20)

# Run the program
if __name__ == "__main__":
    # Create a sample CSV file for testing
    sample_data = [
        ["Name", "Age", "City"],
        ["John", "25", "New York"],
        ["Alice", "30", "London"],
        ["", "", ""],  # Empty row
        ["Bob", "35", "Paris"],
        ["Charlie", "28", "Berlin"]
    ]
    
    # Write sample CSV
    with open('test.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)
    
    print("✅ Sample CSV file 'test.csv' created successfully!")
    print("You can now use 'test.csv' as input or any other CSV file.")
    print("-" * 50)
    
    main()