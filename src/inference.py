"""Inference script for running model predictions."""

import argparse
from src.utils import get_device


def run_inference(model_path: str, input_text: str):
    """Run model inference on input."""
    device = get_device()
    print(f"Loading model from {model_path} onto {device}...")
    # TODO: Load model checkpoints from models/ directory
    # TODO: Perform tokenization / preprocessing and forward pass
    print(f"Input: {input_text}")
    print("Inference completed.")


def parse_args():
    parser = argparse.ArgumentParser(description="Model Inference Script")
    parser.add_argument("--model-path", type=str, default="models/", help="Path to model weights")
    parser.add_argument("--input", type=str, default="Hello, World!", help="Input data or text")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_inference(args.model_path, args.input)
