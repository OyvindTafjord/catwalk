import os
import datasets
import numpy as np

from iz.crossfit.fewshot_gym_dataset import FewshotGymDataset, FewshotGymTextToTextDataset

class Kilt_NQ(FewshotGymTextToTextDataset):

    def __init__(self):
        self.hf_identifier = "kilt_nq"
        self.task_type = "text to text"
        self.license = "unknown"

    def map_hf_dataset_to_list(self, hf_dataset, split_name):
        lines = []
        for datapoint in hf_dataset[split_name]:
            lines.append((datapoint["input"].replace("\n", " "), "\t".join([item["answer"] for item in datapoint["output"]])))
        return lines

    def load_dataset(self):
        return datasets.load_dataset('kilt_tasks','nq')

def main():
    dataset = Kilt_NQ()

    for seed in [100, 13, 21, 42, 87]:
        train, dev, test = dataset.generate_k_shot_data(k=32, seed=seed, path="../data/")

if __name__ == "__main__":
    main()