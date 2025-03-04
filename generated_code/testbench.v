module up_counter_tb ();

reg clk; // clock signal
reg load; // load enable signal
reg [3:0] data; // data to be loaded into the counter
wire [3:0] count; // output of the counter

// Instantiate the up_counter module
up_counter uut (
  .clk(clk),
  .load(load),
  .data(data),
  .count(count)
);

// Clock generation
always #5 clk = ~clk;

initial begin
  // Initialize inputs
  clk = 1'b0;
  load = 1'b0;
  data = 4'b0;

  #10;

  // Load value into counter
  load = 1'b1;
  data = 4'b0001;
  #10 load = 1'b0;

  // Let counter increment for a few cycles
  #50;

  // Display result
  $display("Count: %d", count);

  $finish;
end

endmodule
