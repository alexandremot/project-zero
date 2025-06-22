import cv2
import numpy as np
from enum import Enum
from typing import Literal

class ScreensReferences(Enum):
    TELA_INICIAL = "tela_inicial.png"
    TELA_ESCOLHA_CPF_AGENCIA = "cpf_ou_conta.png"
    ENTRE_COM_AGENCA_E_CONTA = "entre_com_agencia_e_conta.png"


def get_reference_image(self, tela_desejada: ScreensReferences) -> np.ndarray | None:
    model_image = cv2.imread(f'models/{tela_desejada.value}')
    if model_image is None:
        print(f"Erro ao carregar a imagem do modelo: {tela_desejada.value}")
        return None
    return model_image