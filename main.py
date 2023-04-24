import subprocess
import sys

def run_script(script_path):
    result = subprocess.run([sys.executable, script_path], check=True)
    return result.returncode == 0

if __name__ == "__main__":
    plot_path = "plot.py"
    table_path = "table.py"
    readme_path = "readme.py"

    if run_script(plot_path):
        print(f"{plot_path} finished successfully.")
    else:
        print(f"{plot_path} failed to execute.")

    if run_script(table_path):
        print(f"{table_path} finished successfully.")
    else:
        print(f"{table_path} failed to execute.")
        
    if run_script(readme_path):
        print(f"{readme_path} finished successfully.")
    else:
        print(f"{readme_path} failed to execute.")
