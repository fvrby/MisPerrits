from django.test import TestCase

from Perris.models import Post

class PostTest(TestCase):
    def setUp(self):
        #arrange
        Post.objects.create(name="gato")
        #act
    def gato_can_include(self):
        gato = Post.objects.get(name="gato")
        #Assert
        self.assertEqual(Post)
        


class PostTestCase( TestCase ):
    def test_postPublish( self ):
        # Arrange
        expected = 2
        result = -1
        # Act
        result = 2
        # Assert
        self.assertEqual(expected,result)

    def test_postPublish2( self ):
        # Arrange
        expected = 2
        result = -1
        # Act
        result = 3
        # Assert
        self.assertEqual(expected,result)

    def test_postPublish3( self ):
        # Arrange
        expected = 2
        result = -1
        # Act
        result = 2
        # Assert
        self.assertEqual(expected,result)
