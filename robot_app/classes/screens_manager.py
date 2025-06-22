from enum import StrEnum
from enums.screens_references import ScreensReferences
import cv2
import numpy as np

class ScreensManager:
    def get_reference_image(self, tela_desejada: ScreensReferences) -> np.ndarray | None:
        if not isinstance(tela_desejada, ScreensReferences):
            raise TypeError("Parâmetro deve ser do tipo ScreensReferences")
            
        model_image = cv2.imread(f'models/{tela_desejada.value}')
        if model_image is None:
            print(f"Erro ao carregar a imagem do modelo: {tela_desejada.value}")
            return None
        return model_image
