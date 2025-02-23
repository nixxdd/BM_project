"""Parameters for balanced network"""

# Simulation Parameters
STEPS = 20
STEPS_DURATION = 100.0

# Excitatory Neuron Parameters
E_NEURON_E_L = -65.0
E_NEURON_C_M = 250.0
E_NEURON_T_REF = 2.0
E_NEURON_V_TH = -50.0
E_NEURON_V_RESET = -65.0
E_NEURON_TAU_SYN_EX = 4.0
E_NEURON_TAU_SYN_IN = 2.0
ADAPTATION_a = 0.005
ADAPTATION_b = 0.4
ADAPTATION_tau_w = 100.0

# Inhibitory Neuron Parameters
I_NEURON_E_L = -65.0
I_NEURON_C_M = 250.0
I_NEURON_TAU_M = 20.0
I_NEURON_T_REF = 2.0
I_NEURON_V_TH = -57.0
I_NEURON_V_RESET = -65.0
I_NEURON_TAU_SYN_EX = 4.0
I_NEURON_TAU_SYN_IN = 2.0
INH_BACKGROUND = 100.0

# DC Input Parameters
DC_INPUT_AMPLITUDE = 300.0

DC_INPUT_START_1 = 200.0
DC_INPUT_STOP_1 = 500.0
DC_INPUT_START_2 = 1200.0
DC_INPUT_STOP_2 = 1500.0

DC_INPUT_WEIGHT = 1.5
DC_INPUT_DELAY = 1.0


# Thalamic Input Parameters
THALAMIC_INPUT_FIRING_RATE = 200.0
THALAMIC_INPUT_WEIGHT = 2.0
THALAMIC_INPUT_DELAY = 1.0

# Population Parameters
POP_SIZE_E = 200
POP_SIZE_I = 100

# Synapses Parameters
DELAY_CONNECTION = 1.0
G = 1.3
EXC_WEIGHT = 1.0
INH_WEIGHT = -1.0

# Distribution of synaptic connections parameters
GAUSSIAN_STD = 0.7
DISTRIBUTION_THRESHOLD = 0.6
MASK_RADIUS = 0.4

# Distribution of short synaptic connections parameters
GAUSSIAN_STD_SHORT = 0.8
DISTRIBUTION_THRESHOLD_SHORT = 0.2
MASK_RADIUS_SHORT = 0.5
