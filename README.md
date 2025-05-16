# DataAtlas_PY

**Data Atlas** is a Python-based data exploration tool that lets you load structured datasets (like CSV or JSON), perform flexible searches across fields, and experiment with different data structures and search algorithms.

The goal of this project is to reinforce foundational data structure concepts (such as lists, dictionaries, and trees), implement search algorithms in a real-world context, and build a tool that is both practical and extensible.

---

## ✨ Features

- Load datasets from CSV or JSON
- Search records by field and value (e.g., filter all items with `type = Fire`)
- Compare search strategies like linear search, hash-based lookup, and binary search
- Command-line interface for easy interaction
- Extensible structure to support more advanced algorithms (e.g., trie, sorting, indexing)

---

## 🔧 Getting Started

### Clone the Repository

```bash
git clone https://github.com/hewitt205/DataAtlas_PY.git
cd data-atlas

### Set Up a Virtaul Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


### 🧱 Install Dependencies

Install required Python packages (once `requirements.txt` is created):

```bash
pip install -r requirements.txt


### 🚀 Running the App

Start the app using:

```bash
python main.py


### 📂 Project Structure

```plaintext
data-atlas/
├── datasets/        # Sample datasets (CSV, JSON)
├── src/             # Core logic and utilities
│   ├── search.py    # Search algorithms
│   ├── loader.py    # File loading/parsing
│   └── cli.py       # User interaction / input loop
├── main.py          # Entry point for the app
├── README.md
└── requirements.txt


### 🛠 Future Features

- Advanced search: fuzzy match, prefix/autocomplete
- Performance comparisons between search strategies
- In-memory indexing for faster queries
- Optional GUI or web-based interface


### 📚 Learning Goals

This project is a hands-on exercise designed to help you:

- Strengthen understanding of core data structures
- Apply algorithmic thinking to real-world data
- Improve pattern recognition and analytical skills
- Practice clean, modular Python development


### 📜 License

This project is open source and available under the [MIT License](LICENSE).

