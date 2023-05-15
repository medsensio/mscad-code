"""Factor functions for FHIR resources."""

from fhir.resources.patient import Patient
from fhir.resources.bundle import Bundle
from fhir.resources.bundle import BundleEntry
from fhir.resources.encounter import Encounter
from fhir.resources.media import Media
from fhir.resources.observation import Observation
from fhir.resources.questionnaireresponse import QuestionnaireResponse
from fhir.resources.questionnaireresponse import QuestionnaireResponseItem
from fhir.resources.questionnaireresponse import QuestionnaireResponseItemAnswer


# Age group observation
age_group_observation = lambda entry, patient_id: Observation(
    id="age-group",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    code={
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "46251-5",
                "display": "Age Group",
            }
        ]
    },
    valueCodeableConcept={
        "coding": [
            {
                "system": "./FHIR_CODING_SYSTEMS.md",
                "code": entry,
                "display": f"{entry.replace('ag-', '')}",
            }
        ]
    },
)


# Blood pressure (systolic) observation
blood_pressure_systolic_observation = lambda entry, encouter_id, patient_id: Observation(
    id="blood-pressure-systolic",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    encounter={
        "reference": f"Encounter/{encouter_id}",
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    code={
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "8480-6",
                "display": "Systolic blood pressure",
            }
        ]
    },
    valueQuantity={
        "value": entry,
        "unit": "mm[Hg]",
        "system": "http://unitsofmeasure.org",
        "code": "mm[Hg]",
    },
)


# Blood pressure (diastolic) observation
blood_pressure_diastolic_observation = lambda entry, encouter_id, patient_id: Observation(
    id="blood-pressure-diastolic",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    encounter={
        "reference": f"Encounter/{encouter_id}",
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    code={
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "8462-4",
                "display": "Diastolic blood pressure",
            }
        ]
    },
    valueQuantity={
        "value": entry,
        "unit": "mm[Hg]",
        "system": "http://unitsofmeasure.org",
        "code": "mm[Hg]",
    },
)


# Body temperature observation
body_temperature_observation = lambda entry, encouter_id, patient_id: Observation(
    id="body-temperature",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    encounter={
        "reference": f"Encounter/{encouter_id}",
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    code={
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "8310-5",
                "display": "Body temperature",
            }
        ]
    },
    valueQuantity={
        "value": entry,
        "unit": "Cel",
        "system": "http://unitsofmeasure.org",
        "code": "Cel",
    },
)


# Respiratory rate observation (30s)
respiratory_rate_30s_observation = lambda entry, encouter_id, patient_id: Observation(
    id="respiratory-rate-30s",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    encounter={
        "reference": f"Encounter/{encouter_id}",
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    code={
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "9279-1",
                "display": "Respiratory rate",
            }
        ]
    },
    valueQuantity={
        "value": entry,
        "unit": "/30s",
        "system": "http://unitsofmeasure.org",
        "code": "/30s",
    },
)


# Respiratory rate observation (1min)
respiratory_rate_observation = lambda entry, encouter_id, patient_id: Observation(
    id="respiratory-rate-1min",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    encounter={
        "reference": f"Encounter/{encouter_id}",
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    code={
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "9279-1",
                "display": "Respiratory rate",
            }
        ]
    },
    valueQuantity={
        "value": entry,
        "unit": "/min",
        "system": "http://unitsofmeasure.org",
        "code": "/min",
    },
)


# Pulse oximetry Observation Resource
pulse_oximetry_observation = lambda entry, encouter_id, patient_id: Observation(
    id="pulse-oximetry",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    encounter={
        "reference": f"Encounter/{encouter_id}",
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    code={
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "59408-5",
                "display": "Oxygen saturation in Arterial blood",
            }
        ]
    },
    valueQuantity={
        "value": entry,
        "unit": "%",
        "system": "http://unitsofmeasure.org",
        "code": "%",
    },
)


# Weight Observation Resource
weight_observation = lambda entry, encouter_id, patient_id: Observation(
    id="weight",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    encounter={
        "reference": f"Encounter/{encouter_id}",
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    code={
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "29463-7",
                "display": "Body weight",
            }
        ]
    },
    valueQuantity={
        "value": entry,
        "unit": "kg",
        "system": "http://unitsofmeasure.org",
        "code": "kg",
    },
)


# Spirometry Observation Resource
spirometry_fev1prcnt_observation = lambda entry, encouter_id, patient_id: Observation(
    id="spirometry",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    encounter={
        "reference": f"Encounter/{encouter_id}",
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    code={
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "19926-5",
                "display": "Forced expiratory volume in 1 second",
            }
        ]
    },
    valueQuantity={
        "value": entry,
        "unit": "%",
        "system": "http://unitsofmeasure.org",
        "code": "%",
    },
)


# Auscultation Sound Media Resource
auscultation_sound_media = lambda entry, code, encouter_id, patient_id: Media(
    id="auscultation-sound",
    status="final",
    meta={
        "versionId": "1.0.0",
        "lastUpdated": "2023-03-09T00:00:00Z"
    },
    encounter={
        "reference": f"Encounter/{encouter_id}",
    },
    subject={
        "reference": f"Patient/{patient_id}",
    },
    bodySite={
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": code,
                "display": code,
            }
        ]
    },
    content={
        "contentType": "audio/wav",
        "url": entry,
    }
)


def patient_history_questionnaire_response(
    patient_id,
    encounter_id,
    practitioner_id,
    daily_medication=None,
    daily_cough=None,
    breathlessness_code_and_statement=None,
    smoking_habit_code_and_statement=None,
    average_cigarettes_per_day=None,
    years_smoking=None,
    disqualify_patient=None,
):
    """Create a Patient History QuestionnaireResponse FHIR resource.

    Args:
        patient_id (str): The ID of the patient.
        encounter_id (str): The ID of the encounter.
        practitioner_id (str): The ID of the practitioner.
        daily_medication (str, optional): The patient's daily medication. Defaults to None.
        daily_cough (bool, optional): The patient's daily cough. Defaults to None.
        breathlessness_code_and_statement (tuple, optional): The patient's breathlessness code and statement. Defaults to None.
        smoking_habit_code_and_statement (tuple, optional): The patient's smoking habit code and statement. Defaults to None.
        average_cigarettes_per_day (int, optional): The patient's average cigarettes per day. Defaults to None.
        years_smoking (int, optional): The patient's years smoking. Defaults to None.
        disqualify_patient (bool, optional): Whether the patient should be disqualified. Defaults to None.

    Returns:
        QuestionnaireResponse: The Patient History QuestionnaireResponse FHIR resource.
    """
    items = []

    if daily_medication is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="ph-daily-medication",
                text="Daily Medication (name + dosage + time/day)",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueString=daily_medication
                    )
                ]
            ),
        )

    if smoking_habit_code_and_statement is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="ph-smoking",
                text="Smoking Habit",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueCoding={
                            "system": "./FHIR_CODING_SYSTEMS.md",
                            "code": smoking_habit_code_and_statement[0],
                            "display": smoking_habit_code_and_statement[1],
                        }
                    )
                ]
            ),
        )

    if daily_cough is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="ph-daily-cough",
                text="Daily Cough",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueBoolean=daily_cough,
                    )
                ]
            ),
        )

    if breathlessness_code_and_statement is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="ph-breathlessness",
                text="Self-statement about breathlessness",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueCoding={
                            "system": "./FHIR_CODING_SYSTEMS.md",
                            "code": breathlessness_code_and_statement[0],
                            "display": breathlessness_code_and_statement[1],
                        }
                    )
                ]
            ),
        )

    if average_cigarettes_per_day is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="cigarettes-per-day",
                text="Cigarettes per day? (Average)",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueInteger=average_cigarettes_per_day,
                    )
                ]
            )
        )

    if years_smoking is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="years-smoking",
                text="Years of smoking",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueInteger=years_smoking,
                    )
                ]
            )
        )

    if disqualify_patient is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="disqualify-patient",
                text="Disqualify patient?",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueBoolean=disqualify_patient,
                    )
                ]
            )
        )

    return QuestionnaireResponse(
        id="patient-history",
        status="completed",
        meta={
            "versionId": "1.0.0",
            "lastUpdated": "2023-03-09T00:00:00Z"
        },
        subject={
            "reference": f"Patient/{patient_id}",
            "type": "Patient",
        },
        encounter={
            "reference": f"Encounter/{encounter_id}",
            "type": "Encounter",
        },
        author={
            "reference": f"Practitioner/{practitioner_id}",
            "type": "Practitioner",
        },
        source={
            "reference": f"Patient/{patient_id}",
            "type": "Patient",
        },
        item=items,
    )


def background_disease_questionnaire_response(
        patient_id,
        encounter_id,
        practitioner_id,
        asthma=False,
        copd=False,
        emphysema=False,
        chronic_bronchitis=False,
        lung_cancer=False,
        hypertension=False,
        angina_pectoris=False,
        myocardial_infarction=False,
        heart_failure=False,
        diabetes=False,
        current_respiratory_disease=False,
        other_lung_disease=None,
        other_cardiovascular_disease=None,
):
    """Create a QuestionnaireResponse for the Background Disease Questionnaire.

    Args:
        patient_id (str): The ID of the patient.
        encounter_id (str): The ID of the encounter.
        practitioner_id (str): The ID of the practitioner.
        asthma (bool): Whether the patient has asthma.
        copd (bool): Whether the patient has COPD.
        emphysema (bool): Whether the patient has emphysema.
        chronic_bronchitis (bool): Whether the patient has chronic bronchitis.
        lung_cancer (bool): Whether the patient has lung cancer.
        hypertension (bool): Whether the patient has hypertension.
        angina_pectoris (bool): Whether the patient has angina pectoris.
        myocardial_infarction (bool): Whether the patient has myocardial infarction.
        heart_failure (bool): Whether the patient has heart failure.
        diabetes (bool): Whether the patient has diabetes.
        current_respiratory_disease (bool): Whether the patient has a current respiratory disease.
        other_lung_disease (str): Other lung disease.
        other_cardiovascular_disease (str): Other cardiovascular disease.

    Returns:
        QuestionnaireResponse: The QuestionnaireResponse for the Background Disease Questionnaire.
    """
    answers_lung = []
    answers_cv = []
    answers_other = []

    # Lung
    if asthma:
        answers_lung.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-lung-asthma",
                    "display": "Asthma"
                }
            )
        )
    if copd:
        answers_lung.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-lung-copd",
                    "display": "COPD"
                }
            )
        )
    if emphysema:
        answers_lung.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-lung-emphysema",
                    "display": "Emphysema"
                }
            )
        )
    if chronic_bronchitis:
        answers_lung.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-lung-chronic-bronchitis",
                    "display": "Chronic Bronchitis"
                }
            )
        )
    if lung_cancer:
        answers_lung.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-lung-lung-cancer",
                    "display": "Lung Cancer"
                }
            )
        )

    # Cardiovascular
    if hypertension:
        answers_cv.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-cv-hypertension",
                    "display": "Hypertension"
                }
            )
        )
    if angina_pectoris:
        answers_cv.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-cv-angina-pectoris",
                    "display": "Angina Pectoris"
                }
            )
        )
    if myocardial_infarction:
        answers_cv.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-cv-myocardial-infarction",
                    "display": "Myocardial Infarction"
                }
            )
        )
    if heart_failure:
        answers_cv.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-cv-heart-failure",
                    "display": "Heart Failure"
                }
            )
        )

    # Other
    if diabetes:
        answers_other.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-other-diabetes",
                    "display": "Diabetes"
                }
            )
        )
    if current_respiratory_disease:
        answers_other.append(
            QuestionnaireResponseItemAnswer(
                valueCoding={
                    "system": "./FHIR_CODING_SYSTEMS.md",
                    "code": "bd-other-cri",
                    "display": "Current Respiratory Disease"
                }
            )
        )

    # Text answers
    if other_lung_disease is not None and other_lung_disease != "":
        answers_lung.append(
            QuestionnaireResponseItemAnswer(
                valueString=other_lung_disease,
            )
        )

    if other_cardiovascular_disease is not None and other_cardiovascular_disease != "":
        answers_cv.append(
            QuestionnaireResponseItemAnswer(
                valueString=other_cardiovascular_disease,
            )
        )


    items = []
    if answers_lung != []:
        items.append(
            QuestionnaireResponseItem(
                linkId="bd-lung",
                text="Chronic Lung Disease",
                answer=answers_lung,
            )
        )
    if answers_cv != []:
        items.append(
            QuestionnaireResponseItem(
                linkId="bd-cv",
                text="Chronic Cardiovascular Disease",
                answer=answers_cv,
            )
        )
    if answers_other != []:
        items.append(
            QuestionnaireResponseItem(
                linkId="bd-other",
                text="Other",
                answer=answers_other,
            )
        )


    return QuestionnaireResponse(
        id="background-disease",
        status="completed",
        meta={
            "versionId": "1.0.0",
            "lastUpdated": "2023-03-09T00:00:00Z"
        },
        subject={
            "reference": f"Patient/{patient_id}",
            "type": "Patient",
        },
        encounter={
            "reference": f"Encounter/{encounter_id}",
            "type": "Encounter",
        },
        author={
            "reference": f"Practitioner/{practitioner_id}",
            "type": "Practitioner",
        },
        source={
            "reference": f"Patient/{patient_id}",
            "type": "Patient",
        },
        item=items
    )


def change_in_care_questionnaire_response(
        patient_id,
        encounter_id,
        practitioner_id,
        new_increased_medication,
        patient_participation_code_and_statement,
):
    """Create a QuestionnaireResponse for the Change in Care questionnaire.

    Args:
        patient_id (str): The ID of the patient.
        encounter_id (str): The ID of the encounter.
        practitioner_id (str): The ID of the practitioner.
        new_increased_medication (str): The new or increased medication.
        patient_participation_code_and_statement (tuple): The patient participation code and statement.

    Returns:
        QuestionnaireResponse: The QuestionnaireResponse for the Change in Care questionnaire.
    """
    items = []

    if new_increased_medication is not None and new_increased_medication != "":
        items.append(
            QuestionnaireResponseItem(
                linkId="1",
                text="New or Increased Medication (name + dosage + time/day)",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueString=new_increased_medication,
                    )
                ]
            ),
        )

    if patient_participation_code_and_statement is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="2",
                text="Patient participation",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueCoding={
                            "system": "./FHIR_CODING_SYSTEMS.md",
                            "code": patient_participation_code_and_statement[0],
                            "display": patient_participation_code_and_statement[1],
                        }
                    )
                ]
            ),
        )

    return QuestionnaireResponse(
        id="change-in-care",
        status="completed",
        meta={
            "versionId": "1.0.0",
            "lastUpdated": "2023-03-09T00:00:00Z"
        },
        subject={
            "reference": f"Patient/{patient_id}",
            "type": "Patient",
        },
        encounter={
            "reference": f"Encounter/{encounter_id}",
            "type": "Encounter",
        },
        author={
            "reference": f"Practitioner/{practitioner_id}",
            "type": "Practitioner",
        },
        source={
            "reference": f"Patient/{patient_id}",
            "type": "Patient",
        },
        item=items
    )


def current_condition_questionnaire_response(
        patient_id,
        encounter_id,
        practitioner_id,
        coughing_code_and_statement,
        fatigue_code_and_statement,
        sob_code_and_statement,
):
    """Create a QuestionnaireResponse for the current condition questionnaire.

    Args:
        patient_id (str): The ID of the patient.
        encounter_id (str): The ID of the encounter.
        practitioner_id (str): The ID of the practitioner.
        coughing_code_and_statement (tuple): A tuple of the coughing code and statement.
        fatigue_code_and_statement (tuple): A tuple of the fatigue code and statement.
        sob_code_and_statement (tuple): A tuple of the sob code and statement.

    Returns:
        QuestionnaireResponse: A QuestionnaireResponse for the current condition questionnaire.
    """
    items = []

    if coughing_code_and_statement is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="1",
                text="Coughing",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueCoding={
                            "system": "./FHIR_CODING_SYSTEMS.md",
                            "code": coughing_code_and_statement[0],
                            "display": coughing_code_and_statement[1],
                        }
                    )
                ]
            ),
        )

    if fatigue_code_and_statement is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="2",
                text="Fatigue",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueCoding={
                            "system": "./FHIR_CODING_SYSTEMS.md",
                            "code": fatigue_code_and_statement[0],
                            "display": fatigue_code_and_statement[1],
                        }
                    )
                ]
            ),
        )

    if sob_code_and_statement is not None:
        items.append(
            QuestionnaireResponseItem(
                linkId="3",
                text="Shortness of Breath",
                answer=[
                    QuestionnaireResponseItemAnswer(
                        valueCoding={
                            "system": "./FHIR_CODING_SYSTEMS.md",
                            "code": sob_code_and_statement[0],
                            "display": sob_code_and_statement[1],
                        }
                    )
                ]
            ),
        )

    return QuestionnaireResponse(
        id="current-condition",
        status="completed",
        meta={
            "versionId": "1.0.0",
            "lastUpdated": "2023-03-09T00:00:00Z"
        },
        subject={
            "reference": f"Patient/{patient_id}",
            "type": "Patient",
        },
        encounter={
            "reference": f"Encounter/{encounter_id}",
            "type": "Encounter",
        },
        author={
            "reference": f"Practitioner/{practitioner_id}",
            "type": "Practitioner",
        },
        source={
            "reference": f"Patient/{patient_id}",
            "type": "Patient",
        },
        item=items,
    )


def get_encounter(
        patient_id,
        practitioner_id,
        encounter_id,
        encounter_date,
        # organization_id,
):
    """Create an encounter resource.

    Args:
        patient_id (str): The patient id.
        practitioner_id (str): The practitioner id.
        encounter_id (str): The encounter id.
        encounter_date (str): The encounter date.
        organization_id (str): The organization id.

    Returns:
        Encounter: The encounter resource.
    """
    return Encounter(
        id=encounter_id,
        status="finished",
        meta={
            "versionId": "1.0.0",
            "lastUpdated": "2023-03-09T00:00:00Z"
        },
        subject={
            "reference": f"Patient/{patient_id}",
        },
        class_fhir={

        },
        period={
            "start": encounter_date,
            "end": encounter_date,
        },
        participant=[
            {
                "individual": {
                    "reference": f"Practitioner/{practitioner_id}",
                },
            },
        ],
    )


def get_patient(
        patient_id,
        country,
        gender,
):
    """Create a patient resource.

    Args:
        patient_id (str): The patient id.
        country (str): The country.
        gender (str): Geneder of the patient.

    Returns:
        Patient: The patient resource.
    """
    return Patient(
        id=patient_id,
        meta={
            "versionId": "1.0.0",
            "lastUpdated": "2023-03-09T00:00:00Z"
        },
        gender=gender,
        address=[
            {
                "country": country,
            }
        ],
    )


def get_bundle(
        patient=None,
        encounter=None,
        questionnaire_responses=None,
        observations=None,
        medias=None,
):
    """Create a bundle of resources.

    Args:
        patient (Patient): The patient resource.
        encounter (Encounter): The encounter resource.
        questionnaire_responses (List[QuestionnaireResponse]): The questionnaire response resources.
        observations (List[Observation]): The observation resources.
        medias (List[Media]): The media resources.

    Returns:
        Bundle: The bundle of resources.
    """
    entries = []

    if patient is not None:
        entries.append(
            BundleEntry(
                resource=patient,
            ),
        )
    if encounter is not None:
        entries.append(
            BundleEntry(
                resource=encounter,
            ),
        )
    if questionnaire_responses is not None:
        for qr in questionnaire_responses:
            entries.append(
                BundleEntry(
                    resource=qr,
                )
            )
    if observations is not None:
        for obs in observations:
            entries.append(
                BundleEntry(
                    resource=obs,
                )
            )
    if medias is not None:
        for media in medias:
            entries.append(
                BundleEntry(
                    resource=media,
                )
            )

    return Bundle(
        type="collection",
        meta={
            "versionId": "1.0.0",
            "lastUpdated": "2023-03-09T00:00:00Z"
        },
        entry=entries,
    )
