# Architecture Overview

This document describes the high-level architecture of the Liquid Symbiote Swarm Robotics Prototype.

## Components

1. **Physical Layer**  
   - Arduino Nano 33 BLE bots broadcast battery & formation status over BLE.

2. **Virtual Layer**  
   - Mesa-based Python simulation mirrors the physical layout for rapid prototyping.

3. **Global Control**  
   - `global_control/orchestrator.py` steps both physical and virtual swarms, then syncs commands (e.g., formation).

4. **Host Interface**  
   - `host_interface/cli.py` provides a CLI for checking vitals and triggering swarm behaviors.

## Communication Flow

- Physical bots communicate via BLE to the Global Control Node.  
- Simulation agents expose an API that the Global Control Node calls directly.  
- The Global Control Node merges both streams, issues commands, and collects status.

## Directory Structure

```
liquid-symbiote-prototype/
├── firmware/ # Arduino code
├── simulation/ # Mesa simulation scripts
├── global_control/ # Orchestrator & comms
├── host_interface/ # CLI & biometrics
└── docs/ # Documentation
```
