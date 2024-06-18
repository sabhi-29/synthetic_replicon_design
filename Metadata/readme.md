# <u> Contents of the folder </u>

### 1. addgene_metadata.pkl 
* Dictionary that contains all the data extracted from Addgene using the API. Include the following features that were extracted - Plasmid ID,	Plasmid Name,	Vector backbone,	Vector type,	Bacterial Resistance(s),	Growth Temperature,	Growth Strain(s),	Copy number,	Gene/Insert name,	Species	Insert Size (bp),	Cloning method,	5′ sequencing primer,	Organism,	Topology
* Created in **addgene data scrapper.ipynb**

### 2. sample_db.csv
* Created to ensure the code captures all the addgene we require for our project


### 3. temp_files
  * **cds_blasts_done.pkl**
    * Created in **addgene replication extraction blast.ipynb**
    * Contains the top 10 blastx result (descriptions and protein sequences) for all the unique cds feature labels we have in our dataset.
  * **cds_dict.pkl**
    * Created in **addgene replication extraction only blast.ipynb**
    * Contains all the cds feature present in our dataset **db_wo_blast_uniprot.csv**  along with their corresponding nucleotide seqeunce
  * **cds_dict_cleaned_v1.pkl**
    * Created in **addgene replication extraction only blast.ipynb**
    * Contains all the cds features from **cds_dict.pkl** we consider for doing blastx search along with their corresponding nucleotide seqeunce
  * **cds_go_done.pkl**
    *  Created in **addgene replication extraction only blast.ipynb**
    *  Contains all the cds features in **cds_dict_cleaned_v1.pkl** and their corresponding Gene Oncology (GO) Annotations



### 4. addgene_plasmid_data_df_v1.pkl
* Dataframe contating the addgene meta data along with the genbank file information.
* Created in **addgene data scrapper.ipynb**

### 5. addgene_plasmid_data_df_v1.csv
* Same as **addgene_plasmid_data_df_v1.pkl** but in csv format

### 6. addgene_plasmid_data_dict_v1.pkl
* Same as **addgene_plasmid_data_df_v1.pkl** but in dictionary format

### 7. reps_v1
* The replicons identified as of June 19, 2024.



### 6. temp_files
  #### (a) cds_blasts_done.pkl
  * Created in **addgene replication extraction blast.ipynb**
  * Contains the top 10 blastx result (descriptions and protein sequences) for all the unique cds feature labels we have in our dataset.
  #### (b) cds_dict
  * Created in **addgene replication extraction blast.ipynb**


