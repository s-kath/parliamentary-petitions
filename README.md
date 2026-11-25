# Parliamentary Petitions

This repository contains the datasets and code files for the paper "A cross-country comparison of parliamentary petitions:
what factors lead to success in gathering signatures?" by Shivashankari Kathirgamalingam and Eduardo G. Altmann 

## Data

### Petitions datasets
Petitions datasets were obtained from the following sites and combined into standardised, reformatted datasets:
-   Australia - https://www.aph.gov.au/e-petitions
-   Canada - https://www.ourcommons.ca/petitions/en/Home/Index
-   UK - https://petition.parliament.uk/
-   Germany - https://epetitionen.bundestag.de/

[DESCRIBE ACCESS PERMISSIONS]

The Australia and Canada datasets were anonymised through the use of numeric IDs after the author gender classifications had been derived from author names. In Australia, the metadata theme field was created by extracting and X. In Australia, Canada, and the UK, the keywords used in the burstiness analysis were identified by performing a search of each word in the lowercase combined text of each petition. 

### Canada baby names
The Canada baby name collections were obtained from the following government sites:
-   Ontario - https://data.ontario.ca/organization/public-and-business-service-delivery-and-procurement
-   Quebec - https://www.donneesquebec.ca/recherche/organization/rrq

[DESCRIBE ACCESS PERMISSIONS]


Data processing of the names is in the notebook `X-final.ipynb`

### Valence and Arousal lemmas
That valence and arousal lemmas dataset was...

[DESCRIBE ACCESS PERMISSIONS]

## Code Files
The code to generate the figures, tabular information, and statistical tests in the paper can be found in the `burstiness`, `rep-auth`, `signatures`, `temporal`,  `gen-auth`, and  `text-features` folders. The Jupyter notebooks in the `burstiness`, `rep-auth`, `signatures`, `temporal`, and `text-features` folders can be run with the provided datasets in the `data` folder. In the `gen-auth` folder, the following notebooks _cannot_ be run because they rely on data that has not been anonymised: X. These files have been included to illustrate the process of gender classification. 

## Credit
- Eduardo's code repo
- Clauset (?)
- AI credits?
