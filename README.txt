# Genetic algorithms for clustered VRP

- Introduction

Clustering method based on Genetic Algorithms is used in order to solve the Vehicle Routing Problem [1]. The solution combines two approaches: Clustering and Genetic Algorithm (GA) and consist on showing the optimum delivery routes of a set of vehicles when delivering a set of packages into their destination citiess.

1. Clustering: assignment of packages to vehicles using K-Nearest Neighbors (kNN)
2. Genetic Algorithm: optimizing each vehicle delivery route using a GA
3. Executing different experiments and visualizing the results obtained in order to compare them

----

- Project Structure

main.py: it connects data folder, clustering.py, ga.py and results. And it is use to plot the results and graphs
clustering.py: defines kNN algorithm
ga.py: contains GA implementation with mutation and crossover

----

- How to Run

1. Python libraries must be installed: pip install pandas numpy scikit-learn matplotlib

2. Input data files must be in a folder named data/: packages.csv, vehicles.csv and distances.csv

3. Run: python main.py

- 


