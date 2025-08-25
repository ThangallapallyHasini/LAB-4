def analyze_csv_manual():
    print("Enter CSV rows one by one. Enter a blank line to finish.")
    rows = []
    while True:
        row = input()
        if row == "":
            break
        rows.append(row.split(','))

    total_rows = len(rows)
    empty_rows = sum(1 for row in rows if all(cell.strip() == '' for cell in row))
    word_count = sum(len(cell.split()) for row in rows for cell in row)

    print(f"Total rows: {total_rows}")
    print(f"Empty rows: {empty_rows}")
    print(f"Total words: {word_count}")

analyze_csv_manual()