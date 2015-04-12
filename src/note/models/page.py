import re

class Page(object):
    """ Représentation d'une page

        Une page est un élément d'une note, on peut attacher des éléments à une
        page.
        Une page est stocké sur le serveur sous forme de fichier, suivant le
        principe suivant :
        Nom : ordre_NomDeLaPage
        Texte : contenu du fichier
        Tags : :see_also get_tags
    """

    def __init__(self):
        self.name = "Test"
        self.order = 1
        self.text = ""
        self.tags = set()

    def load_from_file(self, page_name):
        self.text = open(page_name, 'r').readlines()
        self.name = page_name.split('_')[1]
        self.order = page_name.split('_')[0]
        self.tags = self.get_tags()
        return self

    def __str__(self):
        return self.order + '_' + self.name

    def get_tags(self):
        """ Retourne tout les tags présents dans le texte de la page sans le #
            qui prefixe le tag.

            Est un tag tout mot commencant par un dièse (#)
            suivit de N chiffres, lettres, ponctuation, caractères spéciaux
            #unTag #1autre-tag #tag.composé #premier_tag#secondtag
        """
        return set(map(lambda tag: tag[1:].strip(),
                          re.compile(r'#[^#\s]+[\s]*').findall(self.text)))
