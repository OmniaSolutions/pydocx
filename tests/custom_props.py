##############################################################################
#
#    OmniaSolutions, Your own solutions
#    Copyright (C) 13/apr/2015 OmniaSolutions (<http://www.omniasolutions.eu>). All Rights Reserved
#    info@omniasolutions.eu
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
'''
Created on 13/apr/2015

@author: mboscolo
'''
from docx import Document

if __name__ == '__main__':

    d=Document(r'D:\d\OmniaSolutions\Clienti\inarca\cross reference\ut057_2015_0.docx')
    p=d.core_properties
    for p in d.custom_properties.properties:
        if p.name=='DOCCOMMESSA':
            print "Value of the tmm_document",p.valueObj.value
            p.valueObj.value="arime ..."
    d.save(r'D:\d\OmniaSolutions\Clienti\inarca\cross reference\new_ut057_2015_0.docx')
    d.custom_properties.newProperties('Matteo',10)
    d.custom_properties.newProperties('Matteo1','111')
    d.custom_properties.newProperties('Matteo2',111.00)
    for p in d.custom_properties.properties:
        print "--",p.name,p.valueObj.value
    
    d.save(r'D:\d\OmniaSolutions\Clienti\inarca\cross reference\new_pROP_ut057_2015_0.docx')
    pass