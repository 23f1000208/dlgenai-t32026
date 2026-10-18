"""Training script for model training and validation."""

import argparse
from src.utils import set_seed, get_device


def train(args):
    """Main training routine."""
    device = get_device()
    print(f"Using device: {device}")
    set_seed(args.seed)
    # TODO: Load dataset
    # TODO: Initialize model
    # TODO: Run training loop
    print("Training pipeline initialized.")


def parse_args():
    parser = argparse.ArgumentParser(description="Model Training Script")
    parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=32, help="Batch size for training")
    parser.add_argument("--lr", type=float, default=1e-4, help="Learning rate")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    train(args)
