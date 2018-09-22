<<<<<<< HEAD

# Import the regex module
=======
>>>>>>> 715ebcce52c03695993bff7dc2eeafb7d4687a4e
import re


def parse_markdown(markdown):
<<<<<<< HEAD
    """Converts markdown text to plain html syntax. Returns a string."""

    lines = markdown.split('\n')
    html = ''  # We'll store our converted html here.
    in_list = False

    h6_regex = '###### (.*)'
    h2_regex = '## (.*)'
    h1_regex = '# (.*)'
    list_regex = r'\* (.*)'
    bold_regex = '(.*)__(.*)__(.*)'
    italic_regex = '(.*)_(.*)_(.*)'

    # iterate through each line looking for patterns. Remember we split our Markdown with '\n' delimiter
    for chunk in lines:
        # first we look for heading syntax

        if re.match(h6_regex, chunk) is not None:
            chunk = '<h6>' + chunk[7:] + '</h6>'

        elif re.match(h2_regex, chunk) is not None:
            chunk = '<h2>' + chunk[3:] + '</h2>'

        elif re.match(h1_regex, chunk) is not None:
            chunk = '<h1>' + chunk[2:] + '</h1>'

        unordered_list_items = re.match(r'\* (.*)', chunk)

        # we check for <ul> items here
        if unordered_list_items:

=======
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(r'\* (.*)', i)
        if m:
>>>>>>> 715ebcce52c03695993bff7dc2eeafb7d4687a4e
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
<<<<<<< HEAD

                # here we segregate the <li> items
                ordered_list_items = unordered_list_items.group(1)

                # to find 'bold' content
                bold_match = re.match(bold_regex, ordered_list_items)

                if bold_match:
                    ordered_list_items = bold_match.group(1) + '<strong>' + \
                        bold_match.group(2) + '</strong>' + bold_match.group(3)
                    is_bold = True

                # to find 'italic' content
                italic_match = re.match(italic_regex, ordered_list_items)

                if italic_match:
                    ordered_list_items = italic_match.group(1) + '<em>' + italic_match.group(2) + '</em>' + italic_match.group(3)
                    is_italic = True

                chunk = '<ul><li>' + ordered_list_items + '</li>'

            # this else section follows very identical construction as the 'if' section above.
            # Most of the code is repeating and doesn't follow the DRY principle.

            else:

                is_bold = False
                is_italic = False
                ordered_list_items = unordered_list_items.group(1)
                bold_match = re.match(bold_regex, ordered_list_items)

                if bold_match:
                    ordered_list_items = bold_match.group(1) + '<strong>' + bold_match.group(2) + '</strong>' + bold_match.group(3)
                    is_bold = True

                italic_match = re.match(italic_regex, ordered_list_items)
                if italic_match:
                    ordered_list_items = italic_match.group(1) + '<em>' + italic_match.group(2) + \
                        '</em>' + italic_match.group(3)

                    is_italic = True

                chunk = '<li>' + ordered_list_items + '</li>'

        else:
            if in_list:
                chunk += '</ul>'
                in_list = False

        paragraph_match = re.match('<h|<ul|<p|<li', chunk)

        if not paragraph_match:
            chunk = '<p>' + chunk + '</p>'

        bold_match = re.match(bold_regex, chunk)

        if bold_match:
            chunk = bold_match.group(1) + '<strong>' + bold_match.group(2) + '</strong>' + bold_match.group(3)

        italic_match = re.match(italic_regex, chunk)

        if italic_match:
            chunk = italic_match.group(1) + '<em>' + italic_match.group(2) + '</em>' + italic_match.group(3)

        html += chunk

    if in_list:
        html += '</ul>'

    return html
=======
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                i = '</ul>+i'
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        res += i
    if in_list:
        res += '</ul>'
    return res
>>>>>>> 715ebcce52c03695993bff7dc2eeafb7d4687a4e
