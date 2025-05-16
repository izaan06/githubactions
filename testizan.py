
import unittest
from prova_escrita3 import *
from prova_escrita4 import *

class TestProvaEscrita03(unittest.TestCase):
    """
    Unes proves per verificar les funcions del mòdul prova_escrita3.
    """
    def test1(self):
        """
        Provem la funció trobar_min_max_rendiment per comprovar que retorna 
        els valors mínim i màxim correctes d'un conjunt de valors.
        """
        resultat = trobar_min_max_rendiment(10.00, 12.00, 15.00)
        # Es comprova que la funció retorni la tupla amb el valor mínim (10.00) i màxim (15.00)
        self.assertEqual(resultat, (10.00, 15.00))
    
    def test2(self):
        """
        Provem la funció comptar_estudiants per verificar que compta correctament 
        el nombre d'estudiants.
        """
        resultat = comptar_estudiants(notes_estudiants)
        # Comprovem que el nombre d'estudiants sigui 4
        self.assertEqual(resultat, 4)
    
    def test3(self):
        """
        Agafo la funció comptar_estudiants_matèria_v2 per comprovar que compta 
        correctament el nombre d'estudiants inscrits en una matèria específica.
        """
        resultat = comptar_estudiants_matèria_v2(notes_estudiants, "Matemàtiques")
        # Comprovem que el nombre d'estudiants a la matèria Matemàtiques sigui 3
        self.assertEqual(resultat, 3)

class TestProvaEscrita04(unittest.TestCase):
    """
    Unes proves per verificar les funcions del mòdul prova_escrita4.
    """
    def test1(self):
        """
        Provo la funció cercar_el per comprovar que troba correctament el valor 
        de destinació a la matriu i retorna la posició correcta si es demana.
        """
        # Cas on el valor es troba a la matriu i no es sol·licita la posició
        resultat = cercar_el(matriu, 5)
        self.assertEqual(resultat, (True, None))
        # Cas on el valor es troba i es sol·licita la posició
        resultat = cercar_el(matriu, 5, mostrar_posicio=True)
        self.assertEqual(resultat, (True, (1, 1)))  
        # Cas on el valor no es troba
        resultat = cercar_el(matriu, 10)
        self.assertEqual(resultat, (False, None))
        
    def test2(self):
        """
        Provo la funció sumar_fila per comprovar que suma correctament tots els 
        elements d'una fila específica de la matriu.
        """
        # Cas amb una fila vàlida
        resultat = sumar_fila(matriu, 1)
        self.assertEqual(resultat, 15)
        # Cas amb un índex de fila que no existeix
        resultat = sumar_fila(matriu, 5) 
        # Si la fila no existeix, la funció hauria de retornar None
        self.assertIsNone(resultat) 
    
    def test3(self):
        """
        Agafo la funció sumar_matriu per comprovar que suma correctament tots 
        els elements de la matriu.
        """
        # Cas on es sumen tots els elements de la matriu
        resultat = sumar_matriu(matriu)
        # La suma de tots els elements de la matriu hauria de ser 45
        self.assertEqual(resultat, 45)
        
    def test4(self):
        """
        Agafo la funció transformar per comprovar que les operacions 
        (+, -, *, /) a la matriu produeixen els resultats correctes.
        """
        def setUp(self):
            """
            Preparo la matriu inicial per les operacions.
            """
            self.matriu = [[1,2,3], [4,5,6], [7,8,9]]
            # Test de suma (afegir 10 a cada element de la matriu)
            resultatesperat = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
            resultat = transformar(matriu, 10, "+" )
            self.assertEqual(matriu, resultatesperat )
            # Test de resta (restar 10 a cada element de la matriu)
            resultatesperat = [[-9, -8, -7], [-6, -5, -4], [-3, -2, -1]]
            resultat = transformar(matriu, 10, "-")
            self.assertEqual(resultat, resultatesperat)
            # Test de multiplicació (multiplicar cada element de la matriu per 10)
            resultatesperat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
            resultat = transformar(matriu, 10, "*")
            self.assertEqual(resultat, resultatesperat)
            # Test de divisió (dividir cada element de la matriu per 10)
            resultatesperat = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
            resultat = transformar(matriu, 10, "/")
            self.assertEqual(resultat, resultatesperat)

# Executem les proves
if __name__ == "__main__":
    unittest.main()
        



