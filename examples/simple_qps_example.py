from qps.core import QuantumPositioningSystem
from qps.entanglement import QuantumEntanglement
from qps.quantum_frequency_mapping import QuantumFrequencyMapping

def main():
    # Initialize Quantum Positioning System
    qps = QuantumPositioningSystem()

    # Generate Entanglement
    entanglement = QuantumEntanglement()
    entangled_state = entanglement.entangle_particles()
    
    # Calculate Position using Quantum Frequency Mapping
    qfm = QuantumFrequencyMapping(frequency=5)
    position = qfm.map_to_position(entangled_state)
    
    # Print the calculated position
    print(f"Calculated Quantum Position: {position}")

if __name__ == '__main__':
    main()
