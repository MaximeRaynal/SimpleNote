/**
 * "Moteur" de template minimaliste le but est de simplifié la créatoin
 * de "composant" pour par exemple coller à des données.
 * Pas fait pour gérer des gros templates,
 * pas de compilation, pas de fonction.
 * Dans un premier temps les variables et ensuite du code libre, gestion d'une
 * valeur en cas d'abscence
 */
function Template() {

    this.variableRegex = /{{\s*([a-zA-Z][\w-]*)\s*}}/g;

    this.render = function (template, datas) {

    }

}