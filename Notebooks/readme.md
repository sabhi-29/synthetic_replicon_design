# <u> Contents of the folder </u>


### 1. addgene data scrapper.ipynb
* This notebook is responsible for extracting data for all the bacterial plasmids present in Addgene and make a dataframe of the relevent information.

### 2. addgene replication extraction only blast.ipynb
* In this notebook we extracted the CDS features labels in our dataset and made a filtered version of the same
* Extracted the Gene Oncology (GO) Annotations of the feature labels from uniprot using Selenium and restAPI to get GO data

### 3. addgene replication extraction blast.ipynb
* In this notebook we performed online blastx search on NCBI for each unique CDS feature we finalized in **cds_dict_cleaned_v1.pkl**
* We made a dataframe integrating the data scrapped from Addgene, the blast reseults, and GO Annotations
* Made dataframe with information about features involved in replication process

### 4. Nucleotide extraction.ipynb
* In this notebook we are extracting all the replicons present in the dataset

  
*<u>Note:-</u>* All notebooks are work in progress and are updated frequently.
