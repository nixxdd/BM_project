"""Parameters for balanced network"""

# Excitatory Neuron Parameters
E_NEURON_E_L = -60.0
E_NEURON_C_M = 250.0
E_NEURON_TAU_M = 10.0
E_NEURON_T_REF = 2.0
E_NEURON_V_TH = -55.0
E_NEURON_V_RESET = -60.0
E_NEURON_TAU_SYN_EX = 5.0
E_NEURON_TAU_SYN_IN = 10.0

# Inhibitory Neuron Parameters
I_NEURON_E_L = -60.0
I_NEURON_C_M = 250.0
I_NEURON_TAU_M = 10.0
I_NEURON_T_REF = 2.0
I_NEURON_V_TH = -55.0
I_NEURON_V_RESET = -60.0
I_NEURON_TAU_SYN_EX = 5.0
I_NEURON_TAU_SYN_IN = 10.0

# Thalamic Input Parameters
THALAMIC_INPUT_FIRING_RATE = 350.0
THALAMIC_INPUT_WEIGHT = 15
THALAMIC_INPUT_DELAY = 1.0

# Population Parameters
POP_SIZE_E = 200
POP_SIZE_I = 70

# Synapses Parameters
DELAY_CONNECTION = 1.0
G = 1.3
EXC_WEIGHT = 4.59
INH_WEIGHT = -G * EXC_WEIGHT

# Distribution of synaptic connections parameters
GAUSSIAN_STD = 0.8
DISTRIBUTION_THRESHOLD = 0.3
MASK_RADIUS = 0.4