import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\obstacle_sensor_data.csv")

kmeans = KMeans(n_clusters=2).fit(data)

joblib.dump(kmeans,"C:\\Users\\ICTC\\Desktop\\ICS Final\\ICS-520-Project-201(1)\\ML-obstacles.sav")

centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(data['density'], data['reflection'])
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)


#Note: there are clearly two clusters
plt.show()






