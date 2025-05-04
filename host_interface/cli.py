import argparse
from host_interface.biometrics import BiometricsMonitor
from global_control.orchestrator import main as run_orchestrator

def main():
    parser = argparse.ArgumentParser("SymBot CLI")
    parser.add_argument("action", choices=["status", "form", "simulate"])
    args = parser.parse_args()

    if args.action == "status":
        bm = BiometricsMonitor()
        print("Vitals:", bm.get_vitals())
    elif args.action == "form":
        print("Issuing FORM command to swarm...")
        run_orchestrator()
    elif args.action == "simulate":
        print("Running full simulation + formation...")
        run_orchestrator()

if __name__ == "__main__":
    main()
