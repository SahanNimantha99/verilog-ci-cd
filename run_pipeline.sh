#!/bin/bash

echo "🚀 Running Verilog Validation & Evaluation Pipeline..."

echo "🔍 Running Lint Checks..."
python3 validation/lint_check.py

echo "🛠 Running Icarus Verilog Simulation..."
python3 validation/run_icarus.py

echo "📊 Evaluating Model Performance..."
python3 evaluation/evaluate.py

echo "✅ Pipeline Execution Completed!"
