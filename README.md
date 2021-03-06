# Metaheuristics Research Algorithms [![Build Status](https://travis-ci.org/earaujoassis/metaheuristics.svg)](https://travis-ci.org/earaujoassis/metaheuristics)

> Metaheuristics algorithms applications

Each folder has a different purpose:

* **eo**: it contains an extension for the [*Evolving Objects*](http://eodev.sourceforge.net/)
(EO) Library, written in C++; that extension is a hybridization module for Genetic Algorithms,
named In Vitro Fertilization Module (IVFm), or In Vitro Fertilization Genetic Algorithm (IVF-GA).
That folder also contains an application code: an algorithm that uses IVF-GA as a solver to
some Multidimensional 0-1 Knapsack instances.

* **scheduling**: it contains application code for some well known scheduling problem classes,
mainly Open-shop, Flow-shop, and Job-shop. Each one has its own problem instances files, used for
results analysis and algorithm tuning. Those instances files are not mine and should be disregarded
from the LICENSE scope.

## Setup & Running

```sh
$ sh build-evolve.sh
$ make scheduling
$ scheduling/cli/scheduling.py jobshop ci/config/jobshop_descriptor.json
```

## Dependencies

 * [Evolving Objects](http://eodev.sourceforge.net/)
 * [Evolve](http://evolvecode.org/)

## License

Please refer to the included LICENSE file for terms of use.

Apache License, Version 2.0. Copyright 2011-2015 &copy; Ewerton Assis.
