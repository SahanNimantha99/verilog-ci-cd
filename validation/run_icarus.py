import subprocess

def run_icarus(file):
    compile_cmd = ["iverilog", "-o", "sim.out", file]
    run_cmd = ["vvp", "sim.out"]

    compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)
    if compile_result.returncode != 0:
        print(f"❌ Compilation Failed: {compile_result.stderr}")
        return

    run_result = subprocess.run(run_cmd, capture_output=True, text=True)
    print(f"✅ Simulation Output:\n{run_result.stdout}")

if __name__ == "__main__":
    run_icarus("generated_code/generated.v")
