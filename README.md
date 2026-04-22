# BLE Smart Scale Reader

A Python tool that connects to BLE bathroom scales and streams real-time weight data directly from the device.

Tested on 1byone smart body scale (BLE model).

---

## ⚙️ Features

- Auto BLE device scanning
- Interactive device selection
- Live weight streaming
- Clean terminal display
- Stable packet decoding
- Cross-device support (any BLE scale using fff0 service)

---

## ⚠️ Notes

- Only weight data is transmitted over BLE
- Body composition metrics (fat %, muscle, water, etc.) are NOT exposed
- Those are likely computed internally by the scale or mobile app

---

## 🚀 Installation

```bash
pip install -r requirements.txt


## 🔧 How It Works
Scans for BLE devices
Connects to selected scale
Subscribes to notification characteristic:
0000fff4-0000-1000-8000-00805f9b34fb
Sends initialization packet
Decodes proprietary 16-byte BLE frames into weight


