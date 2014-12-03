from django.test import TestCase
from note.models import Page

# Create your tests here.

class PageMethodTests(TestCase):

    def test_extract_tags(self):
        """ Test la méthode d'extraction de tag """
        p = Page()
        p.text = """#test
        Un test #plus long
        Test un #tag.compose
        Piege pastag#tag
        et pour finir #tag1#tag2
        """

        self.assertSetEqual({'test', 'plus', 'tag.compose',
                             'tag', 'tag1', 'tag2'}, p.get_tags())
