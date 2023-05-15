import os

import xmltodict

from datetime import datetime


def obtain_row_dict(xml_path):
    """This function takes in a path to an XML file and returns a dictionary with the data
    from the XML file in a long format.
    """
    # Read the xml file
    with open(xml_path, "r", encoding="utf-8") as xml_f:
        xml_content = xmltodict.parse(xml_f.read())
        xml_content = xml_content["Bat-Call_PatientData"]

    # Get the long format of the data
    long_data_row = get_long_df(xml_content)
    # Add the location (care facility) and the date to the dictionary
    # long_data_row['Location'] = get_location(xml_path)
    long_data_row['RecordDate'] = get_date(xml_path)
    # Add a unique identifier for each patient
    # try:
        # long_data_row['PatientIdentifierUnique'] = long_data_row['PatientIdentifier'] + '-' + long_data_row['Location']
    # except KeyError:
        # long_data_row['PatientIdentifierUnique'] = None
        # pass

    return long_data_row


def get_long_df(dictionary, prefix=''):
    """This function takes a dictionary and flattens it into a single row.
    It takes a prefix argument that is used to build a key hierarchy.

    Args:
        dictionary (dict): a dictionary with nested dictionaries
        prefix (str): a prefix to be added to the keys

    Returns:
        dict: a dictionary with a single row
    """
    entry = {}
    if isinstance(dictionary, dict):
        for k, v in dictionary.items():
            if isinstance(v, str):
                if k == "LungDisease":
                    is_asthma, is_copd, is_emphysema, is_chronic_bronchitis, is_lung_cancer, lung_disease = process_lung_disease(v)
                    entry["Asthma"] = is_asthma
                    entry["COPD"] = is_copd
                    entry["Emphysema"] = is_emphysema
                    entry["ChronicBronchitis"] = is_chronic_bronchitis
                    entry["LungCancer"] = is_lung_cancer
                    entry["LungDisease"] = lung_disease.replace('\n', ' | ').replace(',', ';').lower()
                elif k == "HeartDisease":
                    is_hypertension, is_angina_pectoris, is_myocardial_infarction, is_heart_failure, heart_disease = process_heart_disease(v)
                    entry["Hypertension"] = is_hypertension
                    entry["AnginaPectoris"] = is_angina_pectoris
                    entry["MyocardialInfarction"] = is_myocardial_infarction
                    entry["HeartFailure"] = is_heart_failure
                    entry["HeartDisease"] = heart_disease.replace('\n', ' | ').replace(',', ';').lower()
                elif k == "HeartRate" or k == "SpO2":
                    entry[prefix + k] = change_no_measurement_to_none(v)
                elif k == "DisqualifyPatient":
                    entry[prefix + k] = encode_disqualify_patient(v)
                elif k == "Health":
                    entry[prefix + k] = encode_health(v)
                elif k == "Statement":
                    entry[prefix + k] = encode_statement(v)
                elif k == "SmokingHabit":
                    entry[prefix + k] = encode_smoking_habit(v)
                elif k == "Coughing" or k == "Fatigue" or k == "ShortnessOfBreath":
                    entry[prefix + k] = encode_cfs(v)
                elif k == "PatientParticipation":
                    entry[prefix + k] = encode_patient_participation(v)
                elif k == "Diabetes":
                    entry[prefix + k] = encode_diabetes(v)
                elif k == "DailyCough":
                    entry[prefix + k] = encode_daily_cough(v)
                elif k == "RespiratoryInfection":
                    entry[prefix + k] = encode_respiratory_infection(v)
                else:
                    # Sanitize the string
                    entry[prefix + k] = v.replace('\n', ' | ').replace(',', ';').lower()
            else:
                entry = {**entry, **get_long_df(v, prefix=(prefix + k +'_'))}
    return entry


def process_lung_disease(entry):
    """Extract standardised input from `LungDisease`."""
    is_asthma = None
    is_copd = None
    is_emphysema = None
    is_chronic_bronchitis = None
    is_lung_cancer = None

    test_entry = entry.lower()
    if "none" in test_entry:
        return is_asthma, is_copd, is_emphysema, is_chronic_bronchitis, is_lung_cancer, ""
    if "asthma" in test_entry:
        is_asthma = True
        test_entry = test_entry.replace("asthma", "")
    if "copd" in test_entry:
        is_copd = True
        test_entry = test_entry.replace("copd", "")
    if "emphysema" in test_entry:
        is_emphysema = True
        test_entry = test_entry.replace("emphysema", "")
    if "chronic bronchitis" in test_entry:
        is_chronic_bronchitis = True
        test_entry = test_entry.replace("chronic bronchitis", "")
    if "lung cancer" in test_entry:
        is_lung_cancer = True
        test_entry = test_entry.replace("lung cancer", "")

    test_entry = test_entry.replace("- ", " ").strip()

    return is_asthma, is_copd, is_emphysema, is_chronic_bronchitis, is_lung_cancer, test_entry


def process_heart_disease(entry):
    """Extract standardised input from `HeartDisease`."""
    is_hypertension = None
    is_angina_pectoris = None
    is_myocardial_infarction = None
    is_heart_failure = None

    test_entry = entry.lower()
    if "none" in test_entry:
        return is_hypertension, is_angina_pectoris, is_myocardial_infarction, is_heart_failure, ""
    if "hypertension" in test_entry:
        is_hypertension = True
        test_entry = test_entry.replace("hypertension", "")
    if "angina pectoris" in test_entry:
        is_angina_pectoris = True
        test_entry = test_entry.replace("angina pectoris", "")
    if "myocardial infraction" in test_entry:
        is_myocardial_infarction = True
        test_entry = test_entry.replace("myocardial infraction", "")
    if "heart failure" in test_entry:
        is_heart_failure = True
        test_entry = test_entry.replace("heart failure", "")

    test_entry = test_entry.replace("- ", " ").strip()

    return is_hypertension, is_angina_pectoris, is_myocardial_infarction, is_heart_failure, test_entry


def change_no_measurement_to_none(entry):
    """Extract standardised input from `SpO2`."""
    if "no measurement" in entry.lower():
        return None
    else:
        return entry.replace('\n', ' | ').replace(',', ';').lower()


def encode_disqualify_patient(entry):
    """Encode `DisqualifyPatient` as categorical variable."""
    # Lack of information: -1
    idx = False
    if entry.lower() == 'disqualify patient':
        idx = True
    else:
        raise ValueError('Unknown value for DisqualifyPatient: {}'.format(entry))
    return idx


def encode_health(entry):
    """Encode `Health` as categorical variable."""
    # Lack of information: -1
    idx = -1
    if entry.lower() == 'very bad':
        idx = 0
    elif entry.lower() == 'bad':
        idx = 1
    elif entry.lower() == 'neither good or bad':
        idx = 2
    elif entry.lower() == 'good':
        idx = 3
    elif entry.lower() == 'very good':
        idx = 4
    else:
        raise ValueError('Unknown value for Health: {}'.format(entry))
    return idx


def encode_statement(entry):
    """Encode `Statement` as categorical variable."""
    # Lack of information: -1
    idx = -1
    if entry.lower().replace('\n', '') == 'i only get breathless with strenuous exercise.':
        idx = 0
    elif entry.lower().replace('\n', '') == 'i get short of breath when hurrying on level ground or walking up a slight hill.':
        idx = 1
    elif entry.lower().replace('\n', '') == 'on level ground i walk slower than people of the same age because of breathlessness or have to stop for breath when waking at my own pace.':
        idx = 2
    elif entry.lower().replace('\n', '') == 'i stop for breath after walking about 100 yards or after a few minutes on level ground.':
        idx = 3
    elif entry.lower().replace('\n', '') == 'i am too breathless to leave the house or i am breathless when dressing.':
        idx = 4
    else:
        raise ValueError('Unknown value for Statement: {}'.format(entry))
    return idx


def encode_smoking_habit(entry):
    """Encode `SmokingHabit` as categorical variable."""
    # Lack of information: -1
    idx = -1
    if entry.lower() == 'never smoked':
        idx = 0
    elif entry.lower() == 'ex-smoker':
        idx = 1
    elif entry.lower() == 'active smoker':
        idx = 2
    else:
        raise ValueError('Unknown value for SmokingHabit: {}'.format(entry))
    return idx


def encode_cfs(entry):
    """Encode `Coughing`, `Fatigue`, `ShortnessOfBreath` as categorical variable."""
    # Lack of information: -1
    idx = -1
    if entry.lower() == 'normal or better':
        idx = 0
    elif entry.lower() == 'somewhat worse than normal':
        idx = 1
    elif entry.lower() == 'much worse than normal':
        idx = 2
    else:
        raise ValueError('Unknown value for CFS: {}'.format(entry))
    return idx


def encode_patient_participation(entry):
    """Encode `PatientParticipation` statement as categorical variable."""
    # Lack of information: -1
    idx = -1
    if entry.lower().replace('\n', '') == 'continue participation':
        idx = 0
    elif entry.lower().replace('\n', '') == 'intensive care with future return':
        idx = 1
    elif entry.lower().replace('\n', '').replace("–", "-") == 'intensive care - discontinued':
        idx = 2
    elif entry.lower().replace('\n', '').replace("–", "-") == 'personal request - discontinued':
        idx = 3
    elif entry.lower().replace('\n', '') == 'end of trial':
        idx = 4
    elif entry.lower().replace('\n', '') == 'other...':
        idx = 5
    else:
        raise ValueError('Unknown value for PatientParticipation: {}'.format(entry))
    return idx


def encode_diabetes(entry):
    """Encode `Diabetes` as categorical variable."""
    # Lack of information: None
    idx = None
    if entry.lower() == 'no':
        idx = False
    elif entry.lower() == 'yes':
        idx = True
    elif entry.lower() == 'diabetes':
        idx = True
    else:
        raise ValueError('Unknown value for Diabetes: {}'.format(entry))
    return idx


def encode_daily_cough(entry):
    # Lack of information: None
    idx = None
    if entry.lower() == 'no':
        idx = False
    elif entry.lower() == 'yes':
        idx = True
    else:
        raise ValueError('Unknown value for DailyCough: {}'.format(entry))
    return idx


def encode_respiratory_infection(entry):
    # Lack of information: None
    idx = None
    if entry.lower() == 'no':
        idx = False
    elif entry.lower() == 'yes':
        idx = True
    else:
        raise ValueError('Unknown value for RespiratoryInfection: {}'.format(entry))
    return idx


def get_location(path):
    """Return the location (care facility) where files were recorded."""
    try:
        location = path.split('/')[-5]
    except IndexError:
        location = None
    return location


def get_date(xml_path):
    """Get the date from the path to the xml file.
    If there is only one date, return that date.
    If there are multiple dates, return the date that has some recordings collected.

    Args:
        xml_path (str): path to the xml file

    Returns:
        str: date in the format YYYY-MM-DD
    """
    directory_path = os.path.dirname(xml_path)
    # Get all the dates-directories in the directory of the xml file
    dates = [x.path for x in os.scandir(directory_path) if os.path.isdir(x)]

    # If there are multiple dates, return the date that has some recordings collected
    # Remark: it does not happen that there are multiple dates with recordings collected
    if len(dates) > 1:
        nonempty_dates = []
        for date in dates:
            single_date = os.path.basename(date)
            if len(os.listdir(date)) > 1:
                nonempty_dates.append(single_date)
        # assert len(nonempty_dates) == 1, (xml_path, nonempty_dates)
        if len(nonempty_dates) > 1:
            print(xml_path, nonempty_dates)
        return datetime.strptime(nonempty_dates[-1], '%Y_%m_%d').strftime('%Y-%m-%d')

    # If there is only one date, return that date (provided that some recordings were collected)
    if len(dates) == 1:
        assert len(os.listdir(dates[0])) > 0
        return datetime.strptime(os.path.basename(dates[0]), '%Y_%m_%d').strftime('%Y-%m-%d')

    # If there are no dates, return None
    return None
