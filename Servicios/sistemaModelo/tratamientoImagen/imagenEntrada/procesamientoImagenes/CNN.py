from tratamientoImagen.imagenEntrada.procesamientoImagenes.EstrategiaProcesamientoImagenes import EstrategiaProcesamientoImagenes


class CNN(EstrategiaProcesamientoImagenes):

    def procesar(self, img):
        print("funciona CNN")
        return img