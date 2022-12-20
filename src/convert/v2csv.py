# Import the necessary modules
import vobject
import csv
from . import vcarComponent

def vcard2csv(input_path, output_path):
    # Read the vCard file
    with open(input_path, "r") as f:
        vcard_data = f.read()
        vcard = vobject.readOne(vcard_data)

    # Create the CSV writer
    csv_file = open(output_path, "w")
    csv_writer = csv.writer(csv_file, delimiter=",")

    # Write the headers
    csv_writer.writerow(vcarComponent.column_order)

    # Write the vcard
    vcard_info = vcarComponent.get_info_list(vcard, input_path)
    csv_writer.writerow(list(vcard_info.values()))

    # Close the CSV file
    csv_file.close()


# vcard2csv("../../rsc/john-doe.vcf", "../../rsc/john-doe.csv")
