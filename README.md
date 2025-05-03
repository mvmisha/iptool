# iptool

**iptool** is a Python command-line tool that inspects IP addresses using the [ipinfo.io](https://ipinfo.io) API.  
It shows network and location data like hostname, city, region, ASN, and organization.

---

## 📦 Features

- 🌐 Uses `ipinfo.io` to retrieve IP information
- 🧠 Reverse DNS, city, country, ASN, org, and more
- 💡 Clean terminal output with `rich`
- 🧼 Simple and extendable code structure

---
## 🛠 Usage

From the root of the project:

```bash
python run.py 8.8.8.8
```

You’ll get output like this:

```
Info for 8.8.8.8

┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Field    ┃ Value                ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ Ip       │ 8.8.8.8              │
│ Hostname │ dns.google           │
│ City     │ Mountain View        │
│ Region   │ California           │
│ Country  │ US                   │
│ Org      │ AS15169 Google LLC   │
│ Loc      │ 37.3860,-122.0840    │
└──────────┴──────────────────────┘
```

---

## 🧰 Requirements

- Python 3.7+
- Internet connection (uses ipinfo.io API)

---

## 🧠 Project Structure

```
iptool/
├── iptool/               ← Source code package
│   ├── cli.py
│   ├── iplookup.py
│   └── __init__.py
├── run.py                ← Launcher script
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

---

## 📝 License

MIT — use it, modify it, break it, learn from it 😄

---

## 👤 Author

Misha — [@mvmisha](https://github.com/mvmisha)
