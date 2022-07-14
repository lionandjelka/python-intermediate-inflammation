# file: tests/test_serializers.py

from inflammation import mdl, serializers

def test_patients_json_serializer():
    # Create some test data
    patients = [
        mdl.Patient('Alice', [mdl.Observation(i, i + 1) for i in range(3)]),
        mdl.Patient('Bob', [mdl.Observation(i, 2 * i) for i in range(3)]),
    ]

    # Save and reload the data
    output_file = 'patients.json'
    serializers.PatientJSONSerializer.save(patients, output_file)
    patients_new = serializers.PatientJSONSerializer.load(output_file)

    # Check that we've got the same data back
#  for patient_new, patient in zip(patients_new, patients):
    assert patients_new == patients

      #  for obs_new, obs in zip(patient_new.observations, patient.observations):
      #      assert obs_new.day == obs.day
       #     assert obs_new.value == obs.value