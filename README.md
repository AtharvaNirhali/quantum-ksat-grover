# Quantum K-SAT Solver using Grover's Algorithm

This project implements Grover's Quantum Search Algorithm using Qiskit to solve K-SAT problems. The solution leverages quantum superposition and amplitude amplification to achieve a quadratic speedup over classical brute-force search.

## System Architecture

![Architecture](docs/diagrams/architecture.png)

## Workflow:

CNF Input
    ↓
Oracle Construction
    ↓
Diffusion Operator
    ↓
Grover Iterations
    ↓
Quantum Measurement
    ↓
Solution Extraction

## Oracle Circuit

![Oracle](results/circuits/oracle_circuit.png)

## Grover Circuit

![Grover](results/circuits/grover_circuit.png)

## Experimental Results

![Histogram](results/histograms/result_histogram.png)

## Performance Comparison

| Problem Instance | Classical Time (μs) | Quantum Time (μs) | Speedup |
|------------------|---------------------|-------------------|---------|
| 3-SAT, 3 Clauses | 19                  | 3                 | 6.33×   |
| 3-SAT, 4 Clauses | 29                  | 4                 | 7.25×   |
| 3-SAT, 5 Clauses | 19                  | 7                 | 2.71×   |
| 4-SAT, 5 Clauses | 57                  | 4                 | 14.25×  |
| 5-SAT, 5 Clauses | 61                  | 7.5               | 8.13×   |

## Installation

git clone https://github.com/yourname/quantum-ksat-grover.git

cd quantum-ksat-grover

pip install -r requirements.txt

## Run

jupyter notebook notebooks/Grover_KSAT_Demo.ipynb

## Publications

Nirhali A., Patil A., Malwade R., Panchal S.

"Implementation of Efficient Quantum Computing Algorithm for Searching"

ICMET 2025
