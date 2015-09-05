'''
Description:

Inputs:

Outputs:

Currently:

To Do:

Done:
'''
'''
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
'''

import os, sys, shutil

def check_file_exist(path):
    if os.path.exists(path):
        print path, 'exists!'
    else:
        sys.exit('File {} doesn\'t exist'.format(path))
    return None

def grab_out_paths(num_apps):
    out_dir = '..\\apps\\web_apps\\linux\\{pat}'
    project_part = 'P{}'
    out_paths = []
    for num in range(1, num_apps + 1):
        strin = project_part.format(str(num))
        out_paths.append(out_dir.format(pat=strin))
    return out_paths

def grab_web2py_frame():
    webframe = '..\\apps\\scaffolding\\linux\\web2py'
    webdotpy = '..\\apps\\scaffolding\\common\\web2py.py'
    check_file_exist(webdotpy)
    check_file_exist(webframe)
    return webframe, webdotpy

def grab_scaffold_app(version):
    mkever = '..\\apps\\scaffolding\\version\\MKE_v{}'.format(version)
    check_file_exist(mkever)
    return mkever

def copy_webframez(num_apps):
    webframe, webdotpy = grab_web2py_frame()
    out_paths = grab_out_paths(num_apps)
    for path in out_paths:
        shutil.copytree(webframe, os.path.join(path, 'web2py'))
        next_path = os.path.join(path, 'web2py')
        shutil.copy(webdotpy, next_path)
        print 'web2py frame copied to: {}'.format(path)
        print 'web2py.py copied to: {}'.format(next_path)
    return out_paths

def modify_out_paths(int_paths):
    mod_out = []
    addition = 'web2py\\applications'
    for path in int_paths:
        new_path = os.path.join(path, addition)
        mod_out.append(new_path)
    return mod_out

def grab_filename_from_path(in_path):
    '''Input a path, return last chunck'''
    import ntpath
    head, tail = ntpath.split(in_path)
    return tail or ntpath.basename(head)

#def create_bat(out_path, num):
#    mkebat = '..\\apps\\scaffolding\\common\\MKE_PT_.bat'
#    check_file_exist(mkebat)
#    shutil.copy(mkebat, out_path)
#    old_name = os.path.join(out_path, 'MKE_PT_.bat')
#    exe_name = 'MKE_PT_{}.bat'.format(num)
#    new_name = os.path.join(out_path, exe_name)
#    print old_name, new_name
#    os.rename(old_name, new_name)
#    return None

#def rename_exe(path, num):
#    old_name = os.path.join(path, 'web2py.exe')
#    exe_name = 'MKE_PT_{}.exe'.format(num)
#    new_name = os.path.join(path, exe_name)
#    print old_name, new_name
#    os.rename(old_name, new_name)
#    return None

def modify_webframez(out_paths, num_apps):
    assert len(out_paths) == int(num_apps)
    num = 1
    for path in out_paths:
        new_path = os.path.join(path, 'web2py')
        create_bat(new_path, num)
        num += 1
    return None

def copy_app(version, out_paths):
    scaff_app = grab_scaffold_app(version)
    filename = grab_filename_from_path(scaff_app)
    for path in out_paths:
        shutil.copytree(scaff_app, os.path.join(path, filename))
        old_name = os.path.join(path, filename)
        new_name = os.path.join(path, 'MKE_Static_Name')
        os.rename(old_name, new_name)
    return None

def deploy_scaffolding(version, num_apps):
    out_paths = copy_webframez(num_apps)
#    modify_webframez(out_paths, num_apps)
    new_paths = modify_out_paths(out_paths)
    copy_app(version, new_paths)
    return None

if __name__ == "__main__":
    num_apps = 10
    version = '00_01_02'
    deploy_scaffolding(version, num_apps)