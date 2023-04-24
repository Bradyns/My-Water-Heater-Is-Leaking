def insert_table_to_readme(readme_path, results_path, marker):
    with open(readme_path, "r") as readme_file:
        readme_content = readme_file.read()

    with open(results_path, "r") as results_file:
        results_content = results_file.read()

    if marker not in readme_content:
        print(f"Error: Marker '{marker}' not found in {readme_path}")
        return

    new_readme_content = readme_content.replace(marker, results_content)

    with open(readme_path, "w") as readme_file:
        readme_file.write(new_readme_content)

    print(f"Table from {results_path} has been inserted into {readme_path}")

if __name__ == "__main__":
    readme_path = "README.md"
    results_path = "results.md"
    marker = "<!-- INSERT_TABLE_HERE -->"

    insert_table_to_readme(readme_path, results_path, marker)