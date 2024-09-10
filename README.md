# Wigner Crystal Simulation

This repository contains a simple visual representation of the physics behind the Wigner crystal phenomenon, built using **Pygame** and **NumPy**. The project aims to offer an interactive, educational tool for coding enthusiasts and science learners interested in solid-state physics.

## Features

  *Interactive visualization: Watch particles simulate the unique behavior of a Wigner crystal.
  Customizable parameters: Adjust the values for different visual performance and system configurations.
  Educational purpose: Great for exploring concepts in condensed matter physics, especially in a classroom or self-study setting.
  Lightweight: Simple codebase, easy to modify, and extend for various applications.*

![Wigner_Pygame](https://github.com/user-attachments/assets/8928a74f-1b9d-44b5-b934-7724fb062b47)

## Getting Started
### Prerequisites

**Ensure you have the following installed:**

    Python 3.x
    Pygame
    NumPy

**You can install the dependencies via pip:**

    pip install pygame numpy

## Running the Simulation

**Clone the repository:**

    git clone https://github.com/CtrlAltWiz/Wigner-Crystal-Simulation-in-Pygame.git

**Navigate to the project directory:**

    cd Wigner-Crystal-Simulation-in-Pygame

**Run the simulation:**

    python Wigner_CrystalSim_PyGame.py

## Modifying the Parameters

You can modify the simulation’s behavior by changing values in the script such as:

**- Particle count:** Modify the number of particles *(using num_dots)* for performance tuning or to observe different behaviors.

**- Interaction strength:** *(using pygame.time.wait(1))* Adjust how strongly particles interact, affecting the crystal structure.

**- Grid size:** Resize the resolution grid to simulate different scales.

*Most of these parameters are located at the top of Wigner_CrystalSim_PyGame.py for easy access.*

## Understanding Wigner Crystals

![Wigner_cluster_600](https://github.com/user-attachments/assets/03b253b0-5275-4939-8d46-39aae8e9bd6a)
*Image from Wikipedia*

A Wigner crystal is a phase of matter that forms when electrons or other charged particles interact strongly enough at low densities, causing them to arrange into a lattice to minimize their potential energy. This simulation offers a simplified 2D model of this behavior, showcasing the fascinating properties of this crystal structure.

### Contributing

**Feel free to fork the repository and submit pull requests if you'd like to contribute or extend the functionality.**
    
