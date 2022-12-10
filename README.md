
# Performance Analysis of DRL Algorithms in V2V Resource Allocation

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

> Official implementation of the IEEE 2022 paper  
> **"Performance Analysis of DRL Algorithms in V2V Resource Allocation"**

---

## Overview

This project explores how intelligent agents (vehicles) can learn to dynamically allocate wireless communication resources in Vehicle-to-Vehicle (V2V) networks using Deep Reinforcement Learning (DRL). Published at IEEE, it compares the performance of multiple DRL algorithms in optimizing packet delivery, minimizing interference, and allocating spectrum efficiently in mobile, high-density vehicular environments.

Through simulation, policy benchmarking, and experiment-driven analysis, this research contributes to the evolving field of intelligent transportation systems and wireless scheduling.

---

## Project Objectives

- Evaluate DRL techniques for dynamic V2V resource scheduling.
- Model realistic wireless environments for inter-vehicle communication.
- Compare policy-based and value-based learning algorithms (e.g., PPO, DRQN).
- Measure reliability, SINR, channel congestion, and latency across scenarios.
- Provide a simulation baseline for future extensions to real-world systems.

---

## Algorithms Implemented

| Algorithm         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **DRQN**          | Uses LSTM to model temporal dependencies in Q-learning                     |
| **PPO**           | Policy gradient method with clipped surrogate objective                    |
| **Softmax**       | Selects actions probabilistically based on Q-values                        |
| **Epsilon-Greedy**| Trades off exploration and exploitation with decaying epsilon              |
| **Greedy**        | Always selects the highest Q-value action (no exploration)                 |

---

## Features

### Multi-Agent Reinforcement Learning
- Each vehicle is a learning agent choosing resource blocks and power levels.
- Agents are trained in a centralized manner and deployed in a decentralized setting.

### Centralized Training, Decentralized Execution
- Centralized training ensures shared policy convergence.
- During testing, agents act based only on local observations.

### Configurable Experiments
- YAML-based configuration files allow fast experimentation with number of UEs, RBs, and learning parameters.

### Evaluation Metrics
- Signal-to-Interference-plus-Noise Ratio (SINR)
- Packet Reception Ratio (PRR)
- Channel Busy Ratio (CBR)
- Transmission delay

---

## Project Structure

```
.
├── algorithms/              # DRL model definitions and policies
├── envs/                    # Simulation environment and channel logic
├── utils/                   # Experience replay, helper functions
├── config/                  # Experiment configuration files
│   ├── config_dis_03.yaml
│   ├── config_dis_05.yaml
│   ├── config_dis_07.yaml
│   ├── config_dis_95.yaml
│   └── config_dis_07_b40.yaml
├── save_results/            # Output folder for results (.npy, logs)
├── main_test.py             # Main entry script
├── requirements.txt         # Python dependencies
├── LICENSE.md
└── README.md
```

---

## Install Requirements with:

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration Files

All DRQN simulation setups are organized in the `config/` directory. Each YAML file represents a unique experimental variation, changing parameters like discount factor (`gamma`) and input state resolution (`num_bins`).

| File Name | Description |
|-----------|-------------|
| `config_dis_03.yaml` | Baseline configuration with default `gamma` and state discretization. |
| `config_dis_05.yaml` | DRQN setup with discount factor `γ = 0.5`, giving less importance to future rewards. |
| `config_dis_07.yaml` | DRQN with `γ = 0.7`, balancing immediate and future returns. |
| `config_dis_95.yaml` | DRQN with `γ = 0.95`, strongly favoring long-term gains. |
| `config_dis_07_b40.yaml` | DRQN with `γ = 0.7` and increased `num_bins = 40`, allowing finer positional representation in the environment. |

**How to Run a Specific Config:**

```bash
python main_test.py --config config/config_dis_07.yaml
```

> Tip: Keep result files (.npy, logs, plots) for each config inside a dedicated folder inside `/save_results/`.



## Future Scope

- Integrate real-world vehicle traces using SUMO or Veins.
- Explore transformer-based policies for spatio-temporal learning.
- Extend to V2I scenarios and hybrid infrastructure environments.
- Build a dashboard to visualize learning and simulation stats.

---

## Citation

If you use this work in your research or projects, please cite the following IEEE publication:

Performance Analysis of DRL Algorithms in V2V Resource Allocation
Shruthi Chandrakumar, Harini C, Kezia M, Anusuya K. V
[IEEE Xplore Link](https://ieeexplore.ieee.org/document/10100573)


## License

This project is licensed under the [MIT License](./LICENSE.md).
