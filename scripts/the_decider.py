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
    Decide how many web_apps to make,
        and how many images should be in each.
Inputs:
    Dictionaries in '../data',
        {md5:size}

Outputs:
    how_many_apps
    images_per_app

Currently:
    Add support for prime numbers of images.
        Prime numbers of images might create an infinite loop...

To Do:

Done:
    Take average image size.
    Decide how many average images could fit inside a 800Mb application.
    Decide how many applications will be nessecary to contain all
        images based on how many images_per_app.
'''

import os, math

def grab_png_data():
    path = '../data/png_sizes.txt'
    with open(path, 'r') as dict_file:
        dictionary = eval(dict_file.read())
        return dictionary

def take_average(dictionary):
    md5s = dictionary.keys()
    total, count = 0, 0
    for md5 in md5s:
        count += 1
        total += dictionary[md5]
    average = total / count
    return average

def how_many_images_fit(average, total_image_num):
    eighthundomb = 800 * (10 ** 6)
    average_fit = eighthundomb // average
    images_per_app = average_fit
    for nothing in range(images_per_app, images_per_app / 2, -1):
        images_per_app -= 1
        if total_image_num % images_per_app == 0:
            break
    if images_per_app > total_image_num:
        images_per_app = total_image_num
    return images_per_app

def apps_number(images_per_app, total_image_num):
    how_many_apps = total_image_num // images_per_app
    if total_image_num % images_per_app != 0:
        how_many_apps += 1
    return how_many_apps

def the_decider(total_image_num):
    average = take_average(grab_png_data())
    images_per_app = how_many_images_fit(average, total_image_num)
    how_many_apps = apps_number(images_per_app, total_image_num)
    return how_many_apps, images_per_app

if __name__ == "__main__":
    total_image_num = 659
    how_many, images_per = the_decider(total_image_num)
    print 'How many apps: ', how_many, '\n', 'Images per app: ', images_per
