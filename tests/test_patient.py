"""Tests for the Patient model."""


def test_create_patient():
    """Check a patient is created correctly given a name"""
    from inflammation.models import Patient
    name = 'Alice'
    p = Patient(name=name)
    assert p.name == name

def test_create_doctor():
    """Check a doctor is created correctly given a name"""
    from inflammation.models import Doctor
    name = 'Sheila W'
    doc = Doctor(name=name)
    assert doc.name == name

def test_doctor_is_person():
    """Check if a doctor is a person."""
    from inflammation.models import Doctor, Person
    doc = Doctor("Sheila Wheels")
    assert isinstance(doc, Person)

def test_patient_is_person():
    """Check if a patient is a person. """
    from inflammation.models import Patient, Person
    alice = Patient("Alice")
    assert isinstance(alice, Person)

