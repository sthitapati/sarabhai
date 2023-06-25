# this script includes all the classes and functions needed to process the raw data

import os
import argparse
import pandas as pd
import json


class ConfigParser:
    """
    Parses the metadata file and extracts relevant information.
    Supports JSON and CSV file formats.
    """

    def __init__(self, metadata_file):
        """
        Initialize the ConfigParser object.

        Parameters:
        - metadata_file (str): Path to the metadata file.
        """
        self.metadata_file = metadata_file
        self.Animal_ID = None
        self.Group = None
        self.Experiment = None
        self.Path_To_Raw_Data = None
        self.Output_Data_Folder = None
        self.CameraPath = None

    def parse_metadata(self):
        """
        Parses the metadata file based on the file extension.

        Raises:
        - ValueError: If the file format is unsupported.
        """
        file_extension = os.path.splitext(self.metadata_file)[1]

        if file_extension == '.json':
            self._parse_json()
        elif file_extension == '.csv':
            self._parse_csv()
        else:
            raise ValueError("Unsupported metadata file format.")

    def _parse_json(self):
        """
        Parses the metadata from a JSON file.
        """
        with open(self.metadata_file, 'r') as f:
            metadata = json.load(f)
        self.Animal_ID = metadata["Animal_ID"]
        self.Group = metadata["Group"]
        self.Experiment = metadata["Experiment"]
        self.Path_To_Raw_Data = metadata["Path_To_Raw_Data"]
        self.Output_Data_Folder = metadata["Output_Data_Folder"]
        self.CameraPath = metadata["CameraPath"]

    def _parse_csv(self):
        """
        Parses the metadata from a CSV file.
        """
        metadata = pd.read_csv(self.metadata_file)
        self.Animal_ID = metadata['Animal_ID'].tolist()
        self.Group = metadata['Group'].tolist()
        self.Experiment = metadata['Experiment'][0]
        self.Path_To_Raw_Data = metadata['Path_To_Raw_Data'][0]
        self.Output_Data_Folder = metadata['Output_Data_Folder'][0]
        self.CameraPath = metadata['CameraPath'][0]