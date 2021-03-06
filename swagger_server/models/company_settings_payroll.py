# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CompanySettingsPayroll(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, pay_freq: str=None, pay_cycle_start_day: date=None, next_pay_day: date=None, max_travel_time_minutes: int=None, travel_time_calculation_method: str=None, payroll_calculation_method: str=None):  # noqa: E501
        """CompanySettingsPayroll - a model defined in Swagger

        :param pay_freq: The pay_freq of this CompanySettingsPayroll.  # noqa: E501
        :type pay_freq: str
        :param pay_cycle_start_day: The pay_cycle_start_day of this CompanySettingsPayroll.  # noqa: E501
        :type pay_cycle_start_day: date
        :param next_pay_day: The next_pay_day of this CompanySettingsPayroll.  # noqa: E501
        :type next_pay_day: date
        :param max_travel_time_minutes: The max_travel_time_minutes of this CompanySettingsPayroll.  # noqa: E501
        :type max_travel_time_minutes: int
        :param travel_time_calculation_method: The travel_time_calculation_method of this CompanySettingsPayroll.  # noqa: E501
        :type travel_time_calculation_method: str
        :param payroll_calculation_method: The payroll_calculation_method of this CompanySettingsPayroll.  # noqa: E501
        :type payroll_calculation_method: str
        """
        self.swagger_types = {
            'pay_freq': str,
            'pay_cycle_start_day': date,
            'next_pay_day': date,
            'max_travel_time_minutes': int,
            'travel_time_calculation_method': str,
            'payroll_calculation_method': str
        }

        self.attribute_map = {
            'pay_freq': 'payFreq',
            'pay_cycle_start_day': 'payCycleStartDay',
            'next_pay_day': 'nextPayDay',
            'max_travel_time_minutes': 'maxTravelTimeMinutes',
            'travel_time_calculation_method': 'travelTimeCalculationMethod',
            'payroll_calculation_method': 'payrollCalculationMethod'
        }

        self._pay_freq = pay_freq
        self._pay_cycle_start_day = pay_cycle_start_day
        self._next_pay_day = next_pay_day
        self._max_travel_time_minutes = max_travel_time_minutes
        self._travel_time_calculation_method = travel_time_calculation_method
        self._payroll_calculation_method = payroll_calculation_method

    @classmethod
    def from_dict(cls, dikt) -> 'CompanySettingsPayroll':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The company_settings_payroll of this CompanySettingsPayroll.  # noqa: E501
        :rtype: CompanySettingsPayroll
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pay_freq(self) -> str:
        """Gets the pay_freq of this CompanySettingsPayroll.


        :return: The pay_freq of this CompanySettingsPayroll.
        :rtype: str
        """
        return self._pay_freq

    @pay_freq.setter
    def pay_freq(self, pay_freq: str):
        """Sets the pay_freq of this CompanySettingsPayroll.


        :param pay_freq: The pay_freq of this CompanySettingsPayroll.
        :type pay_freq: str
        """

        self._pay_freq = pay_freq

    @property
    def pay_cycle_start_day(self) -> date:
        """Gets the pay_cycle_start_day of this CompanySettingsPayroll.


        :return: The pay_cycle_start_day of this CompanySettingsPayroll.
        :rtype: date
        """
        return self._pay_cycle_start_day

    @pay_cycle_start_day.setter
    def pay_cycle_start_day(self, pay_cycle_start_day: date):
        """Sets the pay_cycle_start_day of this CompanySettingsPayroll.


        :param pay_cycle_start_day: The pay_cycle_start_day of this CompanySettingsPayroll.
        :type pay_cycle_start_day: date
        """

        self._pay_cycle_start_day = pay_cycle_start_day

    @property
    def next_pay_day(self) -> date:
        """Gets the next_pay_day of this CompanySettingsPayroll.


        :return: The next_pay_day of this CompanySettingsPayroll.
        :rtype: date
        """
        return self._next_pay_day

    @next_pay_day.setter
    def next_pay_day(self, next_pay_day: date):
        """Sets the next_pay_day of this CompanySettingsPayroll.


        :param next_pay_day: The next_pay_day of this CompanySettingsPayroll.
        :type next_pay_day: date
        """

        self._next_pay_day = next_pay_day

    @property
    def max_travel_time_minutes(self) -> int:
        """Gets the max_travel_time_minutes of this CompanySettingsPayroll.


        :return: The max_travel_time_minutes of this CompanySettingsPayroll.
        :rtype: int
        """
        return self._max_travel_time_minutes

    @max_travel_time_minutes.setter
    def max_travel_time_minutes(self, max_travel_time_minutes: int):
        """Sets the max_travel_time_minutes of this CompanySettingsPayroll.


        :param max_travel_time_minutes: The max_travel_time_minutes of this CompanySettingsPayroll.
        :type max_travel_time_minutes: int
        """

        self._max_travel_time_minutes = max_travel_time_minutes

    @property
    def travel_time_calculation_method(self) -> str:
        """Gets the travel_time_calculation_method of this CompanySettingsPayroll.


        :return: The travel_time_calculation_method of this CompanySettingsPayroll.
        :rtype: str
        """
        return self._travel_time_calculation_method

    @travel_time_calculation_method.setter
    def travel_time_calculation_method(self, travel_time_calculation_method: str):
        """Sets the travel_time_calculation_method of this CompanySettingsPayroll.


        :param travel_time_calculation_method: The travel_time_calculation_method of this CompanySettingsPayroll.
        :type travel_time_calculation_method: str
        """

        self._travel_time_calculation_method = travel_time_calculation_method

    @property
    def payroll_calculation_method(self) -> str:
        """Gets the payroll_calculation_method of this CompanySettingsPayroll.


        :return: The payroll_calculation_method of this CompanySettingsPayroll.
        :rtype: str
        """
        return self._payroll_calculation_method

    @payroll_calculation_method.setter
    def payroll_calculation_method(self, payroll_calculation_method: str):
        """Sets the payroll_calculation_method of this CompanySettingsPayroll.


        :param payroll_calculation_method: The payroll_calculation_method of this CompanySettingsPayroll.
        :type payroll_calculation_method: str
        """

        self._payroll_calculation_method = payroll_calculation_method
