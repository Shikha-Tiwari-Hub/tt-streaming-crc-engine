`default_nettype none

module tt_um_streaming_crc (
    input  wire [7:0] ui_in,    // Data input
    output wire [7:0] uo_out,   // CRC output
    input  wire [7:0] uio_in,   // Control
    output wire [7:0] uio_out,  // Status
    output wire [7:0] uio_oe,   // Output enable
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Control signals
    wire valid_in = uio_in[0];
    wire restart  = uio_in[1];

    // CRC register (8-bit)
    reg [7:0] crc;

    // Simple CRC update logic (polynomial 0x07)
    wire feedback = crc[7] ^ ui_in[7];

    wire [7:0] crc_next = {
        crc[6],
        crc[5],
        crc[4] ^ feedback,
        crc[3] ^ feedback,
        crc[2] ^ feedback,
        crc[1],
        crc[0],
        feedback
    };

    // Sequential logic
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            crc <= 8'hFF;
        else if (!ena)
            crc <= crc;
        else if (restart)
            crc <= 8'hFF;
        else if (valid_in)
            crc <= crc_next;
    end

    // Outputs
    assign uo_out = crc;

    // Status signals
    assign uio_out[0] = ena;       // ready
    assign uio_out[1] = valid_in;  // valid
    assign uio_out[7:2] = 6'b0;

    // Enable only first 2 bits as outputs
    assign uio_oe = 8'b00000011;

endmodule
