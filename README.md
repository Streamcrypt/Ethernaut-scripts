# Ethernaut Scripts

## Description
This repository contains Python automation scripts for solving Ethernaut levels:

1. **[Privacy_key_extractor.py](Privacy_key_extractor.py)** – Fast automated extraction of the `_key` bytes for **Level 12 – Privacy**.  
2. **[Gatekeeper_one.py](Gatekeeper_one.py)** – Generates a custom `bytes8` key from your `tx.origin` address for **Level 13 – GatekeeperOne**.  

## Features
* **Privacy_key_extractor.py** – Input the constructor bytecode; automatically extracts the `_key` bytes.  
* **Gatekeeper_one.py** – Input your wallet address (`tx.origin`); generates a compliant `bytes8` key.  

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

## Notes

* Both scripts are automations for solving Ethernaut levels.
* Privacy_key_extractor.py is for **fast automated extraction**, Gatekeeper_one.py is for **custom key generation**.

```
```
