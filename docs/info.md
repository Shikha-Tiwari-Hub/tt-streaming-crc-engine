<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works
This project implements a simple 8-bit streaming CRC (Cyclic Redundancy Check) generator.

The design takes an 8-bit data input (ui_in) and updates an internal CRC register on every valid input cycle. The CRC is computed using a lightweight polynomial (0x07) optimized for low-area ASIC implementation.

**Control signals**:
- VALID_IN (uio[0]): When high, the input data is processed and the CRC is updated.
- RESTART (uio[1]): Resets the CRC register to its initial value (0xFF).

The current CRC value is continuously available on the output pins (uo_out[7:0]).

The design is fully synchronous and operates on the rising edge of the clock.

## How to test

1. Apply reset:
   - Set rst_n = 0 → CRC resets to 0xFF
   - Set rst_n = 1 to begin operation

2. Restart CRC (optional):
   - Set RESTART (uio[1]) = 1 for one clock cycle
   - CRC resets to initial value (0xFF)

3. Provide input data:
   - Place an 8-bit value on ui_in[7:0]
   - Set VALID_IN (uio[0]) = 1 for one clock cycle

4. Observe output:
   - CRC result appears on uo_out[7:0]
   - Each valid input updates the CRC

5. Repeat:
   - Continue sending data bytes with VALID_IN pulses
   - CRC updates sequentially

Example:
- Input sequence: 0x12 → 0x34 → 0x56
- CRC updates after each clock cycle when VALID_IN is high

## External hardware
No external hardware is required.

The design is fully self-contained and can be tested using:
- Simulation (Cocotb + Icarus Verilog)
- Tiny Tapeout test infrastructure

Optional:
- LEDs can be connected to uo_out[7:0] to visualize CRC output
- Switches/buttons can be used to drive ui_in and control signals
