import subprocess

def run_script(script_path):
    result = subprocess.run(['python', script_path], check=True)
    return result.returncode == 0

if __name__ == "__main__":
    plot_path = "plot.py"
    table_path = "table.py"

    # Run script1.py
    if run_script(plot_path):
        print(f"{plot_path} finished successfully.")
    else:
        print(f"{plot_path} failed to execute.")

    # Run csv_to_markdown.py
    if run_script(table_path):
        print(f"{table_path} finished successfully.")
    else:
        print(f"{table_path} failed to execute.")
