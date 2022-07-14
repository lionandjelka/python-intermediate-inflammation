"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import numpy as np


class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value
    def __str__(self):
        return self.value
    def __eq__(self, other):
        return (self.day,self.value) == (other.day,other.value)

class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name


class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name, observations=None):
        super().__init__(name)
        self.observations = []
        if observations is not None:
            self.observations = observations

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1
            except IndexError:
                day = 0
        new_observation = Observation(value, day)
        self.observations.append(new_observation)
        return new_observation

    def __eq__(self, other):
        return (self.name, self.observations) == (other.name, other.observations)


class Doctor(Person):
    """A doctor in an inflammation study."""

    def __init__(self, name):
        super().__init__(name)
        self.patients = []

    def add_patient(self, new_patient):
        # A crude check by name if this patient is already looked after
        # by this doctor before adding them
        for patient in self.patients:
            if patient.name == new_patient.name:
                return
        self.patients.append(new_patient)


def load_csv(filename):
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    return np.mean(data, axis=0)


def daily_max(data):
    return np.max(data, axis=0)


def daily_min(data):
    return np.min(data, axis=0)

    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')


def patient_normalise(data):
    """
    Normalise patient data between 0 and 1 of a 2D inflammation data array.

    Any NaN values are ignored, and normalised to 0

    :param data: 2D array of inflammation data
    :type data: ndarray

    """
    if not isinstance(data, np.ndarray):
        raise TypeError('data input should be ndarray')
    if len(data.shape) != 2:
        raise ValueError('inflammation array should be 2-dimensional')
    if np.any(data < 0):
        raise ValueError('inflammation values should be non-negative')
    max_data = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    return normalised