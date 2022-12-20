#!/usr/bin/env python

import logging
import collections
import vobject

# listes des champs les plus importants
column_order = [
    'Name',
    'Full name',
    'ORG',
    'Cell phone',
    'Work phone',
    'Home phone',
    'Email',
    'Note',
]


def get_phone_numbers(vCard):
    """
    récupère les numéros de tel et les stock dans une liste
    :param vCard: un object vcard
    :return: liste de numéros de tel
    """
    cell = home = work = None
    for tel in vCard.tel_list:
        if vCard.version.value == '2.1':
            if 'CELL' in tel.singletonparams:
                cell = str(tel.value).strip()
            elif 'WORK' in tel.singletonparams:
                work = str(tel.value).strip()
            elif 'HOME' in tel.singletonparams:
                home = str(tel.value).strip()
            else:
                logging.warning("Warning: Unrecognized phone number category in `{}'".format(vCard))
                tel.prettyPrint()
        elif vCard.version.value == '3.0':
            if 'CELL' in tel.params['TYPE']:
                cell = str(tel.value).strip()
            elif 'WORK' in tel.params['TYPE']:
                work = str(tel.value).strip()
            elif 'HOME' in tel.params['TYPE']:
                home = str(tel.value).strip()
            else:
                logging.warning("Unrecognized phone number category in `{}'".format(vCard))
                tel.prettyPrint()
        else:
            raise NotImplementedError("Version not implemented: {}".format(vCard.version.value))
    return cell, home, work


def get_info_list(vCard, vcard_filepath):
    """

    :param vCard: l'object vcard
    :param vcard_filepath: chemin vers le fichier de la vcard
    :return: vcard
    """
    vcard = collections.OrderedDict()
    for column in column_order:
        vcard[column] = None
    name = cell = work = home = email = note = None
    vCard.validate()
    for key, val in list(vCard.contents.items()):
        if key == 'fn':
            vcard['Full name'] = vCard.fn.value
        elif key == 'n':
            name = str(vCard.n.valueRepr()).replace('  ', ' ').strip()
            vcard['Name'] = name
        elif key == 'org':
            org = str(vCard.org.value).replace('[', '').replace(']', '').replace("'", '')
            vcard['ORG'] = org
        elif key == 'tel':
            cell, home, work = get_phone_numbers(vCard)
            vcard['Cell phone'] = cell
            vcard['Home phone'] = home
            vcard['Work phone'] = work
        elif key == 'email':
            email = str(vCard.email.value).strip()
            vcard['Email'] = email
        elif key == 'note':
            note = str(vCard.note.value)
            vcard['Note'] = note
        else:
            # An unused key, like `adr`, `title`, `url`, etc.
            pass
    if name is None:
        logging.warning("no name for vCard in file `{}'".format(vcard_filepath))
    if all(telephone_number is None for telephone_number in [cell, work, home]):
        logging.warning("no telephone numbers for file `{}' with name `{}'".format(vcard_filepath, name))

    return vcard


def print_vcard(path):
    """
    Print the vcard to the terminal
    :param path:
    """
    s = open(path, 'r')
    v = vobject.readOne(s)
    odc = get_info_list(v, path)
    content = ''
    for key, value in odc.items():
        content = content + str(key) + ':\t' + str(value) + '\n'

    print(content)