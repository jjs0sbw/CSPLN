"""
<license>
CSPLN_MaryKeelerEdition; Manages images to which notes can be added.
Copyright (C) 2015, Thomas Kercheval

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
___________________________________________________________</license>

Description:
    Deletes all generated files.
    Resets the system for further testing.

Inputs:
    Generated files.

Outputs:
    Environment fresh for generation.

Currently:


To Do:

Done:
    Resets the system so `./automate_everything.py` may be run
"""

from shutil import rmtree
from os.path import exists
from the_decider import resolve_relative_path as resolve_path

def delete_directories(directory_dictionary):
    """Resets system so further files may be deleted."""
    print "\nResetting system...\n"
    directory_keys = directory_dictionary.keys()
    for directory in directory_keys:
        path = resolve_path(__file__, directory_dictionary[directory])
        print "Deleteing {}.".format(path)
        if exists(path):
            rmtree(path)
        else:
            print "    But it doesn't exist..."
    print "\nFinished resetting system...\n"
    return None

if __name__ == '__main__':
    GENERATED_DIRS = {"web_apps":"../apps/web_apps",
                      "images_processed":"../images/processed_images",
                      "populators":"./populators"}
    delete_directories(GENERATED_DIRS)
