import argparse
import json
import inflammation
from inflammation import models, views
from inflammation import  serializers
import argparse
import pandas as pd


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    #patients_df = pd.read_json('/Users/andjelka/Documents/Vezba1/python-intermediate-inflammation/patients.json')
    infiles = args.infiles

    patients_new = serializers.PatientJSONSerializer.load('patients.json')
    for patient_new1 in patients_new:

        if patient_new1.name == args.patient:

            print(patient_new1.name)
            for obs_new in patient_new1.observations:
                print('day',obs_new.day, 'value',obs_new.value)



    #patients_df = pd.read_json(infiles)
    #print(patients_df.loc[patients_df['name'] == args.patient])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        help='Input JSON containing inflammation series for each patient')

    parser.add_argument(
        '--patient',
        type=str,
        default=0,
        help='Which patient should be displayed?')

    args = parser.parse_args()

    main(args)
