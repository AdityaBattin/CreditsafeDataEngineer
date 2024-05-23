import os
import re
import datetime

def remove_blank_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    blank_lines = [index + 1 for index, line in enumerate(lines) if line.strip() == '']
    lines = [line for line in lines if line.strip() != '']

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    return blank_lines


def main(directory, file_pattern, log_file):
    # Start date and time
    start_time = datetime.datetime.now()

    # Logging start time
    with open(log_file, 'w', encoding='utf-8') as log:
        log.write(f"Start Date and Time: {start_time}\n")
        log.write("Files matched the pattern:\n")

    # Searching for files matching the pattern
    matched_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.match(file_pattern, file):
                matched_files.append(os.path.join(root, file))

    # Processing each matched file
    for file in matched_files:
        blank_lines = remove_blank_lines(file)
        if blank_lines:
            with open(log_file, 'a', encoding='utf-8') as log:
                log.write(f"File: {file}\n")
                for line_number in blank_lines:
                    log.write(f"Blank line at line number: {line_number}\n")
        else:
            with open(log_file, 'a', encoding='utf-8') as log:
                log.write(f"File: {file}\n")
                log.write("No blank lines found in this file.\n")

    # End date and time
    end_time = datetime.datetime.now()

    # Logging end time
    with open(log_file, 'a', encoding='utf-8') as log:
        log.write(f"End Date and Time: {end_time}\n\n")


if __name__ == "__main__":
    directory = r"C:\Users\CSINAABN\OneDrive - Creditsafe\Desktop\CRO DDATA FIX"
    file_pattern = r"Ddata_\d+_\d+\.dat"
    log_file = "log.txt"

    main(directory, file_pattern, log_file)
