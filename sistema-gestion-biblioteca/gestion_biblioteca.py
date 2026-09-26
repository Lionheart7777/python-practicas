"""
Objetivo: practicar herencia, super(), polimorfismo y encapsulamiento básico.

Requisitos

1. Clase base Material

Atributos: titulo, autor, disponible (bool, default True)
Método info() → imprime titulo y autor
Método prestar() → si está disponible, lo marca como no disponible e imprime confirmación; si no, avisa que no se puede
Método devolver() → lo marca como disponible

2. Clases hijas que heredan de Material

Libro: agrega paginas y genero
Revista: agrega numero_edicion
DVD: agrega duracion_minutos

Cada una debe sobrescribir info() llamando con super().info() al padre, y agregando su propio dato extra (ej: el libro muestra también el genero).

3. Clase biblio

Atributo: catalogo (lista de materiales)
Método agregar_material(material)
Método buscar_por_titulo(titulo) → devuelve el material o None
Método mostrar_catalogo() → recorre todo el catálogo y llama .info() de cada uno (acá es donde se ve el polimorfismo: no importa si es Libro, Revista o DVD, todos responden a .info() distinto)
Método prestar_material(titulo) → busca y llama .prestar()
Ejemplo de uso esperado
python
biblio = Biblioteca()
biblio.agregar_material(Libro("Cien años de soledad", "García Márquez", 471, "Realismo mágico"))
biblio.agregar_material(Revista("National Geographic", "Varios", 305))
biblio.agregar_material(DVD("Matrix", "Wachowski", 136))

biblio.mostrar_catalogo()
biblio.prestar_material("Matrix")
biblio.prestar_material("Matrix")  # debería avisar que ya no está disponible
Desafío extra (opcional)

Agregá una clase MaterialDigital (mixin o herencia múltiple) que tenga un método descargar(), y una clase EBook(Libro, MaterialDigital) que combine ambas — así probás herencia múltiple."""


class Material :
    def __init__(self, titulo, autor, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
  
    def info(self):
        stock = "Disponible" if self.disponible else "No Disponible"
        return f"titulo: {self.titulo}, Autor: {self.autor}, Stock:{stock}"
        
    def prestar(self):
        tipo = type(self).__name__
        if self.disponible: 
            self.disponible = False
            return f"{tipo}, '{self.titulo}' se acaba de prestar." # lo guarda
        else:
            return f"{tipo}, '{self.titulo}' ya se prestó. No se puede prestar."

    def devolver(self):
        tipo = type(self).__name__
        self.disponible = True
        return f"{tipo}, '{self.titulo}' ha sido devuelto."

    
    
class Libro(Material):
    def __init__(self, titulo, autor, paginas, genero):
        super().__init__(titulo, autor)
        self.paginas= paginas
        self.genero = genero
    
    def info(self):
        info_Dad = super().info()
        return f" {info_Dad}, Páginas : {self.paginas}, Genero : {self.genero}"

       

class Revista(Material):
    def __init__(self, titulo, autor, numero, edicion):
        super().__init__(titulo, autor)
        self.numero = numero
        self.edicion = edicion

    def info(self):
        info_Dad = super().info()
        return f"{info_Dad}, Número : {self.numero}, Edición : {self.edicion}"


    
class DVD(Material):
    def __init__(self, titulo, autor, duracion_minutos):
        super().__init__(titulo, autor)
        self.duracion = duracion_minutos
    
    def info(self):
        info_Dad = super().info()
        return f" {info_Dad}, duracion Minutos de DVD : {self.duracion}"

    
    
class Biblioteca():
    def __init__(self):
        self.coleccion = []
    
    def agregar_material(self,material):
        self.coleccion.append(material)
    
    def buscar_por_titulo(self, titulo):
        for item in self.coleccion:
            if item.titulo  == titulo:
                return item
        print(f" No se encontró  el Título : {titulo}")
        return None   
    
    def mostrar_catalogo(self):
        for materia in self.coleccion:
            print(materia.info())
    
    def prestar_material(self, titulo):
        mater = self.buscar_por_titulo(titulo)
        if mater:
            print(mater.prestar())
       
       
            
class MaterialDigital:
    def descargar(self):
        return f"Descargando '{self.titulo}' ...."



class EBook(Libro, MaterialDigital):
    def __init__(self, titulo, autor, paginas, genero):
        super().__init__(titulo, autor, paginas, genero ) 
        
    
#libro = Libro("Cien años de soledad", "García Márquez", 471, "Realismo mágico")
#print(libro.info()) 

#libro = Libro("Test", "Autor", 100, "Genero")
#print(libro.__class__.__name__)
"""
libro = Libro("Test", "Autor", 100, "Novela")
libro.prestar()        # primera vez, disponible=True → entra al if
print(libro.prestar())  # segunda vez, disponible=False → entra al else


biblio = Biblioteca()
libro = Libro("Cien años de soledad", "García Márquez", 471, "Realismo mágico")
biblio.agregar_material(libro)
print(len(biblio.coleccion))
biblio.mostrar_catalogo()

biblio.buscar_por_titulo("aa")

resultado = biblio.buscar_por_titulo("Cien años de soledad")
print(resultado)

if  resultado:
    print(resultado.info())
    
prestadito = biblio.prestar_material("AA")
print(prestadito) """

biblio = Biblioteca()
biblio.agregar_material(Libro("Cien años de soledad", "García Márquez", 471, "Realismo mágico"))
biblio.agregar_material(Revista("National Geographic", "Varios", 305, "Edición Especial"))
biblio.agregar_material(DVD("Matrix", "Wachowski", 136))

biblio.mostrar_catalogo()
biblio.prestar_material("Matrix")
biblio.prestar_material("Matrix")  # debería avisar que ya no está disponible

ebook = EBook("Python para todos", "Autor X", 200, "Programación")
print(ebook.info())        # heredado de Libro
print(ebook.descargar())   # heredado de MaterialDigital


