# Synaptic Pruning and Firing Rate Analysis

## Overview
This project investigates the effects of synaptic pruning on neural network dynamics using **NEST Simulator**. We analyze how different pruning strategies impact network activity, particularly focusing on excitatory-inhibitory interactions and firing rates under varying thalamic input frequencies.

## Pruning Strategies
Two pruning methods are implemented:
- **Distance-based pruning**: Removes synapses exceeding a set Euclidean distance threshold.
- **Weight-based pruning**: Removes synapses with an effective weight (computed as \( u \times x \)) below a given threshold.

A **baseline model** with no pruning is used for comparison.

## Simulation Setup
1. **Network Initialization**
   - Creates excitatory (layer_e) and inhibitory (layer_i) neuron populations.
   - Establishes synaptic connections based on predefined connectivity rules.
   
2. **Pruning Application**
   - Pruning strategies are applied independently to ensure results are not influenced by prior pruning steps.
   
3. **Thalamic Input Simulation**
   - The network is stimulated with varying thalamic input rates to assess response dynamics.
   
4. **Recording and Analysis**
   - Measures synaptic variables (u, x) and firing rates across different conditions.
   - Results are visualized to compare pruning effects.

## Results
- **Pruning leads to increased excitability**: Pruned networks show higher firing rates compared to the baseline.
- **Weight pruning has a stronger effect**: It causes greater deviations from the unpruned model compared to distance pruning.
- **Activity stabilizes at higher input frequencies**: The difference between pruned and unpruned networks diminishes as input rates increase.

## Plots and Analysis
### 1. Firing Rate Differences
Plots illustrate how pruning alters firing rates relative to the baseline, revealing stronger deviations at moderate input frequencies.

### 2. Synaptic Variable Evolution
Tracking **u** (utilization) and **x** (available resources) over time highlights distinct recovery and depletion patterns under different pruning conditions.

### 3. Input-Response Relationship
Comparisons of firing rates as a function of thalamic input provide insight into network adaptation and stability.

## Future Improvements
- Implement additional pruning strategies (e.g., activity-based pruning).
- Explore network plasticity and long-term stability.
- Optimize computational efficiency for large-scale simulations.
