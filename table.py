import csv
import sys

def csv_to_markdown_table(csv_file_path):
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        table_header = "| " + " | ".join(header) + " |\n"

        separator_row = "| " + " | ".join(["---" for _ in header]) + " |\n"

        table_body = ""
        for row in reader:
            table_body += "| " + " | ".join(row) + " |\n"

        markdown_table = table_header + separator_row + table_body

        return markdown_table

def write_to_file(output_file, content):
    with open(output_file, "w") as file:
        file.write(content)

if __name__ == "__main__":
    input_csv = "results.csv"
    output_md = "results.md"

    markdown_table = csv_to_markdown_table(input_csv)
    write_to_file(output_md, markdown_table)

    print(f"Markdown table has been generated and saved to {output_md}")