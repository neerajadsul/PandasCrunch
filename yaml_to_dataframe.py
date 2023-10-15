import os

import yaml
import pandas as pd


def process_yaml_file(data_file) -> dict:
    """Read yaml file and return data as dictionary."""
    if not os.path.exists(data_file):
        raise FileNotFoundError

    file_ext = os.path.basename(data_file).split('.')[-1]
    if 'yaml' not in file_ext:
        raise ValueError('Unknown file type, expected YAML.')

    with open(data_file) as f:
        data = yaml.load(f, yaml.Loader)

    return data


if __name__ == "__main__":
    yaml_data = process_yaml_file('./data/student_sample.yaml')
    df = pd.DataFrame.from_records(yaml_data['Person'])
    print(df.head())
