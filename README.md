# nbody_standard_code

1. Install packages to run C++ file nbody_sh1.C, and install pip
apt-get update && apt-get install -y --no-install-recommends \
        build-essential g++\ 
        python3-pip \
        gcc\ 

RUN if neccessary
pip3 install --upgrade pip 

Create nbody_sh1. Run 
g++ -o nbody_sh1 nbody_sh1.C


2. How to Create a new virtualenv (myenv) and install packages using pip

All neccessary dependencies and packages are included in requirements.txt

Create a new virtualenv (myenv) with python2 and
bin/virtualenv myenv
(bin/virtualenv -p python3 myenv)

Activate the environment using:
source myenv/bin/activate

Now install the packages according to requirements.txt from the local archive directory
Run (Python 2)
pip install -r requirements.txt  
(or python -m pip install -r /path/to/requirements.txt)

or (Python 3)
pip3 install -r requirements.txt 


3. How to use
First run main_with_total_change.py to Create data_in.txt, data_info.txt, data_out.txt, Report.pdf
We use Matplotlib and VPython to animate the movement of System in 2D and 3D.

a. main_with_total_change.py
In this file, we need to input information of Planets in the function createData.
This file will create a Folder, and this Folder includes all information of System.
If we want to visualize the System, we should run the following files.

b. main_animation_matplotlib_2D.py, main_animation_matplotlib_3D.py, main_animation_vpython2D.py, main_animation_vpython3D.py
In order to run these files, we need to copy data_in.txt in the created Folder above into these path.
