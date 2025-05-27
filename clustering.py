import pandas as pd
import numpy as np
from sklearn import neighbors

def assign_packages(packages, vehicles, city_coords):
    vehicles['x'] = vehicles['origin_city'].map(lambda c: city_coords[c][0])
    vehicles['y'] = vehicles['origin_city'].map(lambda c: city_coords[c][1])

    attr_train = vehicles[['x', 'y']].values
    objective_train = vehicles['id'].values

    clasif_knn = neighbors.KNeighborsClassifier(n_neighbors=2, metric='euclidean')
    clasif_knn.fit(attr_train, objective_train)

    packages['x'] = packages['init_city'].map(lambda c: city_coords[c][0])
    packages['y'] = packages['init_city'].map(lambda c: city_coords[c][1])
    attr_test = packages[['x', 'y']].values

    distances, neighbors_ids = clasif_knn.kneighbors(attr_test)

    packages['vehicle_id'] = None
    vehicles['actual_load'] = 0

    for i in range(len(packages)):
        p_size = packages.at[i, 'size']
        vecinos = neighbors_ids[i]  # índices en el array de vehículos

        for v in vecinos:
            v_id = vehicles.at[v, 'id']
            cap = vehicles.at[v, 'capacity']
            carga = vehicles.at[v, 'actual_load']

            if carga + p_size <= cap:
                packages.at[i, 'vehicle_id'] = v_id
                vehicles.at[v, 'actual_load'] = carga + p_size
                break  # asignado, no hace falta probar el otro

    return packages, vehicles


