# encoding: utf-8

"""
lxml custom element classes for core properties-related XML elements.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from . import parse_xml
from .ns import nsdecls
from .xmlchemy import BaseOxmlElement



class CT_intValue(BaseOxmlElement):
    """
        ``<vt:i4>``
    """
    _int_tmpl = (
        '<vt:i4 %s/>\n' % nsdecls('vt')
    )    
    @classmethod
    def new(cls):
        """
        Return a new ``<property>`` element
        """
        xml = cls._int_tmpl
        intValue = parse_xml(xml)
        return intValue
    
class CT_strValue(BaseOxmlElement):
    """
        ``<vt:lpwstr>``
    """
    _str_tmpl = (
        '<vt:lpwstr %s/>\n' % nsdecls('vt')
    )    
    @classmethod
    def new(cls):
        """
        Return a new ``<property>`` element
        """
        xml = cls._str_tmpl
        strValue = parse_xml(xml)
        return strValue    

def getPropValueFromValue(value):
    """
        return the proper template from the value searched
    """
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    
    if is_number(value):
        if is_int(value):
            return CT_intValue
    return CT_strValue
    
    
class CT_CustomProperty(BaseOxmlElement):
    """
    ``<properties>``
    """

    _property_tmpl = (
        '<property />\n'
    )

    @classmethod
    def new(cls):
        """
        Return a new ``<property>`` element
        """
        xml = cls._property_tmpl
        property = parse_xml(xml)
        return property

    def _get_or_add(self, prop_name):
        """
        Return element returned by 'get_or_add_' method for *prop_name*.
        """
        get_or_add_method_name = 'get_or_add_%s' % prop_name
        get_or_add_method = getattr(self, get_or_add_method_name)
        element = get_or_add_method()
        return element  
      
class CT_CustomProperties(BaseOxmlElement):
    """
    ``<properties>`` element, the root element of the Core Properties
    part stored as ``/docProps/custom.xml``. Implements many of the Dublin Core
    document metadata elements. String elements resolve to an empty string
    ('') if the element is not present in the XML. String elements are
    limited in length to 255 unicode characters.
    """

    _customProperties_tmpl = (
        '<Properties %s/>\n' % nsdecls('vt')
    )

    @classmethod
    def new(cls):
        """
        Return a new ``<properties>`` element
        """
        xml = cls._customProperties_tmpl
        coreProperties = parse_xml(xml)
        return coreProperties

    def _get_or_add(self, prop_name):
        """
        Return element returned by 'get_or_add_' method for *prop_name*.
        """
        get_or_add_method_name = 'get_or_add_%s' % prop_name
        get_or_add_method = getattr(self, get_or_add_method_name)
        element = get_or_add_method()
        return element

    def _text_of_element(self, property_name):
        """
        Return the text in the element matching *property_name*, or an empty
        string if the element is not present or contains no text.
        """
        element = getattr(self, property_name)
        if element is None:
            return ''
        if element.text is None:
            return ''
        return element.text
    
