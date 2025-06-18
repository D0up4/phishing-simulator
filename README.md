# 🎯 Phishing Simulation Toolkit (Red Team Lab)

**Author:**  D0up4   
**Project Type:** Red Team Simulation / Educational
**Last Updated:**  06/2025

## 📘 Description

This is a **lab-only phishing simulation toolkit** designed to demonstrate how credential harvesting attacks may occur using social engineering and fake login pages. It includes a realistic-looking Microsoft-style login page built from scratch (no copyrighted code), a local Flask server to receive test credentials, and credential logging.

This project is intended for **ethical red team development**, **security education**, and **security awareness training** — strictly in **controlled, private lab environments**.

---

## ⚙️ Features

- ✅ Realistic Microsoft-style login UI (100% custom HTML/CSS)
- ✅ Flask-based backend server (`Python`)
- ✅ Credential capture and timestamped logging
- ✅ Redirects to Microsoft’s real login page post-submit
- ✅ Safe for labs: no external delivery or malware involved

---

## 🖼️ Screenshots

| Login Page              | Credential Log Output              |
|-------------------------|------------------------------------|
| ![login page](https://github.com/user-attachments/assets/197b42cd-0d82-48d5-9b39-c15868b83974) | ![logs](https://github.com/user-attachments/assets/988e4ee6-e871-47be-a17f-91c3cf045707)         |

---

## 🚀 Usage

### 🧱 1. Requirements

- Python 3.x
- Flask

### 🧪 2. Setup

```bash
git clone https://github.com/D0up4/phishing-simulator.git
cd phishing-simulator
pip install -r requirements.txt
python server.py
