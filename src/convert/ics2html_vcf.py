# Import the necessary modules
from ics import Calendar
import html
import csv
import icalendar
from datetime import datetime
from prettytable import PrettyTable


def print_cal(path):
    """
    Ce code analysera le fichier ICS et extraira les événements qu'il contient. Il créera ensuite une table à l'aide
    du module "prettytable" et ajoutera les événements à la table.
    Enfin, il imprimera le tableau sur le terminal, indiquant les dates et heures de début et de fin, le lieu
    ainsi que le résumé de chaque événement
    :param path:
    :return:
    """
    # Read the ICS file
    with open(path, 'rb') as f:
        cal = icalendar.Calendar.from_ical(f.read())

    # Create a table to display the events
    table = PrettyTable()
    table.field_names = ['Start', 'End', 'Summary', 'Location', 'Description']

    # Add the events from the ICS file to the table
    for event in cal.walk('vevent'):
        start_date = event['dtstart'].dt
        end_date = event['dtend'].dt
        summary = event['summary']
        location = event['location']
        description = event['description']
        table.add_row([datetime.strftime(start_date, '%Y-%m-%d %H:%M:%S'),
                       datetime.strftime(end_date, '%Y-%m-%d %H:%M:%S'),
                       summary, location, description])

    # Print the table to the terminal
    print(table)


def ics2html(input_path, output_path):
    # Read the calendar file
    with open(input_path, "r") as f:
        calendar = Calendar(f.read())

    # Create the HTML markup
    html_output = "<html>\n<head>\n<link rel='stylesheet' " \
                  "href='../rsc/style.css'>\n</head>\n<body>\n<table>\n<thead>\n<tr>\n<th> EventName </th>\n<th> " \
                  "StartDateTime </th>\n<th> EndDateTime </th>\n<th> LocationName </th>\n<th> Description " \
                  "</th>\n</tr>\n</thead>\n<tbody>\n<tr> \n "
    for event in calendar.events:
        html_output += "<td>{}</td>\n".format(html.escape(event.name))
        html_output += "<td>{}</td>\n".format(html.escape(str(event.begin)))
        html_output += "<td>{}</td>\n".format(html.escape(str(event.end)))
        html_output += "<td>{}</td>\n".format(html.escape(event.location))
        html_output += "<td>{}</td>\n".format(html.escape(event.description))
    html_output += "</tr>\n</tbody>\n</table>\n</body>\n</html>"

    # Save the HTML file
    with open(output_path, "w") as f:
        f.write(html_output)


def ics2csv(input_path, output_path):
    # Read the calendar file
    with open(input_path, "r") as f:
        calendar = Calendar(f.read())

    # Create the CSV writer
    csv_file = open(output_path, "w")
    csv_writer = csv.writer(csv_file, delimiter=",")

    # Write the headers
    csv_writer.writerow(["Name", "Description", "Start Time", "End Time"])

    # Write the events
    for event in calendar.events:
        csv_writer.writerow([event.name, event.description, event.begin, event.end])

    # Close the CSV file
    csv_file.close()
