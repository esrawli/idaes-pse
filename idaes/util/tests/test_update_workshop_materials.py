##############################################################################
# Institute for the Design of Advanced Energy Systems Process Systems
# Engineering Framework (IDAES PSE Framework) Copyright (c) 2018-2020, by the
# software owners: The Regents of the University of California, through
# Lawrence Berkeley National Laboratory,  National Technology & Engineering
# Solutions of Sandia, LLC, Carnegie Mellon University, West Virginia
# University Research Corporation, et al. All rights reserved.
#
# Please see the files COPYRIGHT.txt and LICENSE.txt for full copyright and
# license information, respectively. Both files are also available online
# at the URL "https://github.com/IDAES/idaes-pse".
##############################################################################

"""
Tests for update_workshop_materials
"""
import idaes.util.update_workshop_materials as up
import pytest

@pytest.mark.unit
def test_update_workshop_materials():
    # Note: This tests that the methods in update_workshop_materials.py
    # successfully download install_idaes_workshop_materials.py from Pyomo.org
    # We purposely do NOT test code within that downloaded module since we do
    # not want to automatically execute code during testing that was downloaded
    # from outside the IDAES repository.
    
    # download the module from pyomo.org
    download_dest = up.download_install_module()

    # check that the file contains the desired function (execute())
    download_succeeded = False
    with open(download_dest, 'r') as fd:
        for line in fd:
            if line.startswith('def execute():'):
                download_succeeded = True
                break

    assert download_succeeded == True

if __name__ == '__main__':
    test_update_workshop_materials()
    
