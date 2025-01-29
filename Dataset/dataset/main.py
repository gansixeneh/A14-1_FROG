import argparse

parser = argparse.ArgumentParser()

parser.add_argument('dataset_name', type=str, help='Name of the dataset')
parser.add_argument('dataset_path', type=str, help='Path to dataset or dataset endpoint')
parser.add_argument('timeout', type=int, help='Timeout in seconds')
parser.add_argument('amount', type=int, help='Amount of data to be generated')
parser.add_argument('category', type=str, choices=['simple_1', 'complex_1', 'simple_2', 'complex_2'], help='Category of data to be generated')
parser.add_argument('--count', action='store_true', help='Whether to generate count query')

args = parser.parse_args()

name = args.dataset_name
path = args.dataset_path
amount = args.amount
category = args.category
count = args.count
timeout = args.timeout

with open("dataset\io\excluded_props.txt", "r") as f:
    excluded_props = [line.strip() for line in f.readlines()]
    print("Successfully loaded list of excluded properties")

from generator import QADatasetGenerator

qads = QADatasetGenerator(path, excluded_props, timeout)
qads.write_to_file(name, amount, category, count)