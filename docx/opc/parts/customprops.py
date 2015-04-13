# encoding: utf-8

"""
Core properties part, corresponds to ``/docProps/core.xml`` part in package.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from datetime import datetime

from ..constants import CONTENT_TYPE as CT

from ..customprops import CustomProperties
from ...oxml.customprops import CT_CustomProperties
from ..packuri import PackURI
from ..part import XmlPart


class CustomPropertiesPart(XmlPart):
    """
    Corresponds to part named ``/docProps/core.xml``, containing the core
    document properties for this document package.
    """
    @classmethod
    def default(cls, package):
        """
        Return a new |CustomPropertiesPart| object initialized with default
        values for its base properties.
        """
        custom_properties_part = cls._new(package)
        custom_properties = custom_properties_part.custom_properties
        return custom_properties 

    @property
    def custom_properties(self):
        """
        A |Custom Properties| object providing read/write access to the custom
        properties contained in this core properties part.
        """
        return CustomProperties(self.element)

    @classmethod
    def _new(cls, package):
        partname = PackURI('/docProps/core.xml')
        content_type = CT.OPC_CUSTOM_PROPERTIES
        coreProperties = CT_CustomProperties.new()
        return CustomPropertiesPart(
            partname, content_type, coreProperties, package
        )
