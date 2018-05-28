# SVDistic
Optimized-for-speed Eigen implementations of SVD, SVD++ and TimeSVD++ algorithms.

![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Maintenance Intended](http://maintained.tech/badge.svg)](http://maintained.tech/) 
## Requirements
This application is fully Dockerized for easier usage. We suggest having at least Docker 18.03.1-ce installed.

If you wish to do not wish to deploy through Docker, you must have Eigen installed.
Find installation instructions here:
<http://eigen.tuxfamily.org/index.php?title=Main_Page>.

## Usage
Usage instructions for the actual Svdistic program.
```
Usage: ./svdistic <svd/svdpp/help> <train/infer/score>
Options: required settings are flaired with [r]
-model_id    STRING:  name of the model
-fname       STRING:  file name of data in data/corpus/
-n_product   INT:     number of products
-n_user      INT:     number of users
-n_example   INT:     number of examples to process
-report_freq INT:     frequency of epoch reports
-n_epochs    INT:     number of epochs to run training for
-reg_weight  FLOAT:   weight regularization strength
-reg_bias    FLOAT:   bias regularization strength
-lr          FLOAT:   learning rate
-lr_decay    FLOAT:   learning rate decay
```

Add your data files to /data/corpus and note the filename as command line arguments to the program. For training and validation, your data files must match the data format specified in the following section with three valid columns denoting user id, product id and ranking. For inference, your data file must still meet the data format, but fill in whatever you want for ranking.

## Docker
Use Docker for painless hyperparameter optimization.
Simply update the Dockerfile to download your dataset into data/corpus and add your desired hyperparameter cases to docker-compose.

## Speed.
We performed benchmarks on a 2 core i7-7660U 2.5GHz processor with process memory usage capped at 0.4GB. We test the speed of an epoch across 95 million examples with 500,000 users and 18,000 products, using 200 latent factors.
The basic SVD model takes 20 second per epoch. The SVD++ model takes 35 seconds per epoch.

## Data format.
### Input data.
The standard data format is a csv file, where each entry corresponding to a ranking.
Do not add a header line.

Each line consists of 3 pairs: `user_index,product_index,score`.
To calculate the user index, transform user ids to indices ranging from 0 to the number of users.
The same process applies to product indexing.
Scores are expected to be integer values, although we weakly support float rankings.

Please note that **entries must be ordered by user index**. Entries with the same user index should be consecutive in the data file.

### Weight dumps.
Weights dumps are a column-major iteration through matrix
values. Every entry is separated by a newline.

