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


class Scan(object):
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
        'id': 'str',
        'environment_id': 'str',
        'created_at': 'int',
        'updated_at': 'int',
        'finished_at': 'int',
        'status': 'str',
        'message': 'str',
        'remediation_error': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'environment_id': 'environment_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'finished_at': 'finished_at',
        'status': 'status',
        'message': 'message',
        'remediation_error': 'remediation_error'
    }

    def __init__(self, id=None, environment_id=None, created_at=None, updated_at=None, finished_at=None, status=None, message=None, remediation_error=None):  # noqa: E501
        """Scan - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._environment_id = None
        self._created_at = None
        self._updated_at = None
        self._finished_at = None
        self._status = None
        self._message = None
        self._remediation_error = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if environment_id is not None:
            self.environment_id = environment_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if finished_at is not None:
            self.finished_at = finished_at
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if remediation_error is not None:
            self.remediation_error = remediation_error

    @property
    def id(self):
        """Gets the id of this Scan.  # noqa: E501

        ID of the scan.  # noqa: E501

        :return: The id of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scan.

        ID of the scan.  # noqa: E501

        :param id: The id of this Scan.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def environment_id(self):
        """Gets the environment_id of this Scan.  # noqa: E501

        ID of the environment the scan belongs to.  # noqa: E501

        :return: The environment_id of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this Scan.

        ID of the environment the scan belongs to.  # noqa: E501

        :param environment_id: The environment_id of this Scan.  # noqa: E501
        :type: str
        """

        self._environment_id = environment_id

    @property
    def created_at(self):
        """Gets the created_at of this Scan.  # noqa: E501

        Time the scan was created.  # noqa: E501

        :return: The created_at of this Scan.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Scan.

        Time the scan was created.  # noqa: E501

        :param created_at: The created_at of this Scan.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Scan.  # noqa: E501

        Time the scan was last updated.  # noqa: E501

        :return: The updated_at of this Scan.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Scan.

        Time the scan was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Scan.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def finished_at(self):
        """Gets the finished_at of this Scan.  # noqa: E501

        Time the scan was finished.  # noqa: E501

        :return: The finished_at of this Scan.  # noqa: E501
        :rtype: int
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this Scan.

        Time the scan was finished.  # noqa: E501

        :param finished_at: The finished_at of this Scan.  # noqa: E501
        :type: int
        """

        self._finished_at = finished_at

    @property
    def status(self):
        """Gets the status of this Scan.  # noqa: E501

        Status of the scan.  # noqa: E501

        :return: The status of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Scan.

        Status of the scan.  # noqa: E501

        :param status: The status of this Scan.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "QUEUED", "IN_PROGRESS", "ERROR", "SUCCESS", "CANCELED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self):
        """Gets the message of this Scan.  # noqa: E501

        Message related to the scan.  # noqa: E501

        :return: The message of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Scan.

        Message related to the scan.  # noqa: E501

        :param message: The message of this Scan.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def remediation_error(self):
        """Gets the remediation_error of this Scan.  # noqa: E501

        Indicates whether there were any remediation errors on the scan.  # noqa: E501

        :return: The remediation_error of this Scan.  # noqa: E501
        :rtype: bool
        """
        return self._remediation_error

    @remediation_error.setter
    def remediation_error(self, remediation_error):
        """Sets the remediation_error of this Scan.

        Indicates whether there were any remediation errors on the scan.  # noqa: E501

        :param remediation_error: The remediation_error of this Scan.  # noqa: E501
        :type: bool
        """

        self._remediation_error = remediation_error

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
        if not isinstance(other, Scan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
