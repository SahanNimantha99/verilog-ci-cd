import subprocess

def run_verilator(file):
    result = subprocess.run(["verilator", "--lint-only", file], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{file}: ✅ Linting successful!")
    else:
        print(f"{file}: ❌ Linting failed!\n{result.stderr}")

if __name__ == "__main__":
    run_verilator("generated_code/generated.v")
