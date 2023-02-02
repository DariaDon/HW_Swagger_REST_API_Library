# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book import Book  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBookController(BaseTestCase):
    """BookController integration test stubs"""

    def test_create_book(self):
        """Test case for create_book

        Метод добавления новой книги в каталог
        """
        body = Book()
        response = self.client.open(
            '/api/v1//books',
            method='POST',
            data=json.dumps(body),
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_book_by_id(self):
        """Test case for delete_book_by_id

        Метод удаления книги по идентификатору
        """
        response = self.client.open(
            '/api/v1//books/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_book_by_id(self):
        """Test case for get_book_by_id

        Метод получения книги по идентификатору
        """
        response = self.client.open(
            '/api/v1//books/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_books(self):
        """Test case for get_books

        Метод получения книг
        """
        response = self.client.open(
            '/api/v1//books',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_book(self):
        """Test case for update_book

        Метод обновления книги в каталоге
        """
        body = Book()
        response = self.client.open(
            '/api/v1//books/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
