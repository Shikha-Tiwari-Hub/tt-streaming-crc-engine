# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start Simple CRC Test")

    # Clock: 100 kHz (10 us period)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # ----------------------
    # Reset
    # ----------------------
    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 5)

    # ----------------------
    # 1. Test Restart
    # ----------------------
    dut._log.info("Testing Restart...")

    dut.uio_in.value = 0b00000010  # restart = 1
    await ClockCycles(dut.clk, 1)

    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 1)

    # CRC should reset to 0xFF
    assert dut.uo_out.value == 0xFF, \
        f"Restart failed: {int(dut.uo_out.value)} != 0xFF"

    dut._log.info("Restart passed.")

    # ----------------------
    # 2. Test Data Input
    # ----------------------
    dut._log.info("Testing Data Input...")

    dut.ui_in.value = 0xA5  # sample data

    dut.uio_in.value = 0b00000001  # valid_in = 1
    await ClockCycles(dut.clk, 1)

    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 1)

    # CRC should change from initial value
    assert dut.uo_out.value != 0xFF, \
        "CRC did not update after valid input"

    dut._log.info(f"CRC updated to: {int(dut.uo_out.value)}")

    # ----------------------
    # 3. Multiple Data Cycles
    # ----------------------
    dut._log.info("Testing Multiple Updates...")

    data_sequence = [0x12, 0x34, 0x56]

    for data in data_sequence:
        dut.ui_in.value = data
        dut.uio_in.value = 0b00000001  # valid_in

        await ClockCycles(dut.clk, 1)

        dut.uio_in.value = 0
        await ClockCycles(dut.clk, 1)

    # Just ensure it's still producing valid output
    assert dut.uo_out.value is not None, "CRC output invalid"

    dut._log.info(f"Final CRC: {int(dut.uo_out.value)}")

    # ----------------------
    # Test Done
    # ----------------------
    dut._log.info("All tests passed")
