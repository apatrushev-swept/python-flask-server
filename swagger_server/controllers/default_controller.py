import connexion
import six

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.models.plan import Plan  # noqa: E501
from swagger_server.models.subscription import Subscription  # noqa: E501
from swagger_server import util


def createcompany(body):  # noqa: E501
    """Create a company

    Creates a new instance of a &#x60;company&#x60;. # noqa: E501

    :param body: A new &#x60;company&#x60; to be created.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Company.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def createplan(body):  # noqa: E501
    """Create a plan

    Creates a new instance of a &#x60;plan&#x60;. # noqa: E501

    :param body: A new &#x60;plan&#x60; to be created.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Plan.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def createsubscription(companyId, body):  # noqa: E501
    """Create a subscription

    Creates a new instance of a &#x60;subscription&#x60;. # noqa: E501

    :param companyId: A unique identifier for a &#x60;company&#x60;.
    :type companyId: str
    :param body: A new &#x60;subscription&#x60; to be created.
    :type body: dict | bytes

    :rtype: Subscription
    """
    if connexion.request.is_json:
        body = Subscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def deletecompany(companyId):  # noqa: E501
    """Delete a company

    Deletes an existing &#x60;company&#x60;. # noqa: E501

    :param companyId: A unique identifier for a &#x60;company&#x60;.
    :type companyId: str

    :rtype: None
    """
    return 'do some magic!'


def deleteplan(planId):  # noqa: E501
    """Delete a plan

    Deletes an existing &#x60;plan&#x60;. # noqa: E501

    :param planId: A unique identifier for a &#x60;plan&#x60;.
    :type planId: str

    :rtype: None
    """
    return 'do some magic!'


def deletesubscription(companyId, subscriptionId):  # noqa: E501
    """Delete a subscription

    Deletes an existing &#x60;subscription&#x60;. # noqa: E501

    :param companyId: A unique identifier for a &#x60;company&#x60;.
    :type companyId: str
    :param subscriptionId: A unique identifier for a &#x60;subscription&#x60;.
    :type subscriptionId: str

    :rtype: None
    """
    return 'do some magic!'


def getcompanies():  # noqa: E501
    """List All companies

    Gets a list of all &#x60;company&#x60; entities. # noqa: E501


    :rtype: List[Company]
    """
    return 'do some magic!'


def getcompany(companyId):  # noqa: E501
    """Get a company

    Gets the details of a single instance of a &#x60;company&#x60;. # noqa: E501

    :param companyId: A unique identifier for a &#x60;company&#x60;.
    :type companyId: str

    :rtype: Company
    """
    return 'do some magic!'


def getplan(planId):  # noqa: E501
    """Get a plan

    Gets the details of a single instance of a &#x60;plan&#x60;. # noqa: E501

    :param planId: A unique identifier for a &#x60;plan&#x60;.
    :type planId: str

    :rtype: Plan
    """
    return 'do some magic!'


def getplans():  # noqa: E501
    """List All plans

    Gets a list of all &#x60;plan&#x60; entities. # noqa: E501


    :rtype: List[Plan]
    """
    return 'do some magic!'


def getsubscription(companyId, subscriptionId):  # noqa: E501
    """Get a subscription

    Gets the details of a single instance of a &#x60;subscription&#x60;. # noqa: E501

    :param companyId: A unique identifier for a &#x60;company&#x60;.
    :type companyId: str
    :param subscriptionId: A unique identifier for a &#x60;subscription&#x60;.
    :type subscriptionId: str

    :rtype: Subscription
    """
    return 'do some magic!'


def getsubscriptions(companyId):  # noqa: E501
    """List All subscriptions

    Gets a list of all &#x60;subscription&#x60; entities. # noqa: E501

    :param companyId: A unique identifier for a &#x60;company&#x60;.
    :type companyId: str

    :rtype: List[Subscription]
    """
    return 'do some magic!'


def updatecompany(companyId, body):  # noqa: E501
    """Update a company

    Updates an existing &#x60;company&#x60;. # noqa: E501

    :param companyId: A unique identifier for a &#x60;company&#x60;.
    :type companyId: str
    :param body: Updated &#x60;company&#x60; information.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Company.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def updateplan(planId, body):  # noqa: E501
    """Update a plan

    Updates an existing &#x60;plan&#x60;. # noqa: E501

    :param planId: A unique identifier for a &#x60;plan&#x60;.
    :type planId: str
    :param body: Updated &#x60;plan&#x60; information.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Plan.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def updatesubscription(companyId, subscriptionId, body):  # noqa: E501
    """Update a subscription

    Updates an existing &#x60;subscription&#x60;. # noqa: E501

    :param companyId: A unique identifier for a &#x60;company&#x60;.
    :type companyId: str
    :param subscriptionId: A unique identifier for a &#x60;subscription&#x60;.
    :type subscriptionId: str
    :param body: Updated &#x60;subscription&#x60; information.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Subscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
