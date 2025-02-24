`timescale 1ns/1ps
module testbench;
    reg clk, reset;
    wire [3:0] count;

    // Instantiate the counter module
    counter uut (
        .clk(clk),
        .reset(reset),
        .count(count)
    );

    // Clock generation
    always #5 clk = ~clk;  // Toggle clock every 5ns

    initial begin
        $dumpfile("testbench.vcd"); // Enable waveform output
        $dumpvars(0, testbench);

        // Initialize signals
        clk = 0;
        reset = 1;
        #10; // Keep reset high for 10 time units

        reset = 0;
        #100; // Let the counter run for 100 time units

        $finish; // End simulation
    end

    // Monitor output
    always @(posedge clk) begin
        $display("Time=%0t | Count=%d", $time, count);
    end
endmodule
