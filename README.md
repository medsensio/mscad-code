# Medsensio-Sanolla Cardiopulmonary Auscultation Dataset [MSCAD] - a dataset of lung & heart auscultation recordings as well as vitals data for COVID and chronic patients [CODE]

This repository contains supplemental code for the [PyxY.ai project](https://pyxy.ai/).

The data can be found on [Zenodo](https://zenodo.org/record/5527700).

The code is available on [GitHub](https://github.com/medsensio/mscad-code).

```text
This project has received funding from the European Union's Horizon 2020 research
and innovation programme under grant agreement No 101016046.
```

```text
Data in the "Medsensio-Sanolla Cardiopulmonary Auscultation Dataset [MSCAD] -
a dataset of lung & heart auscultation recordings as well as vitals data for COVID and chronic patients."
is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 Unported License.
```

```text
Code in the "Medsensio-Sanolla Cardiopulmonary Auscultation Dataset [MSCAD] -
a dataset of lung & heart auscultation recordings as well as vitals data for COVID and chronic patients."
is licensed under the MIT License.
```

This is a comprehensive clinical database that contains information from confirmed COVID-19 patients,
individuals who are at higher risk for COVID-19, and healthy patients.
The data was collected as part of the [PyxY.ai project](https://pyxy.ai/), which is funded under the Horizon 2020 program.
The dataset has been collected specifically to aid in the development of the PyXy.ai system.
In line with the Horizon 2020 open research data pilot, the data will be made available for public access.

## Running the scripts

1. All scripts were tested on Python 3.11.
2. Python requirements are listed in the `requirements.txt` file.
    Note that the pySoX library requires the SoX library to be installed on the system.
    Consult the official [SoX page](https://sox.sourceforge.net/) for installation instructions.
3. For the ease of use, we provide a `Dockerfile` that can be used to build a Docker image
    with all the required dependencies installed.
4. If you have Docker installed in your system, you can use provided `Makefile` to
    quickly build (`make build_docker`) and run (`make run_docker`) the Docker image.
