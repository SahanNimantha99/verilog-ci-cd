module counter (
    input clk, reset,
    output reg [3:0] count
);
always @(posedge clk or posedge reset) begin
    if (reset)
        count <= 4'b0000;  // ✅ Correct Reset (set to 0)
    else
        count <= count + 1; // ✅ Correct Increment (increment by 1)
end
endmodule
