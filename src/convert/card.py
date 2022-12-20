import vobject


def name(path):
    """
    fonction qui retourne le nom se trouvent dans une vcard
    :param path: chemin d'acces au fichier
    :return: le nom
    """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            data = vcard.contents["n"][0].value
        except KeyError:
            data = None
        finally:
            return data


def fullname(path):
    """
       fonction qui retourne le nom se trouvent dans une vcard
       :param path: chemin d'acces au fichier
       :return: le nom complet
       """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            data = vcard.contents["fn"][0].value
        except KeyError:
            data = None
        finally:
            return data


def honorific_prefix(path):
    """
       fonction qui retourne le nom se trouvent dans une vcard
       :param path: chemin d'acces au fichier
       :return: le nom d'honneur
       """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            data = vcard.contents["honorific-prefix"][0].value
        except KeyError:
            data = None
        finally:
            return data


def given_name(path):
    """
       fonction qui retourne le nom se trouvent dans une vcard
       :param path: chemin d'acces au fichier
       :return: le nom donné
       """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            data = vcard.contents["given-name"][0].value
        except KeyError:
            data = None
        finally:
            return data


def additional_name(path):
    """
       fonction qui retourne le nom se trouvent dans une vcard
       :param path: chemin d'acces au fichier
       :return: le nom additionel
       """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            data = vcard.contents["additional-name"][0].value
        except KeyError:
            data = None
        finally:
            return data


def family_name(path):
    """
       fonction qui retourne le nom se trouvent dans une vcard
       :param path: chemin d'acces au fichier
       :return: le nom de famille
       """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            data = vcard.contents["family-name"][0].value
        except KeyError:
            data = None
        finally:
            return data


def honorific_suffix(path):
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            data = vcard.contents["honorific-suffix"][0].value
        except KeyError:
            data = None
        finally:
            return data


def tel(path):
    """
       fonction qui retourne ls numéros de telephones qui se trouvent dans une vcard
       :param path: chemin d'acces au fichier
       :return: liste des numéros de tel
       """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            li = []
            for data in vcard.contents["tel"]:
                li.append(data.value)
        finally:
            return li


def photo(path):
    """
       fonction qui retourne lea photo se trouvent dans une vcard
       :param path: chemin d'acces au fichier
       :return: photo
       """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            li = []
            for data in vcard.contents["photo"]:
                li.append(data.value)
        finally:
            return li


def email(path):
    """fonction qui retourne les e-mails qui se trouvent dans une vcard
       :param path: chemin d'acces au fichier
       :return: liste qui contient tous les e-mails de la vcard """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            li = []
            for data in vcard.contents["email"]:
                li.append(data.value)
        finally:
            return li


def urls(path):
    """fonction qui retourne les urlsqui se trouvent dans une vcard
           :param path: chemin d'acces au fichier
           :return: liste qui contient tous les urls de la vcard """
    with open(path, 'r') as f:
        try:
            vcard: vobject.vCard = vobject.readOne(f.read())
            li = []
            for data in vcard.contents["url"]:
                li.append(data.value)
        finally:
            return li

