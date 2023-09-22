import argparse
import json

def generate_main_json(model_name):
    # Create a dictionary with "modelnames" as the key and the model name + ".py" as the value
    model_mapping = {"modelnames": model_name + ".py"}

    with open("main.json", "w") as json_file:
        json.dump(model_mapping, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate main.json for model deployment")
    parser.add_argument("model_name", type=str, help="Name of the model")

    args = parser.parse_args()

    generate_main_json(args.model_name)
    print(f"main.json generated for model: {args.model_name}")
