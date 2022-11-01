from pathlib import Path
import os
from routines import copy
from routines.copy import copy_file


def test_copy_file():
    copy_file('testfile', 'targetfile')
    txt = Path('targetfile').read_text()
    assert ("ahh" in txt)

    # Delete the targetfile
    os.remove('targetfile')