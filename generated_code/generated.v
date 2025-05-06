module TOP_CASEZ(CLK, RST, cnt);
  input CLK, RST;
  output reg [7:0] cnt;

  always @(posedge CLK) begin
    if (RST) begin
      cnt <= 0;
    end else begin
      casez(cnt)
        8'b00000000: begin
          cnt <= cnt + 1;
        end
        8'b1???????: begin
          cnt <= 0;
        end
        default: begin
          cnt <= cnt + 1;
        end
      endcase
    end
  end
endmodule
