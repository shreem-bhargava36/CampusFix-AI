# CampusFix AI — Project Statement

## 1. Problem Statement

Students regularly face campus problems such as infrastructure issues, technical failures, academic concerns, administrative problems, and finance-related issues. Complaints may be difficult to classify, prioritize, and forward to the appropriate department manually.

CampusFix AI is designed to provide an intelligent complaint analysis system that automatically analyzes a student's complaint and supports faster routing and prioritization.

## 2. Project Scope

The project focuses on:

- Text-based student complaint analysis
- Automatic complaint category classification
- Automatic severity prediction
- Priority score and priority-level calculation
- Department routing
- Detection of similar previous complaints
- Campus complaint analytics
- Command-line based execution and testing

The current system uses machine learning and NLP-based text processing for complaint analysis.

## 3. Target Users

- Students
- Campus administration
- Department staff
- Complaint-management teams

## 4. High-Level Features

### 4.1 Complaint Classification
Classifies complaints into:

- Infrastructure
- Technical
- Academic
- Administrative
- Finance

### 4.2 Severity Prediction
Predicts complaint severity as:

- Low
- Medium
- High
- Urgent

### 4.3 Priority Engine
Calculates a priority score from 0–100 using the predicted severity and complaint category.

### 4.4 Department Routing
Routes complaints to an appropriate department based on the complaint category and routing rules.

### 4.5 Similar Complaint Detection
Uses TF-IDF and cosine similarity to identify potentially similar complaints from previous records.

### 4.6 Campus Analytics
Provides summaries of complaints by category, severity, department, and complaint aspects.

## 5. System Input

The primary input is:

- Student complaint text

Example:

> WiFi is completely unavailable in Lab 3.

## 6. System Output

The system produces:

- Predicted category
- Predicted severity
- Priority score
- Priority level
- Responsible department
- Similar previous complaints, when detected

## 7. Technology Stack

- Python
- Pandas
- Scikit-learn
- XGBoost
- TF-IDF
- Cosine Similarity
- Joblib
- Pytest
- Git/GitHub

## 8. Machine Learning

Two supervised machine-learning models are used:

1. Category classification model
2. Severity classification model

The project uses the University Students Complaints Dataset containing complaint descriptions and corresponding category, severity, and department-related information.

## 9. Project Objective

The main objective of CampusFix AI is to demonstrate how artificial intelligence and machine learning can assist in analyzing student complaints, determining their urgency, and supporting appropriate departmental routing.