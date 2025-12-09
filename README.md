# Ethernaut Scripts

## Description
This repository contains Python automation scripts for solving Ethernaut levels:

1. **[Privacy_key_extractor.py](Privacy_key_extractor.py)** – Fast automated extraction of the `_key` bytes for **Level 12 – Privacy**.  
2. **[Gatekeeper_one.py](Gatekeeper_one.py)** – Generates a custom `bytes8` key from your `tx.origin` address for **Level 13 – GatekeeperOne**.
3. **[pad_to_bytes32.py](pad_to_bytes32.py)** – Pads any hex string to a 32-byte (64-hex-char) zero-padded value, commonly used in **AlienCodex** level.

## Features
* **Privacy_key_extractor.py** – Input the constructor bytecode; automatically extracts the `_key` bytes.  
* **Gatekeeper_one.py** – Input your wallet address (`tx.origin`); generates a compliant `bytes8` key.  
* **pad_to32_bytes.py** – Input any hex string; returns a bytes32-padded version.

## Usage

### Privacy key extractor:
```bash
python Privacy_key_extractor.py
````

* Paste the constructor bytecode.
* Script outputs the `_key` bytes.

### Gatekeeper key generator:

```bash
python Gatekeeper_one.py
```

* Input your wallet address starting with `0x`.
* Script outputs your `bytes8` key.

### Pad hex to bytes32:

```bash
python pad_to32_bytes.py
```

* Input any hex string (`0x` optional).
* Script outputs the zero-padded 32-byte value.

## Notes

* All scripts automate tasks used in Ethernaut levels.
* Privacy_key_extractor.py is for **fast `_key` extraction**, Gatekeeper_one.py is for **custom key generation**, and pad_to32_bytes.py is for **bytes32 hex padding**.


```
```
