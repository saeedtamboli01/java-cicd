import subprocess
import re

CODE_PATH = "."
REPORT_FILE = "report.txt"

def run_pylint():
    result = subprocess.run(
        ["/usr/local/bin/pylint", CODE_PATH],
        capture_output=True,
        text=True
    )
    with open(REPORT_FILE, "w") as f:
        f.write(result.stdout)
        f.write(result.stderr)
    return result.stdout

def extract_score(output):
    match = re.search(r"Your code has been rated at (-?\d+(\.\d+)?)/10", output)
    if match:
        return float(match.group(1))
    return 0.0

if __name__ == "__main__":
    pylint_output = run_pylint()
    score = extract_score(pylint_output)
    print(score)   # Jenkins console log will show only the score
