# Introduction to DL and GenAI Project [BSDA2001P]

This repository contains the coursework project for **Introduction to DL and GenAI Project [BSDA2001P]**.

---

## Repository Structure

The repository follows the course guidelines:

```text
dlgenai-t32026/
│
├── notebooks/
│   ├── milestone-1.ipynb
│   ├── milestone-2.ipynb
│   └── final_notebook.ipynb
│
├── src/
│   ├── __init__.py
│   ├── train.py
│   ├── inference.py
│   └── utils.py
│
├── reports/
│   ├── milestone-1-report.pdf
│   ├── milestone-2-report.pdf
│   └── final-report.pdf
│
├── models/
│   └── .gitkeep
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Branching Strategy (Mandatory)

### 1. Main Branch (`main`)
The `main` branch represents the stable version of the project and contains:
- Latest working notebooks
- Final training and inference scripts
- Updated milestone and final reports
- Project documentation and README

### 2. Milestone Branches (`milestone-1`, `milestone-2`, `milestone-3`)
- All milestone work must be developed inside its corresponding milestone branch.
- **Do not commit milestone work directly to `main`**.
- **Do not delete milestone branches** after merging into `main`. Milestone branches are retained for evaluation and audit.

### Recommended Workflow

1. **Create and switch to a milestone branch**:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b milestone-1
   ```

2. **Develop and commit changes**:
   ```bash
   git add .
   git commit -m "Milestone 1: Completed data preprocessing and EDA"
   ```

3. **Push the milestone branch to remote**:
   ```bash
   git push -u origin milestone-1
   ```

4. **Merge into `main` after milestone completion**:
   ```bash
   git checkout main
   git merge milestone-1
   git push origin main
   ```

---

## Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/23f1000208/dlgenai-t32026.git
   cd dlgenai-t32026
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Milestones Summary

| Milestone | Description | Branch | Status |
|---|---|---|---|
| **Milestone 1** | Problem Formulation, Dataset Preparation & EDA | `milestone-1` | In Progress |
| **Milestone 2** | Baseline Modeling & Feature Engineering | `milestone-2` | Pending |
| **Milestone 3** | Advanced Modeling, Fine-tuning & Evaluation | `milestone-3` | Pending |
| **Final** | Final Training/Inference Scripts & Project Report | `main` | Pending |
