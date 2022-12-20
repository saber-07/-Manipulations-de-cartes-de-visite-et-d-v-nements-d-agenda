import argparse
from convert import v2h, v2csv, ics2html_vcf, vcarComponent
import os
import glob

# Define the command-line arguments
parser = argparse.ArgumentParser(description="Convert calendar and vcard")
parser.add_argument("-i", "--ics_file", type=str, help="The input calendar file")
parser.add_argument("-v", "--vcf_file", type=str, help="The input vcard file")
parser.add_argument("-t", "--html_file", type=str, help="The output HTML file")
parser.add_argument("-c", "--csv_file", type=str, help="The output CSV file")
parser.add_argument("-d", "--directory", type=str, help="List all the calendar or vcard files into the directory")

# Parse the command-line arguments
args = parser.parse_args()

if args.ics_file:
    if args.html_file:
        ics2html_vcf.ics2html(args.ics_file, args.html_file)
    elif args.csv_file:
        ics2html_vcf.ics2csv(args.ics_file, args.csv_file)
    else:
        ics2html_vcf.print_cal(args.ics_file)
elif args.vcf_file:
    if args.html_file:
        v2h.vcard2html(args.vcf_file, args.html_file)
    elif args.csv_file:
        v2csv.vcard2csv(args.vcf_file, args.csv_file)
    else:
        vcarComponent.print_vcard(args.vcf_file)
else:
    # Find all VCF and ICS files in the specified directory
    vcf_files = glob.glob(os.path.join(args.directory, "*.vcf"))
    ics_files = glob.glob(os.path.join(args.directory, "*.ics"))

    # Print the list of HTML and CSV files
    print("VCF files in {}:".format(args.directory))
    for file in vcf_files:
        print(" - {}".format(file))

    print("ICS files in {}:".format(args.directory))
    for file in ics_files:
        print(" - {}".format(file))
