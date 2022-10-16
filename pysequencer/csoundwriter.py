# Author:  Martin McBride
# Created: 2022-10-01
# Copyright (C) 2022, Martin McBride
# License: MIT

import pystache


def create_csd(fname, sequences):
    with open("../templates/template.csd", 'r') as infile:
        template = infile.read()

    score = "\n".join(map(str, sequences))

    csound_script = pystache.render(template, dict(score=score))

    with open(fname, 'w') as outfile:
        outfile.write(csound_script)
