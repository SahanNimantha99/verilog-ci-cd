import subprocess
import os

def run_icarus():
    """
    Compiles and runs the PWM generator simulation using Icarus Verilog (iverilog).
    """

    verilog_file = "generated_code/generated.v"
    testbench_file = "generated_code/testbench.v"
    simulation_output = "simv"
    waveform_file = "wave.vcd"

    # Step 1: Compile the Verilog design with the testbench
    compile_cmd = ["iverilog", "-o", simulation_output, verilog_file, testbench_file]
    compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)

    if compile_result.returncode != 0:
        print(f"❌ Compilation Failed:\n{compile_result.stderr}")
        return

    print(f"✅ Compilation Successful! Running simulation...\n")

    # Step 2: Run the compiled simulation
    run_cmd = ["vvp", simulation_output]
    run_result = subprocess.run(run_cmd, capture_output=True, text=True)

    print(f"✅ Simulation Output:\n{run_result.stdout}")

    # Step 3: Check if wave.vcd exists (for GTKWave debugging)
    if os.path.exists(waveform_file):
        print(f"📊 Waveform file '{waveform_file}' generated. View it using:\n    gtkwave {waveform_file}")

if __name__ == "__main__":
    run_icarus()
