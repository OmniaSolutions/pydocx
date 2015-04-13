# encoding: utf-8

"""
The :mod:`pptx.packaging` module coheres around the concerns of reading and
writing presentations to and from a .docx file.
"""



from __future__ import (
    absolute_import, division, print_function, unicode_literals
)
import uuid
from ..oxml.customprops import CT_CustomProperty,getPropValueFromValue

class PropertyValue(object):
    """
        get the property value elements
    """
    def __init__(self, element):
        self._element = element

    @property
    def value(self):
        """
            get the value
        """
        return self._element.text
    
    @value.setter
    def value(self,value):
        self._element.text=str(value)
    

class CustomProperty(object):
    """
        CustomProperties to part named ``/docProps/custom.xml``, containing custom properties
    """
    def __init__(self, element):
        self._element = element

    @property
    def fmtid(self):
        """
            get  the fmtid value
        """
        return self._element.get('fmtid')
    
    @fmtid.setter
    def fmtid(self,vFmtid):
        """
            set fmtid value
        """
        self._element.attrib['fmtid']=vFmtid
    
    @property
    def name(self):
        """
            get name
        """
        return self._element.get('name')
    
    @name.setter
    def name(self,vName):
        """
            set name
        """
        self._element.attrib['name']=vName
    
    @property
    def valueObj(self):
        """
            get value
        """
        for v in self._element.getchildren():
            return PropertyValue(v)
        return None
    
    @valueObj.setter
    def valueObj(self,value):
        """
            add value
        """
        for v in self._element.getchildren():
            vObj=PropertyValue(v)
            vObj.value=value
            return

    def newValueObj(self,value):
        #Create a new prop value
        newEle=getPropValueFromValue(value).new()
        pValue=PropertyValue(newEle)
        pValue.value=value
        # 
        self._element.append(pValue._element)
        return pValue
            
    @property
    def pid(self):
        """
            get pid 
        """
        return self._element.get('pid')
    
    @pid.setter
    def pid(self,vPid):
        """
            set pid value
        """
        self._element.attrib['pid']=str(vPid)
    
class CustomProperties(object):
    """
    CustomProperties to part named ``/docProps/custom.xml``, containing custom properties
    """
    def __init__(self, element):
        self._element = element

    
    @property
    def properties(self):
        """
            get the property objects
        """
        out=[]
        for element in self._element.getchildren():
            out.append(CustomProperty(element))
        return out
    
    @property
    def hash(self):
        """
            get the hash code for all the properties
        """
        fmtid=False
        for p in self.properties:
            fmtid=p.fmtid
            break
        if not fmtid:
            fmtid=uuid.uuid1()
        return fmtid
    @property
    def newPid(self):
        """
            create a new pid for a new property
        """
        return max([int(p.pid) for p in self.properties])+1
    
    def newProperties(self,name,value):
        """
            add a new properties
        """
        newProp=CustomProperty(CT_CustomProperty.new())
        newProp.fmtid=self.hash
        newProp.pid=self.newPid
        newProp.name=name
        newProp.newValueObj(value)
        self._element.append(newProp._element)
        return newProp


# <Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/custom-properties" 
#             xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">

#     <property fmtid="{D5CDD505-2E9C-101B-9397-08002B2CF9AE}" pid="2"  name="TMM_DOCUMENT">
#        <vt:lpwstr>DOCUT</vt:lpwstr></property>




    