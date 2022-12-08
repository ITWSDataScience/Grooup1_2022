import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import numpy as np

import csv

# helper for reading in state names (
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut",  "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia",  "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

hydros = []
for state in state_names:
    hydros.append([state, 0])

incomeData = []
for state in states:
    incomeData.append([state, 0])

print(len(hydros), "hydros")

print(len(states), len(state_names))

features = []
for i in range(50):
   features.append([0,0,0])

# read in precipitation and population
with open('precipitation_average_per_state.csv', newline='') as f:
   rows = list(csv.reader(f))  # Read all rows into a list
for row in rows:
   state = row[2]
   for i in range(50):
      if states[i] == state:
         features[i][0] = row[1] # precipitation
         features[i][1] = int(row[4].replace(',', '')) # population

print("got here ok")

# read in number of hydro plants
with open('hydropower_plants_US.csv', newline='',  encoding="utf8") as f:
   rows = list(csv.reader(f))  # Read all rows into a list
for row in rows:
    for i in range(50):
        if states[i] == row[3]:
             #features[i][2] += 1 # increment # of hydro plants
             hydros[i][1] += 1
        elif states[i] == row[4]:
             #features[i][2] += 1 # increment # of hydro plants
             hydros[i][1] += 1
        elif states[i] == row[2]:
             #features[i][2] += 1 # increment # of hydro plants
             hydros[i][1] += 1
print("hydros:")
print(hydros)

# read in income

with open('ACSST5Y2020.S1902-Data.csv', newline='') as f:
 rows = list(csv.reader(f))  # Read all rows into a list


for row in rows:
    state = row[1]
    for i in range(50):
        if state_names[i] == state:
            features[i][2] = row[74]  # income
            incomeData[i][1] = row[74]


print("Income data:", incomeData)

print("first 5 state features:", features[:5])

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

sseList = []
for i in range(1, 11):

    kmeans = KMeans(
        init="random",
        n_clusters=i,
        n_init=10,
        max_iter=50,
        random_state=42
    )

    kmeans.fit(scaled_features)
    sseList.append(kmeans.inertia_)
    # lowest SSE
    #print("lowest SSE:", kmeans.inertia_)
    # final centers
    #print("final centers:", kmeans.cluster_centers_)
    # iterations we needed
    #print("it took ", kmeans.n_iter_, "iterations")

    #print(kmeans.labels_[:5])

plt.plot(range(1, 11), sseList)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()


# A list holds the silhouette coefficients for each k
silhouette_coefficients = []

for k in range(2, 11):
    kmeans = KMeans(
        init="random",
        n_clusters=k,
        n_init=10,
        max_iter=50,
        random_state=42
    )
    kmeans.fit(scaled_features)
    score = silhouette_score(scaled_features, kmeans.labels_)
    silhouette_coefficients.append(score)

plt.plot(range(2, 11), silhouette_coefficients)
plt.xticks(range(2, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")
plt.show()


kmeans = KMeans(
        init="random",
        n_clusters=3,
        n_init=10,
        max_iter=100,
        random_state=42
    )

kmeans.fit(scaled_features)
print(len(kmeans.labels_))
print(kmeans.labels_)

# final centers
print("final centers:", kmeans.cluster_centers_)

labeledStates = []
for i in range(50):
    labeledStates.append([state_names[i], kmeans.labels_[i]])

print(labeledStates)

X = scaled_features

y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[y_kmeans==0, 0], X[y_kmeans==0, 1], s=100, c='red', label ='Cluster 1')
plt.scatter(X[y_kmeans==1, 0], X[y_kmeans==1, 1], s=100, c='blue', label ='Cluster 2')
plt.scatter(X[y_kmeans==2, 0], X[y_kmeans==2, 1], s=100, c='green', label ='Cluster 3')
#plt.scatter(X[y_kmeans==3, 0], X[y_kmeans==3, 1], s=100, c='cyan', label ='Cluster 4')

#Plot the centroid. This time we're going to use the cluster centres  #attribute that returns here the coordinates of the centroid.
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label = 'Centroids')

plt.show()

print("hydros:")
print(hydros)