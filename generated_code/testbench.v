`timescale 1ns / 1ps

module tb_TOP_CASEZ;
    reg CLK;
    reg RST;
    wire [7:0] cnt;

    // Instantiate the TOP_CASEZ module
    TOP_CASEZ uut (
        .CLK(CLK),
        .RST(RST),
        .cnt(cnt)
    );

    // Clock generation: 10ns period (100 MHz)
    always begin
        #5 CLK = ~CLK;
    end

    // Test cases
    initial begin
        CLK = 0;
        RST = 1;  // Apply reset
        $display("Starting TOP_CASEZ Testbench...");
        $dumpfile("top_casez_tb.vcd");
        $dumpvars(0, tb_TOP_CASEZ);
        
        #10 RST = 0;  // Release reset

        #100 RST = 1; // Apply reset again
        #10  RST = 0; // Release reset

        // Let the counter run
        #200;

        $display("Testbench completed.");
        $finish;
    end

    // Monitor outputs
    initial begin
        $monitor("Time: %0t | CLK: %b | RST: %b | cnt: %h", $time, CLK, RST, cnt);
    end
endmodule
