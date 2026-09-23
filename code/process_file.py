"""
process_file.py — Part 2: one file of package descriptions, uploaded.

A Streamlit app that accepts an uploaded text file with one package description
per line, shows the total for every line, and writes the parsed packages to a
JSON file in the `data/` folder — `data/packaging1.txt` in, `data/packaging1.json`
out.

New here: an uploaded file arrives as **bytes**, not text, so it has to be
decoded before it can be split into lines. And a text file usually ends with a
newline, so the last "line" is empty and must be skipped rather than parsed.

Run it:  Run and Debug -> "Streamlit Run: Current File"   (see README Reference #1)
Test it: pytest tests/test_streamlit.py -k process_file
"""

# --- The page ---------------------------------------------------------------------
#
# Less scaffolding this time. The steps are described, but which widget and which
# function does each job — and what to call the result — is now yours to work out.
# `one_package.py` is your worked example for anything structural, and README
# Reference #4 and #5 cover the two things that are new here.

import streamlit as st
import json
from packaging_parser import calc_total_units, get_unit, parse_packaging 

st.title("Process File of Packages")

package_data = st.file_uploader("Select a file to process", key="package_data",type=["txt"])
if package_data is not None:
    filename = package_data.name
    data = package_data.read()
    string_data = data.decode()
    list_data = string_data.split("\n")

    result_list = []
    for line in list_data:
        if line != "":
            line2 = line.strip()
            package = parse_packaging(line2)
            result_list.append(package)
            total = calc_total_units(package)
            unit = get_unit(package)
            st.info(f"{line} ➡️ Total📦 Size: {total} {unit}")

    with open(f'data/{filename.replace(".txt", ".json")}', 'w') as file:
        json.dump(result_list, file)
        
    num = len(result_list)
    st.success(f"{num} packages written to data/{filename.replace('.txt', '.json')}")