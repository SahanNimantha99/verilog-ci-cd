import subprocess

def run_icarus():
    verilog_file = "generated_code/generated.v"
    testbench_file = "generated_code/testbench.v"
    
    # Compile the Verilog module with the testbench
    compile_cmd = ["iverilog", "-o", "sim.out", verilog_file, testbench_file]
    compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)

    if compile_result.returncode != 0:
        print(f"❌ Compilation Failed:\n{compile_result.stderr}")
        return

    # Run the simulation
    run_cmd = ["vvp", "sim.out"]
    run_result = subprocess.run(run_cmd, capture_output=True, text=True)

    print(f"✅ Simulation Output:\n{run_result.stdout}")

if __name__ == "__main__":
    run_icarus()
