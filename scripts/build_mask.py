# -*- coding: utf-8 -*-

"""
Fichier : build_mask.py
Description : Construction d'un masque raster à partir de la BD Forêt
Autrice : Audrey
Relectrice : Doris
"""

import os
import sys
import geopandas as gpd

sys.path.append('libsigma/')
import read_and_write as rw


def build_mask(shp: str, ref: str, out: str, excl: list = None) -> None:
    """Fonction qui crée un masque raster selon une emprise et
    une résolution spatiale donnée à partir d'un fichier de polygones.
    Optionnellement exclue des classes de polygones résultat.

    Args:
        shp (str): Chemin d'accès pour le fichier de polygones qui serviront à la création du masque.
        ref (str): Chemin d'accès du fichier qui indiquera l'emprise et la résolution spatiale.
        out (str): Chemin pour le ficher de sortie.
        excl (list, optionnal): Liste des classes de polygones à exclure du masque.

    Returns:
        None: Cette fonction ne retourne rien, elle crée un fichier de sortie.
    """

    if excl is None:
        excl = []

    # Identifier les zones à inclure dans le masque
    gdf = gpd.read_file(shp)
    gdf['mask'] = gdf['TFV'].apply(lambda x: 0 if x in excl else 1)
    #print(gdf.head())

    # Récupérer les dimensions
    data_set = rw.open_image(ref)

    y_size, x_size, _ = rw.get_image_dimension(data_set)
    x_min, y_max = rw.get_origin_coordinates(data_set)
    x_psize, y_psize = rw.get_pixel_size(data_set)

    # Calculer l'emprise
    x_max = x_min + x_size * x_psize
    y_min = y_max + y_size * y_psize

    


    


if __name__ == "__main__":

    script_dir = os.path.dirname(os.path.abspath(__file__))

    excluded_values = [
        'Lande',
        'Formation herbacée',
        'Forêt ouverte de conifères purs',
        'Forêt ouverte de feuillus purs',
        'Forêt ouverte sans couvert arboré',
        'Forêt ouverte à mélange de feuillus et conifères',
        'Forêt fermée sans couvert arboré'
    ]

    s2_preprocessed_path = os.path.join(script_dir, '../../data/images/SENTINEL2B_20220326-105856-076_L2A_T31TCJ_C_V3-0_FRE_B11.tif')
    bdforet_shp_path = os.path.join(script_dir, '../../data/project/FORMATION_VEGETALE.shp')
    output_path = os.path.join(script_dir, '../results/data/img_pretraitees/masque_foret.tif')

    build_mask(bdforet_shp_path, s2_preprocessed_path, output_path, excluded_values)
