# Contextualised Machine Learning for Stock Return Prediction

This repository contains the code and experimental materials for my final-year engineering thesis at the University of Oxford. The project explores **contextualised machine learning methods** for predicting **stock returns**, focusing on how both macroeconomic and firm-level signals can modulate model parameters dynamically.

## 📘 Project Overview

Conventional financial forecasting models often fail to generalise across varying economic conditions and firm contexts. This project introduces a framework for *contextualised learning* where predictive models, such as ARIMA and XGBoost, are extended to incorporate contextual information—like macroeconomic uncertainty indices and firm fundamentals—as modulators of their parameters. The goal is to improve both predictive performance and economic relevance of model outputs.

## 🚀 Key Contributions

- **Contextualised Regression Framework:** A general-purpose architecture that allows model parameters to vary with context.
- **ContextARIMA:** A novel time-series forecasting model that integrates firm fundamentals into ARIMA coefficients.
- **Experimental Benchmarks:** Evaluations on both synthetic panel data and real-world financial data.
- **Portfolio Backtesting:** Performance analysis using directional accuracy, Sharpe ratio, and portfolio returns.

## 📁 Project Structure

```bash
.
data/ # Raw and processed financial data
├── lightning_logs/ # PyTorch Lightning logs and checkpoints
├── models/ # trained contextualised models
├── notebooks/ # Experiments and training scripts
├── results/ # Final metrics, plots
├── utils/ # Helper functions (data loading, metrics, etc.)
├── README.md               # This file
