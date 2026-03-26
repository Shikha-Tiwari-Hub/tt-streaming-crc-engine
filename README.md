![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# Tiny Tapeout Verilog Project
- [Read the documentation for project](docs/info.md)

## What is Tiny Tapeout?
Tiny Tapeout is an educational project that aims to make it easier and cheaper than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## Cyclic Redundancy Check (CRC)

This design is based on the concept of **Cyclic Redundancy Check (CRC)**, a widely used error-detection technique in digital communication systems.

CRC works by treating binary data as a polynomial and performing **modulo-2 division** using a generator polynomial (key). The remainder obtained from this division is appended to the original data for transmission.

At the receiver side, the same division is performed again:
- If the remainder is **zero**, the data is considered error-free  
- If the remainder is **non-zero**, an error is detected  

Unlike normal division, modulo-2 division:
- Uses **XOR instead of subtraction**
- Does not involve carry or borrow  
- Operates purely on binary values  

This makes CRC highly efficient for hardware implementation. :contentReference[oaicite:1]{index=1}

### Architecture Diagram 
<img width="500" height="500" alt="block diagram crc" src="https://github.com/user-attachments/assets/df5749aa-637e-413e-93bb-271a31bb6e6f" />

---
## ⚙️ Design Features
- 8-bit streaming data input
- Real-time CRC computation
- Low-area hardware implementation (ASIC-friendly)
- Simple control interface using valid and restart signals
- Fully synchronous design (clock-driven)
- Continuous output availability

---

## Design Approach
Instead of performing full binary division directly, this implementation uses a **shift-register-based approach (LFSR-like behavior)**.

This approach:
- Mimics modulo-2 division
- Uses XOR operations for feedback
- Is optimized for hardware efficiency
- Reduces complexity compared to long division

---

## Applications
This CRC engine can be used in:

- Data communication systems (UART, SPI, etc.)
- Error detection in digital transmission
- Embedded systems data integrity checks
- Storage systems (basic checksum validation)

---
## 🚀 Future Improvements

- Support for configurable CRC polynomials  
- Extend to CRC-16 / CRC-32  
- Add UART interface for real-world communication  
- Pipeline optimization for higher clock speeds  

---
## 📚 References

- GeeksforGeeks - Modulo-2 Binary Division and CRC  
- Digital Communication Systems (CRC error detection concept)
