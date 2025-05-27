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

----

- Methodology

* Package Assigment: packages are asigned to one vehicle and if that vehicle is already full, it is assigned to the next one, this is done using kNN.

* Route optimization: looks for the best route for each vehicle using GA and minimizing the total distance travelled.

*Experiments: test of different population sizes and mutation probabilities and calculate the average fitness of each experiment.

----

- Experiments

If you want to modify the experiments, go to the last part of main.py and change:

  experiments = [
      {'population': 20, 'mutation': 0.1, '1': 123.4, '2': 125.6, '3': 124.1},
      {'population': 30, 'mutation': 0.1, '1': 120.0, '2': 118.5, '3': 119.2},
      {'population': 30, 'mutation': 0.25, '1': 108.0, '2': 109.5, '3': 107.3},
      {'population': 50, 'mutation': 0.3, '1': 105.2, '2': 106.8, '3': 104.5}
  
  ]

----

- Outputs

* Packages going to each vehicle

* Best route of each vehicle and total distance

* Bar chart: Route travelled per vehicle and comparison of each experiment




