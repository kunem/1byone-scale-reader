import asyncio
from bleak import BleakClient, BleakScanner

WRITE_UUID = "0000fff1-0000-1000-8000-00805f9b34fb"
NOTIFY_UUID = "0000fff4-0000-1000-8000-00805f9b34fb"

INIT_PACKET = bytes.fromhex("fe010100aa2d0285")

last_weight = None


# ----------------------------
# decode weight (from your packets)
# ----------------------------
def decode_weight(data):
    try:
        if len(data) != 16:
            return None

        raw = (data[5] << 8) | data[7]

        lbs = raw * 0.000888 + 224.68
        kg = lbs / 2.20462

        return round(kg, 1), round(lbs, 1)

    except:
        return None


# ----------------------------
# BLE handler
# ----------------------------
def notification_handler(sender, data):
    global last_weight

    decoded = decode_weight(data)

    if decoded:
        kg, lbs = decoded

        # only print if changed significantly
        if last_weight is None or abs(lbs - last_weight) > 0.2:
            print(f"\r⚖️  Weight: {lbs:.1f} lb | {kg:.1f} kg", end="")
            last_weight = lbs


# ----------------------------
# device scanner
# ----------------------------
async def select_device():
    print("\n🔍 Scanning for BLE scales...\n")

    devices = await BleakScanner.discover(timeout=6)

    for i, d in enumerate(devices):
        name = d.name if d.name else "Unknown"
        print(f"[{i}] {name} | {d.address}")

    idx = int(input("\nSelect device index: "))
    return devices[idx].address


# ----------------------------
# main
# ----------------------------
async def main():
    address = await select_device()

    print(f"\n🔗 Connecting to {address}...\n")

    async with BleakClient(address) as client:

        if not client.is_connected:
            print("❌ Connection failed")
            return

        print("✅ Connected")
        print("📡 Waiting for weight data...\n")

        await client.start_notify(NOTIFY_UUID, notification_handler)

        await asyncio.sleep(0.5)
        await client.write_gatt_char(WRITE_UUID, INIT_PACKET)

        print("🟢 Step on the scale...\n")

        while True:
            await asyncio.sleep(1)


asyncio.run(main())