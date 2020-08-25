# coding: utf-8

"""
    Fugue API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UpdateCustomRuleInput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'resource_type': 'str',
        'rule_text': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'resource_type': 'resource_type',
        'rule_text': 'rule_text'
    }

    def __init__(self, name=None, description=None, status=None, resource_type=None, rule_text=None):  # noqa: E501
        """UpdateCustomRuleInput - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._status = None
        self._resource_type = None
        self._rule_text = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if resource_type is not None:
            self.resource_type = resource_type
        if rule_text is not None:
            self.rule_text = rule_text

    @property
    def name(self):
        """Gets the name of this UpdateCustomRuleInput.  # noqa: E501

        Human readable name of the custom rule  # noqa: E501

        :return: The name of this UpdateCustomRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCustomRuleInput.

        Human readable name of the custom rule  # noqa: E501

        :param name: The name of this UpdateCustomRuleInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateCustomRuleInput.  # noqa: E501

        Description of the custom rule  # noqa: E501

        :return: The description of this UpdateCustomRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCustomRuleInput.

        Description of the custom rule  # noqa: E501

        :param description: The description of this UpdateCustomRuleInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this UpdateCustomRuleInput.  # noqa: E501

        Status of the custom rule  # noqa: E501

        :return: The status of this UpdateCustomRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateCustomRuleInput.

        Status of the custom rule  # noqa: E501

        :param status: The status of this UpdateCustomRuleInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def resource_type(self):
        """Gets the resource_type of this UpdateCustomRuleInput.  # noqa: E501

        Resource type to which the custom rule applies  # noqa: E501

        :return: The resource_type of this UpdateCustomRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this UpdateCustomRuleInput.

        Resource type to which the custom rule applies  # noqa: E501

        :param resource_type: The resource_type of this UpdateCustomRuleInput.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def rule_text(self):
        """Gets the rule_text of this UpdateCustomRuleInput.  # noqa: E501

        Rego code used by the rule  # noqa: E501

        :return: The rule_text of this UpdateCustomRuleInput.  # noqa: E501
        :rtype: str
        """
        return self._rule_text

    @rule_text.setter
    def rule_text(self, rule_text):
        """Sets the rule_text of this UpdateCustomRuleInput.

        Rego code used by the rule  # noqa: E501

        :param rule_text: The rule_text of this UpdateCustomRuleInput.  # noqa: E501
        :type: str
        """

        self._rule_text = rule_text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateCustomRuleInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
