# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.errorunknown import ERRORUNKNOWN  # noqa: F401,E501
from swagger_server import util


class CompanySettingsPhone(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, primary: List[ERRORUNKNOWN]=None, client_support: List[ERRORUNKNOWN]=None):  # noqa: E501
        """CompanySettingsPhone - a model defined in Swagger

        :param primary: The primary of this CompanySettingsPhone.  # noqa: E501
        :type primary: List[ERRORUNKNOWN]
        :param client_support: The client_support of this CompanySettingsPhone.  # noqa: E501
        :type client_support: List[ERRORUNKNOWN]
        """
        self.swagger_types = {
            'primary': List[ERRORUNKNOWN],
            'client_support': List[ERRORUNKNOWN]
        }

        self.attribute_map = {
            'primary': 'primary',
            'client_support': 'clientSupport'
        }

        self._primary = primary
        self._client_support = client_support

    @classmethod
    def from_dict(cls, dikt) -> 'CompanySettingsPhone':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The company_settings_phone of this CompanySettingsPhone.  # noqa: E501
        :rtype: CompanySettingsPhone
        """
        return util.deserialize_model(dikt, cls)

    @property
    def primary(self) -> List[ERRORUNKNOWN]:
        """Gets the primary of this CompanySettingsPhone.


        :return: The primary of this CompanySettingsPhone.
        :rtype: List[ERRORUNKNOWN]
        """
        return self._primary

    @primary.setter
    def primary(self, primary: List[ERRORUNKNOWN]):
        """Sets the primary of this CompanySettingsPhone.


        :param primary: The primary of this CompanySettingsPhone.
        :type primary: List[ERRORUNKNOWN]
        """

        self._primary = primary

    @property
    def client_support(self) -> List[ERRORUNKNOWN]:
        """Gets the client_support of this CompanySettingsPhone.


        :return: The client_support of this CompanySettingsPhone.
        :rtype: List[ERRORUNKNOWN]
        """
        return self._client_support

    @client_support.setter
    def client_support(self, client_support: List[ERRORUNKNOWN]):
        """Sets the client_support of this CompanySettingsPhone.


        :param client_support: The client_support of this CompanySettingsPhone.
        :type client_support: List[ERRORUNKNOWN]
        """

        self._client_support = client_support
