from . import card

# path = "../../rsc/saber.vcf"


def write_fullname(path):
    html = '<span class="fn">' + card.fullname(path) + '</span>' + "\n"
    return html


# Returns a string of HTML with the contact's name.
def write_name(path):
    html = '<span class="n">' + "\n"
    htmli = html

    name = card.honorific_prefix(path)
    if name is not None:
        html += "\t" + '<span class="honorific-prefix">' + name + '</span>' + "\n"

    name = card.given_name(path)
    if name is not None:
        html += "\t" + '<span class="given-name">' + name + '</span>' + "\n"

    name = card.additional_name(path)
    if name is not None:
        html += "\t" + '<span class="additional-name">' + name + '</span>' + "\n"

    name = card.family_name(path)
    if name is not None:
        html += "\t" + '<span class="family-name">' + name + '</span>' + "\n"

    name = card.honorific_suffix(path)
    if name is not None:
        html += "\t" + '<span class="honorific-suffix">' + name + '</span>' + "\n"

    if html == htmli:
        return ''
    else:
        html += '</span>' + "\n"
        return html


# Returns a string of HTML with the contact's phone numbers.
def write_telephone(path):
    ltel = card.tel(path)

    if not ltel:
        return ''

    html = '<div class="telephones">' + "\n"
    for tel in ltel:
        html += "\t" '<div class="tel">' + tel + '</div>' + "\n"

    html += '</div>' + "\n"
    return html


def write_photos(path):
    li = card.photo(path)

    if not li:
        return ''

    html = "\t"  '<div class="photos">' + "\n"
    for photo in li:
        html += '<div class="photo">' + photo + '</div>' + "\n"

    html += '</div>' + "\n"
    return html


def write_email(path):
    li = card.email(path)

    if not li:
        return ''

    html = '<div class="emails">' + "\n"
    for email in li:
        html += "\t"  '<span><a class="email" href="mailto:' + email + '">' + email + '</a></span>' + "\n"

    html += '</div>' + "\n"
    return html


def write_url(path):
    li = card.urls(path)

    if not li:
        return ''

    html = '<div class="urls">' + "\n"
    for url in li:
        html += "\t"  '<span><a class="url" href="' + url + '">' + url + '</a></span>' + "\n"

    html += '</div>' + "\n"
    return html


def vcard2html(input_path, output_path):
    # Create the HTML markup
    html = "<html>\n<head>\n<link rel='stylesheet' href='../rsc/style.css'>\n</head>\n<body>\n<div class='vcard'>\n"
    html += write_fullname(input_path)
    html += write_name(input_path)
    html += write_email(input_path)
    html += write_url(input_path)
    html += write_telephone(input_path)
    html += write_photos(input_path)
    html += '</div>\n</body>\n</html>'

    # Save the HTML file
    with open(output_path, "w") as f:
        f.write(html)


#vcard2html("../../rsc/saber.vcf", "../../rsc/saber.html")
