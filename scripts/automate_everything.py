'''
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
    Does it all! (more descriptive description later)

Inputs:
    All the scripts!
    Version number of current scaffolding_app
    Images in '../images/raw_tiff'
    OS Versions of web2py framework in '../scaffolidng'

Outputs:
    All the things!
    All populated web_apps.
    The final project output, for Linux, Mac, and Windows.
    Updates README

Currently:
    Rewriting scripts to avoid errors while calling from
        different directories.

To Do:
    Rewrite Description, Inputs, and Outputs.
    Create version_search, which determines most up to date version.

Done:
'''

import reset_system
import create_web_apps_win
import create_web_apps_mac
import create_web_apps_linux
import image_path_chunk_grabber as impcg
import populate_web_app as popu
import process_images
import the_decider as t_d
import view_change as v_c
import update_readme

import os

def discover_how_many_tifs(tif_dir):
    """Discovers how many tiffs are intended to be processed."""
    dir_list = os.listdir(t_d.resolve_relative_path(__file__, tif_dir))
    number_images_to_process = len(dir_list)
    return number_images_to_process

def prepare_png_images(adict):
    """
    Processes raw tiff images, creates png images for web_apps.
    Creates data for web_app database population.
    Decides how png images will be distributed between a number of apps.
    """
    total_image_num = discover_how_many_tifs(adict["tif_path"])
    process_images.in_summary(adict)
    how_many_apps, images_per_app = t_d.the_decider(total_image_num, adict)
    return how_many_apps, images_per_app

def create_web_app_population(adict, how_many_apps, images_per_app):
    """
    Creates web_apps for Linux, Windows, and Mac. (from scaffolding)
    Populates web_apps with png images and corresponding data.
    """
    version_app = adict["version"]
    os_list = ['win', 'mac', 'linux']
    create_web_apps_win.deploy_scaffolding(version_app, how_many_apps)
    create_web_apps_mac.deploy_scaffolding(version_app, how_many_apps)
    create_web_apps_linux.deploy_scaffolding(version_app, how_many_apps)
    proc_path = adict["out_path"]
    dict_image_p = impcg.image_path_chunk_grabber(images_per_app, proc_path)
    for w_os in os_list:
        for number in range(len(dict_image_p.keys())):
            part = "P{}".format(number+1)
            popu.populate_web_app(part, dict_image_p[part], w_os, adict)
            v_c.replace_view(part, dict_image_p[part][0], w_os)
    return None

def final(adict):
    """
    Runs everything. Updates README.txt

    adict - the automation dictionary
        keys:
            version - the current project version
            generated_dirs - a dictionaries containing the directories
                                 produced by `automate_everything.py`
            tif_path - relative path to raw_tif files
    """
    reset_system.delete_directories(adict["generated_dirs"])
    how_many_apps, images_per_app = prepare_png_images(adict)
    create_web_app_population(adict, how_many_apps, images_per_app)
    print "\n    Finished, now updating readme...\n"
    curr_dir = os.path.dirname(t_d.resolve_relative_path(__file__, "scripts"))
    update_readme.update_readme(curr_dir)
    return None

if __name__ == "__main__":
    DIR_DICT = {"web_apps":"../apps/web_apps",
                "images_processed":"../images/processed_images",
                "populators":"./populators"}

    AUTO_DICT = {"version":"00_01_02",
                 "generated_dirs":DIR_DICT,
                 "tif_path":"../images/raw_tiff",
                 "out_path":"../images/processed_images",
                 "image_name_form":"M2JT{}",
                 "meta_path":"../data",
                 "pop_path":"./populators/{}_populator.py"}
    final(AUTO_DICT)
