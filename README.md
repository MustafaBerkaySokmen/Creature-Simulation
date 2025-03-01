# Creature Simulation

## Overview
This project simulates an **ecosystem** where creatures move, eat, survive, and reproduce on a **grid-based environment**. The simulation is animated using **Matplotlib** and follows simple survival rules.

## Features
- **Random Creature Movement:** Creatures move randomly within the grid.
- **Food Spawning:** Food appears randomly on the grid.
- **Survival Mechanics:** Creatures die if they don’t eat within 10 time steps.
- **Reproduction System:** Creatures that eat twice within 10 time steps reproduce.
- **Matplotlib Animation:** The simulation updates in real-time, displaying creatures and food dynamically.

## Installation
To set up and run this project, follow these steps:

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/creature-simulation.git
cd creature-simulation
```

### **2. Install Dependencies**
```bash
pip install numpy matplotlib
```

### **3. Run the Simulation**
```bash
python creature_simulation.py
```

## Usage
- **Run the script** and watch as creatures move, search for food, and reproduce.
- Modify parameters in `creature_simulation.py` to experiment with different survival conditions.
- Adjust the **grid size, food spawn rate, and reproduction rules** to observe different outcomes.

## Example Output
```
Step 10: 5 creatures alive, 3 pieces of food available
Step 20: 8 creatures alive, 4 pieces of food available
Step 50: 15 creatures alive, 6 pieces of food available
```

## File Renaming Guide
| **Old Name**          | **New Name (Suggested)**      | **Description** |
|----------------------|----------------------------|----------------|
| `ChatBir_ADAM.py`    | **`creature_simulation.py`** | Main simulation script |

## License
This project is licensed under the **MIT License**.

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact
For any questions or support, please open an issue on GitHub.

