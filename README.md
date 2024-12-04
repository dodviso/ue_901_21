## Images Sentinel-2 relevées
Téléchargées depuis le portail Theia

|Date|Taux de couverture nuageuse (%)| Période |
|----|---------------------------|---------|
| 2022-03-26  | 14  | Printemps |
| 2022-04-05  | 0  | Printemps |
| 2022-08-03  | 0  | Été |
| 2022-09-22  | 0  | Automne |
| 2022-11-11  | 0  | Automne |
| 2023-02-09  | 3  | Hiver |

## Données fournies

**FORMATION_VEGETALE.shp** :  
Issu de la BD Forêt, formations végétales de la Haute-Garonne   
Contient les TFV (types de formation végétale) suivants :
```python
tfv_bdforet = [
    'Formation herbacée',
    'Forêt fermée de châtaignier pur',
    'Forêt fermée de chênes décidus purs',
    'Forêt fermée de chênes sempervirents purs',
    'Forêt fermée de conifères purs en îlots',
    'Forêt fermée de douglas pur',
    'Forêt fermée de feuillus purs en îlots',
    'Forêt fermée de hêtre pur',
    'Forêt fermée de mélèze pur',
    'Forêt fermée de pin laricio ou pin noir pur',
    'Forêt fermée de pin maritime pur',
    'Forêt fermée de pin sylvestre pur',
    'Forêt fermée de robinier pur',
    'Forêt fermée de sapin ou épicéa',
    'Forêt fermée d’un autre conifère pur autre que pin',
    'Forêt fermée d’un autre feuillu pur',
    'Forêt fermée d’un autre pin pur',
    'Forêt fermée sans couvert arboré',
    'Forêt fermée à mélange de conifères',
    'Forêt fermée à mélange de conifères prépondérants et feuillus',
    'Forêt fermée à mélange de feuillus',
    'Forêt fermée à mélange de feuillus prépondérants et conifères',
    'Forêt fermée à mélange de pins purs',
    'Forêt fermée à mélange d’autres conifères',
    'Forêt ouverte de conifères purs',
    'Forêt ouverte de feuillus purs',
    'Forêt ouverte sans couvert arboré',
    'Forêt ouverte à mélange de feuillus et conifères',
    'Lande',
    'Peupleraie'
]
```

## Mapping des TFV vers noms et codes demandés par le prof
```python
map_tfv_classif = {
    'Forêt fermée de châtaignier pur': {
        'Nom': 'Autres feuillus',
        'Code': 11
    },
    'Forêt fermée de chênes décidus purs': {
        'Nom': 'Chênes',
        'Code': 12
    },
    'Forêt fermée de conifères purs en îlots': {
        'Nom': 'Conifères en îlots',
        'Code': 27
    },
    'Forêt fermée de douglas pur': {
        'Nom': 'Douglas',
        'Code': 23
    },
    'Forêt fermée de feuillus purs en îlots': {
        'Nom': 'Feuillus en îlots',
        'Code': 16
    },
    'Forêt fermée de hêtre pur': {
        'Nom': 'Autres feuillus',
        'Code': 11
    },
    'Forêt fermée de mélèze pur': {
        'Nom': 'Autres conifères autre que pin',
        'Code': 21
    },
    'Forêt fermée de pin laricio ou pin noir pur': {
        'Nom': 'Pin laricio ou pin noir',
        'Code': 24
    },
    'Forêt fermée de pin maritime pur': {
        'Nom': 'Pin maritime',
        'Code': 25
    },
    'Forêt fermée de pin sylvestre pur': {
        'Nom': 'Autres pin',
        'Code': 22
    },
    'Forêt fermée de robinier pur': {
        'Nom': 'Robinier',
        'Code': 13
    },
    'Forêt fermée de sapin ou épicéa': {
        'Nom': 'Autres conifères autre que pin',
        'Code': 21
    },
    'Forêt fermée d’un autre conifère pur autre que pin': {
        'Nom': 'Autres conifères autre que pin',
        'Code': 21
    },
    'Forêt fermée d’un autre feuillu pur': {
        'Nom': 'Autres feuillus',
        'Code': 11
    },
    'Forêt fermée d’un autre pin pur': {
        'Nom': 'Autres pins',
        'Code': 22
    },
    'Forêt fermée à mélange de conifères': {
        'Nom': 'Mélange conifères',
        'Code': 26
    },
    'Forêt fermée à mélange de conifères prépondérants et feuillus': {
        'Nom': 'Mélange de conifères prépondérants et feuillus',
        'Code': 28
    },
    'Forêt fermée à mélange de feuillus': {
        'Nom': 'Mélange de feuillus',
        'Code': 15
    },
    'Forêt fermée à mélange de feuillus prépondérants et conifères': {
        'Nom': 'Mélange de feuillus prépondérants et conifères',
        'Code': 29
    },
    'Forêt fermée à mélange de pins purs': {
        'Nom': 'Autres pin',
        'Code': 22
    },
    'Forêt fermée à mélange d’autres conifères': {
        'Nom': 'Autres conifères autre que pin',
        'Code': 21
    },
    'Peupleraie': {
        'Nom': 'Peupleraie',
        'Code': 14
    }
}
```

## Liste des noms pour classif pixel

```python
classes_cl_pixel = [
    'Autres feuillus',
    'Chêne',
    'Robinier',
    'Peupleraie',
    'Autres conifères autre que pin',
    'Autres pin',
    'Douglas',
    'Pin laricio ou pin noir',
    'Pin maritime'
]
```

