# CampusFix AI

## Intelligent Campus Complaint Detection, Prioritization and Routing System

CampusFix AI is an AI-based campus complaint analysis system that uses Natural Language Processing and Machine Learning to analyze student complaints.

The system takes a student complaint as text and automatically predicts its category and severity, calculates a priority score, routes the complaint to an appropriate department, and searches for similar previous complaints.

---

## 1. Problem Overview

Students may report different types of campus problems such as infrastructure issues, technical problems, academic concerns, administrative issues, and finance-related complaints.

Manually reviewing and routing a large number of complaints can be time-consuming.

CampusFix AI provides an intelligent pipeline to assist with:

- Complaint classification
- Severity prediction
- Priority calculation
- Department routing
- Similar complaint detection
- Campus complaint analytics

---

## 2. Objectives

The main objectives of CampusFix AI are:

1. Automatically classify student complaints into meaningful categories.
2. Predict the severity of a complaint.
3. Calculate a priority score and priority level.
4. Route complaints to an appropriate department.
5. Identify similar previous complaints.
6. Provide basic campus complaint analytics.
7. Demonstrate the practical application of AI and Machine Learning concepts.

---

## 3. Features

### 3.1 Complaint Category Classification

The system classifies complaints into:

- Infrastructure
- Technical
- Academic
- Administrative
- Finance

The category prediction model uses:

- TF-IDF
- XGBoost

---

### 3.2 Severity Prediction

The system predicts complaint severity as:

- Low
- Medium
- High
- Urgent

The severity prediction model also uses:

- TF-IDF
- XGBoost

---

### 3.3 Priority Engine

The priority engine combines the predicted severity and category to calculate a priority score between 0 and 100.

Priority levels are:

| Score | Priority Level |
|---:|---|
| 0–39 | Low |
| 40–64 | Medium |
| 65–84 | High |
| 85–100 | Critical |

---

### 3.4 Department Routing

The routing engine maps complaints to appropriate departments.

Examples:

| Category | Department |
|---|---|
| Infrastructure | Maintenance |
| Technical | IT |
| Academic | Department Head |
| Finance | Finance |
| Administrative | Registrar |

Additional routing rules are available for specific complaint aspects.

---

### 3.5 Similar Complaint Detection

CampusFix AI uses:

- TF-IDF Vectorization
- Cosine Similarity

to compare a new complaint with previous complaints and identify potentially similar issues.

---

### 3.6 Campus Analytics

The analytics module provides summaries of:

- Complaints by category
- Complaints by severity
- Complaints by department
- Top complaint aspects

---

## 4. System Workflow

```text
Student Complaint
       ↓
Input Validation
       ↓
Text Preprocessing
       ↓
 ┌───────────────┬────────────────┐
 ↓               ↓
Category       Severity
Prediction     Prediction
 ↓               ↓
 └───────┬───────┘
         ↓
  Priority Engine
         ↓
 ┌───────┴────────┐
 ↓                ↓
Department      Similar
Routing         Complaints
 ↓                ↓
 └───────┬────────┘
         ↓
    Final Analysis

5. Technology Stack
Technology	Purpose
Python	Core implementation
Pandas	Dataset handling
Scikit-learn	NLP and evaluation
XGBoost	Machine Learning classification
TF-IDF	Text feature extraction
Cosine Similarity	Similar complaint detection
Joblib	Saving/loading trained models
Pytest	Automated testing
Git	Version control
GitHub	Source code management
6. Dataset

The project uses the University Students Complaints Dataset.

The dataset contains student complaint information including:

Complaint description
Category
Severity
Responsible department information
Complaint aspects
Complaint group information

The dataset is divided into:

Training data: 273 records
Testing data: 59 records

The project uses the provided training and testing files separately.

Categories
Infrastructure
Technical
Academic
Administrative
Finance
Severity Classes
Low
Medium
High
Urgent
7. Machine Learning Models
Category Classification

The category classifier uses:

Complaint Text
      ↓
Text Preprocessing
      ↓
TF-IDF
      ↓
XGBoost Classifier
      ↓
Predicted Category
Severity Classification

The severity classifier uses:

Complaint Text
      ↓
Text Preprocessing
      ↓
TF-IDF
      ↓
XGBoost Classifier
      ↓
Predicted Severity
8. Model Evaluation

The models were evaluated using the separate test dataset.

Category Classification

Test Accuracy: 50.85%

Severity Classification

Test Accuracy: 44.07%

These results are reported from the current implementation and are not assumed to represent optimal model performance.

The dataset is relatively small and contains class imbalance, which can affect classification performance, particularly for less frequent classes.

9. Project Structure
CampusFix-AI/
│
├── app.py
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── models/
│   ├── category_xgboost.pkl
│   ├── category_tfidf.pkl
│   ├── category_labels.pkl
│   ├── severity_xgboost.pkl
│   ├── severity_tfidf.pkl
│   └── severity_labels.pkl
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── issue_classifier.py
│   ├── severity_engine.py
│   ├── priority_engine.py
│   ├── routing_engine.py
│   ├── similar_complaints.py
│   └── analytics.py
│
├── tests/
│   └── test_campusfix.py
│
└── diagrams/
    ├── system_architecture.png
    ├── workflow.png
    ├── use_case.png
    ├── class_diagram.png
    ├── component_diagram.png
    └── sequence_diagram.png
10. Installation
Step 1: Clone the repository
git clone https://github.com/shreem-bhargava36/CampusFix-AI.git
cd CampusFix-AI
Step 2: Create a virtual environment

Windows:

python -m venv .venv

Activate it:

.\.venv\Scripts\Activate.ps1
Step 3: Install dependencies
pip install -r requirements.txt
11. Running the Application

Run:

python app.py

The application provides three options:

1. Analyze New Complaint
2. Campus Analytics
3. Exit

Example complaint:

WiFi is completely unavailable in Lab 3

Example output:

Category       : Technical
Severity       : Urgent
Priority       : 98/100 (Critical)
Department     : IT
12. Training the Models

Category model:

python src/issue_classifier.py

Severity model:

python src/severity_engine.py

The trained models and TF-IDF vectorizers are saved in the models/ directory.

13. Testing

The project includes automated tests using Pytest.

Run:

python -m pytest -v

Current test result:

4 passed

The tests cover:

Text preprocessing
Priority calculation
Priority levels
Department routing
14. Input Validation and Error Handling

The application validates user input and prevents empty complaints from being processed.

Example:

Error: Complaint cannot be empty.

The main analysis pipeline also uses exception handling to prevent unexpected errors from terminating the application without an informative message.

15. Design Documentation

The diagrams/ directory contains the major design artifacts:

System Architecture Diagram
Workflow Diagram
UML Use Case Diagram
UML Class Diagram
UML Component Diagram
UML Sequence Diagram

These diagrams describe the system structure, workflow, components, interactions, and design.

16. Limitations

The current version has several limitations:

The dataset is relatively small.
Classification performance can be affected by class imbalance.
The system currently processes text-based complaints.
Similar complaint detection depends on textual similarity.
Department routing is based on predefined routing rules.
The current application is command-line based.
17. Future Scope

Possible future improvements include:

Larger and more diverse campus complaint datasets
Better NLP models and transformer-based classification
Multilingual complaint support
Image-based complaint analysis
Web-based student interface
Administrative dashboard
Complaint status tracking
Database integration
Duplicate and recurring issue monitoring
Improved model evaluation and hyperparameter optimization
18. Conclusion

CampusFix AI demonstrates how Artificial Intelligence, Natural Language Processing, and Machine Learning can be applied to a practical campus problem.

The system combines machine-learning prediction with rule-based priority and routing logic to transform an unstructured student complaint into structured information that can support campus complaint management.

19. Author

Developed as an academic project for:

Fundamentals of AI (CSA2001)

VIT Bhopal University