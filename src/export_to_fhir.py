import glob
import os

from utils.general import dump_json_to_file, read_json_from_file
from utils.fhir import get_patient, get_encounter, get_bundle
from utils.fhir import age_group_observation
from utils.fhir import blood_pressure_diastolic_observation, blood_pressure_systolic_observation
from utils.fhir import body_temperature_observation, weight_observation
from utils.fhir import respiratory_rate_observation, respiratory_rate_30s_observation
from utils.fhir import pulse_oximetry_observation, spirometry_fev1prcnt_observation
from utils.fhir import auscultation_sound_media
from utils.fhir import patient_history_questionnaire_response
from utils.fhir import background_disease_questionnaire_response
from utils.fhir import change_in_care_questionnaire_response
from utils.fhir import current_condition_questionnaire_response
from utils.xml_processing import obtain_row_dict


COUNTRY_CODES = {
    "Germany": "DEU",
    "Spain": "ESP",
    "Norway": "NOR",
    "Israel": "ISR",
    None: None,
}

GENDER_CORRECT = [
    "male",
    "female",
    "other",
    "unknown",
    None,
]

BREATHLESSNESS_CODES = {
    None: None,
    0: ("ph-breathlessness-0", "I only get breathless when I do strenuous exercise"),
    1: ("ph-breathlessness-1", "I get short of breath when hurrying on the level or walking up a slight hil"),
    2: ("ph-breathlessness-2", "On level ground I walk slower than people of the same age because of breathlessness or have to stop for breath w),n walking at my own pace"),
    3: ("ph-breathlessness-3", "I stop for breath after walking about 100 yards or after a few minutes on the level ground"),
    4: ("ph-breathlessness-4", "I am too breathless to leave the house or get out of breath when dressing or undressing"),
}

SMOKING_HABIT_CODES = {
    None: None,
    0: ("ph-smoking-0", "Never"),
    1: ("ph-smoking-1", "Ex-smoker"),
    2: ("ph-smoking-2", "Current smoker"),
}

PARTICIPATION_CODES = {
    None: None,
    0: ("pp-0", "Continue participation"),
    1: ("pp-1", "Intensive care with future return"),
    2: ("pp-2", "Intensive care - discontinued"),
    3: ("pp-3", "Personal request - discontinued"),
    4: ("pp-4", "End of trial"),
    5: ("pp-5", "Other"),
}


COUGHING_CODES = {
    None: None,
    0: ("cc-coughing-0", "Normal or better"),
    1: ("cc-coughing-1", "Somewhat worse than normal"),
    2: ("cc-coughing-2", "Much worse than normal"),
}

FATIGUE_CODES = {
    None: None,
    0: ("cc-fatigue-0", "Normal or better"),
    1: ("cc-fatigue-1", "Somewhat worse than normal"),
    2: ("cc-fatigue-2", "Much worse than normal"),
}

SOB_CODES= {
    None: None,
    0: ("cc-sob-0", "Normal or better"),
    1: ("cc-sob-1", "Somewhat worse than normal"),
    2: ("cc-sob-2", "Much worse than normal"),
}


XML_FAMILIES = [
    "raw_data--anonymised/28-11-2022/*/Data/input/*/*.xml",  # Horizon
    # "raw_data--anonymised/16-03-2022/*/Data/input/*/*.xml",  # Sanolla
]


def process_to_fhir():
    """Process all XML files and audio recordings to FHIR bundles.
    """
    for xml_path_format in XML_FAMILIES:
        all_xml_files = glob.glob(xml_path_format)

        for single_file in all_xml_files:
            long_data_row = obtain_row_dict(single_file)

            recordings = os.path.join(os.path.dirname(single_file), "*/locations.json")
            locations_paths = glob.glob(recordings)

            # Generate FHIR bundles
            tabular_bundle, patient_id, encounter_loc_id = process_entry(long_data_row)
            # Dump FHIR bundle to file
            dump_path = os.path.dirname(single_file).replace("raw_data", "fhir")
            dump_path = os.path.join(dump_path, "encounter_bundle.json")
            os.makedirs(os.path.dirname(dump_path), exist_ok=True)
            dump_json_to_file(dump_path, tabular_bundle.json(indent=4))

            # Generate FHIR bundles for audio recordings and dump to file
            _ = process_locations(locations_paths, patient_id, encounter_loc_id)


def process_entry(row_dict):
    """Process a single row of data from the XML file."""

    # Get patient ID
    patient_id = row_dict.get("PatientIdentifier")

    # Get country code
    country = row_dict.get("Country")
    country = country.capitalize() if country else None
    assert country in COUNTRY_CODES, f"Country {country} not in COUNTRY_CODES"

    # Get correct gender
    gender = row_dict.get("Gender")
    gender = gender.lower() if gender else None
    assert gender in GENDER_CORRECT, f"Gender {gender} not in GENDER_CORRECT"

    # Get practitioner ID
    practitioner_id = row_dict.get("CollectorNameID")
    # Get encounter ID
    encounter_id = row_dict.get("SerialNumber")
    # Get encounter date
    encounter_date = row_dict.get("RecordDate")  # YYYY-MM-DD


    # Get patient resource
    patient = get_patient(
        patient_id,
        COUNTRY_CODES[country],
        gender,
    )

    # Get encounter resource
    encounter = get_encounter(
        patient_id,
        practitioner_id,
        encounter_id,
        encounter_date,
    )

    # Collect all observations
    observations = []

    age_group = row_dict.get("Age")
    if age_group:
        age_group_obs = age_group_observation("ag-" + age_group, patient_id)
        observations.append(age_group_obs)

    diastolic = row_dict.get("Diastolic")
    if diastolic:
        diastolic_obs = blood_pressure_diastolic_observation(int(diastolic), encounter_id, patient_id)
        observations.append(diastolic_obs)

    systolic = row_dict.get("Systolic")
    if systolic:
        systolic_obs = blood_pressure_systolic_observation(int(systolic), encounter_id, patient_id)
        observations.append(systolic_obs)

    temperature = row_dict.get("BodyTemperature")
    if temperature:
        temperature_obs = body_temperature_observation(float(temperature), encounter_id, patient_id)
        observations.append(temperature_obs)

    respiratory_rate_30 = row_dict.get("RespiratoryRate30Sec")
    if respiratory_rate_30:
        respiratory_rate_30_obs = respiratory_rate_30s_observation(int(respiratory_rate_30), encounter_id, patient_id)
        observations.append(respiratory_rate_30_obs)

    respiratory_rate_1 = row_dict.get("RespiratoryRateInOneMinute")
    if respiratory_rate_1:
        respiratory_rate_1_obs = respiratory_rate_observation(int(respiratory_rate_1), encounter_id, patient_id)
        observations.append(respiratory_rate_1_obs)

    pulse_oximetry = row_dict.get("PulseOximetry")
    if pulse_oximetry:
        pulse_oximetry_obs = pulse_oximetry_observation(float(pulse_oximetry), encounter_id, patient_id)
        observations.append(pulse_oximetry_obs)

    weight = row_dict.get("Weight")
    if weight:
        try:
            weight_obs = weight_observation(float(weight), encounter_id, patient_id)
            observations.append(weight_obs)
        except ValueError:
            print("Weight is not float-converible: ", weight, " for patient ", patient_id)

    spirometry_fev1prcnt = row_dict.get("Spirometry")
    if spirometry_fev1prcnt:
        spirometry_fev1prcnt_obs = spirometry_fev1prcnt_observation(float(spirometry_fev1prcnt), encounter_id, patient_id)
        observations.append(spirometry_fev1prcnt_obs)


    # Collect all questionnaires
    questionnaires = []

    patient_history = patient_history_questionnaire_response(
        patient_id,
        encounter_id,
        practitioner_id,
        daily_medication=row_dict.get("DailyMedication"),
        daily_cough=row_dict.get("DailyCough"),
        breathlessness_code_and_statement=BREATHLESSNESS_CODES[row_dict.get("Statement")],
        smoking_habit_code_and_statement=SMOKING_HABIT_CODES[row_dict.get("SmokingHabit")],
        average_cigarettes_per_day=row_dict.get("CigarettesPerDay"),
        years_smoking=row_dict.get("YearsOfSmoking"),
        disqualify_patient=row_dict.get("DisqualifyPatient"),
    )
    questionnaires.append(patient_history)


    background_disease = background_disease_questionnaire_response(
        patient_id,
        encounter_id,
        practitioner_id,
        asthma=row_dict.get("Asthma"),
        copd=row_dict.get("COPD"),
        emphysema=row_dict.get("Emphysema"),
        chronic_bronchitis=row_dict.get("ChronicBronchitis"),
        lung_cancer=row_dict.get("LungCancer"),
        hypertension=row_dict.get("Hypertension"),
        angina_pectoris=row_dict.get("AnginaPectoris"),
        myocardial_infarction=row_dict.get("MyocardialInfarction"),
        heart_failure=row_dict.get("HeartFailure"),
        diabetes=row_dict.get("Diabetes"),
        current_respiratory_disease=row_dict.get("RespiratoryInfection"),
        other_lung_disease=row_dict.get("LungDisease"),
        other_cardiovascular_disease=row_dict.get("HeartDisease"),
    )
    questionnaires.append(background_disease)


    change_in_care = change_in_care_questionnaire_response(
        patient_id,
        encounter_id,
        practitioner_id,
        new_increased_medication=row_dict.get("NewIncreasedMedication"),
        patient_participation_code_and_statement=PARTICIPATION_CODES[row_dict.get("PatientParticipation")],
    )
    questionnaires.append(change_in_care)


    current_condition = current_condition_questionnaire_response(
        patient_id,
        encounter_id,
        practitioner_id,
        coughing_code_and_statement=COUGHING_CODES[row_dict.get("Coughing")],
        fatigue_code_and_statement=FATIGUE_CODES[row_dict.get("Fatigue")],
        sob_code_and_statement=SOB_CODES[row_dict.get("ShortnessOfBreath")],
    )
    questionnaires.append(current_condition)

    # Create tabular bundle
    tabular_bundle = get_bundle(
        patient,
        encounter,
        questionnaires,
        observations,
        None,
    )

    return tabular_bundle, patient_id, encounter_id


def process_locations(locations, patient_id, encounter_id):
    """Process locations.json files and create media bundles"""
    for single_file in locations:
        medias = []

        # Read locations.json
        locations = read_json_from_file(single_file)
        # Get directory (date) of locations.json
        directory = os.path.dirname(single_file)

        # Generate media resources
        for filename, code in locations.items():
            file_path = os.path.join(directory, filename)
            media = auscultation_sound_media(file_path, code, encounter_id, patient_id)
            medias.append(media)

        # Create media bundle
        media_bundle = get_bundle(
            None,
            None,
            [],
            [],
            medias,
        )

        # Dump media bundle to file
        dump_path = single_file.replace("raw_data", "fhir").replace("locations.json", "media_bundle.json")
        os.makedirs(os.path.dirname(dump_path), exist_ok=True)
        dump_json_to_file(dump_path, media_bundle.json(indent=4))


if __name__ == "__main__":
    process_to_fhir()
