"""Parameters for balanced network"""

# Excitatory Neuron Parameters
E_NEURON_E_L = -70.0
E_NEURON_C_M = 250.0
E_NEURON_TAU_M = 10.0
E_NEURON_T_REF = 2.0
E_NEURON_V_TH = -55.0
E_NEURON_V_RESET = -70.0
E_NEURON_TAU_SYN_EX = 4.0
E_NEURON_TAU_SYN_IN = 2.0

# Inhibitory Neuron Parameters
I_NEURON_E_L = -70.0
I_NEURON_C_M = 250.0
I_NEURON_TAU_M = 10.0
I_NEURON_T_REF = 2.0
I_NEURON_V_TH = -55.0
I_NEURON_V_RESET = -70.0
I_NEURON_TAU_SYN_EX = 4.0
I_NEURON_TAU_SYN_IN = 2.0

# Thalamic Input Parameters
THALAMIC_INPUT_FIRING_RATE = 650.0
THALAMIC_INPUT_WEIGHT = 50.0
THALAMIC_INPUT_DELAY = 1.0

# Population Parameters
POP_SIZE_E = 200
POP_SIZE_I = 100

# Synapses Parameters
DELAY_CONNECTION = 1.0
G = 1.3
EXC_WEIGHT = 100.0
INH_WEIGHT = -50.0

# Distribution of synaptic connections parameters
GAUSSIAN_STD = 0.7
GAUSSIAN_STD_LONG = 0.1
DISTRIBUTION_THRESHOLD = 0.6
MASK_RADIUS = 0.4

# Distribution of short synaptic connections parameters
GAUSSIAN_STD_SHORT = 0.8
DISTRIBUTION_THRESHOLD_SHORT = 0.2
MASK_RADIUS_SHORT = 0.5
