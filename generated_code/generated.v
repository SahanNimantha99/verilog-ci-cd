module up_counter (
  input clk,   // clock signal
  input load,  // load enable signal
  input [3:0] data, // data to be loaded into the counter
  output reg [3:0] count   // output of the counter
);

always @(posedge clk) begin
  if (load) begin
    count <= data;
  end else begin
    count <= count + 1'b1;
  end
end

endmodule
