# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.models.plan import Plan  # noqa: E501
from swagger_server.models.subscription import Subscription  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_createcompany(self):
        """Test case for createcompany

        Create a company
        """
        body = Company()
        response = self.client.open(
            '/companies',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_createplan(self):
        """Test case for createplan

        Create a plan
        """
        body = Plan()
        response = self.client.open(
            '/plans',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_createsubscription(self):
        """Test case for createsubscription

        Create a subscription
        """
        body = Subscription()
        response = self.client.open(
            '/companies/{companyId}/subscriptions'.format(companyId='companyId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deletecompany(self):
        """Test case for deletecompany

        Delete a company
        """
        response = self.client.open(
            '/companies/{companyId}'.format(companyId='companyId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deleteplan(self):
        """Test case for deleteplan

        Delete a plan
        """
        response = self.client.open(
            '/plans/{planId}'.format(planId='planId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deletesubscription(self):
        """Test case for deletesubscription

        Delete a subscription
        """
        response = self.client.open(
            '/companies/{companyId}/subscriptions/{subscriptionId}'.format(companyId='companyId_example', subscriptionId='subscriptionId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getcompanies(self):
        """Test case for getcompanies

        List All companies
        """
        response = self.client.open(
            '/companies',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getcompany(self):
        """Test case for getcompany

        Get a company
        """
        response = self.client.open(
            '/companies/{companyId}'.format(companyId='companyId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getplan(self):
        """Test case for getplan

        Get a plan
        """
        response = self.client.open(
            '/plans/{planId}'.format(planId='planId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getplans(self):
        """Test case for getplans

        List All plans
        """
        response = self.client.open(
            '/plans',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getsubscription(self):
        """Test case for getsubscription

        Get a subscription
        """
        response = self.client.open(
            '/companies/{companyId}/subscriptions/{subscriptionId}'.format(companyId='companyId_example', subscriptionId='subscriptionId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getsubscriptions(self):
        """Test case for getsubscriptions

        List All subscriptions
        """
        response = self.client.open(
            '/companies/{companyId}/subscriptions'.format(companyId='companyId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updatecompany(self):
        """Test case for updatecompany

        Update a company
        """
        body = Company()
        response = self.client.open(
            '/companies/{companyId}'.format(companyId='companyId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updateplan(self):
        """Test case for updateplan

        Update a plan
        """
        body = Plan()
        response = self.client.open(
            '/plans/{planId}'.format(planId='planId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updatesubscription(self):
        """Test case for updatesubscription

        Update a subscription
        """
        body = Subscription()
        response = self.client.open(
            '/companies/{companyId}/subscriptions/{subscriptionId}'.format(companyId='companyId_example', subscriptionId='subscriptionId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
