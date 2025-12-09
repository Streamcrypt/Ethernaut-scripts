prompt = input("Enter your hex string to pad to bytes32 (0x optional):\n --> ").replace("0x", "")
print("0x" + format(prompt, "0>64"))
