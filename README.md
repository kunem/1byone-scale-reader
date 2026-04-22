# BLE Smart Scale Reverse Engineering

A Python tool for connecting to and analyzing BLE smart bathroom scales (tested on 1byone smart body scale models).

This project focuses on reverse engineering the BLE communication protocol used by smart scales to extract real-time weight data directly from the device.

---

## 📌 What This Project Does

- Connects directly to BLE smart scales using Python (`bleak`)
- Discovers and logs all BLE services and characteristics
- Captures live weight broadcast packets in real time
- Decodes proprietary 16-byte BLE frames
- Converts raw sensor values into human-readable weight (lbs / kg)
- Provides debugging tools for reverse engineering unknown BLE devices

---

## ⚠️ Important Limitations

- The scale tested in this project broadcasts **weight only over BLE**
- Body composition metrics (body fat %, muscle, water, bone mass, BMR) are **NOT transmitted via BLE**
- Those values are likely computed internally by the scale or handled by the official mobile app
- This project focuses strictly on BLE-level data extraction

---

## 🧠 Key Findings

During reverse engineering, the following was discovered:

- The scale uses a fixed 16-byte BLE packet structure: cf 01 ad aa 04 XX YY ZZ ...
- - Only specific bytes contain weight-related data
- Remaining bytes represent device state, flags, or checksums
- No impedance or body composition data is exposed via BLE

---

## 📦 Requirements

Install dependencies:

```bash
pip install bleak


🚀 Usage

Run the main script:

python scale_reader.py


Example output:

============================
RAW : 11622
KG  : 106.8
LBS : 235.4
============================
