# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.errorunknown import ERRORUNKNOWN  # noqa: F401,E501
from swagger_server import util


class CompanyTwillio(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, public_survey: List[ERRORUNKNOWN]=None, ivr: List[ERRORUNKNOWN]=None):  # noqa: E501
        """CompanyTwillio - a model defined in Swagger

        :param public_survey: The public_survey of this CompanyTwillio.  # noqa: E501
        :type public_survey: List[ERRORUNKNOWN]
        :param ivr: The ivr of this CompanyTwillio.  # noqa: E501
        :type ivr: List[ERRORUNKNOWN]
        """
        self.swagger_types = {
            'public_survey': List[ERRORUNKNOWN],
            'ivr': List[ERRORUNKNOWN]
        }

        self.attribute_map = {
            'public_survey': 'publicSurvey',
            'ivr': 'ivr'
        }

        self._public_survey = public_survey
        self._ivr = ivr

    @classmethod
    def from_dict(cls, dikt) -> 'CompanyTwillio':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The company_twillio of this CompanyTwillio.  # noqa: E501
        :rtype: CompanyTwillio
        """
        return util.deserialize_model(dikt, cls)

    @property
    def public_survey(self) -> List[ERRORUNKNOWN]:
        """Gets the public_survey of this CompanyTwillio.


        :return: The public_survey of this CompanyTwillio.
        :rtype: List[ERRORUNKNOWN]
        """
        return self._public_survey

    @public_survey.setter
    def public_survey(self, public_survey: List[ERRORUNKNOWN]):
        """Sets the public_survey of this CompanyTwillio.


        :param public_survey: The public_survey of this CompanyTwillio.
        :type public_survey: List[ERRORUNKNOWN]
        """

        self._public_survey = public_survey

    @property
    def ivr(self) -> List[ERRORUNKNOWN]:
        """Gets the ivr of this CompanyTwillio.


        :return: The ivr of this CompanyTwillio.
        :rtype: List[ERRORUNKNOWN]
        """
        return self._ivr

    @ivr.setter
    def ivr(self, ivr: List[ERRORUNKNOWN]):
        """Sets the ivr of this CompanyTwillio.


        :param ivr: The ivr of this CompanyTwillio.
        :type ivr: List[ERRORUNKNOWN]
        """

        self._ivr = ivr
