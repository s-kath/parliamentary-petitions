# Parliamentary Petitions

This repository contains the datasets and code files for the paper "A cross-country comparison of parliamentary petitions:
what factors lead to success in gathering signatures?" by Shivashankari Kathirgamalingam and Eduardo G. Altmann 

## Data

### Petitions datasets
Petitions datasets were obtained from the following sites and combined into standardised, reformatted datasets:
-   [Australia](https://www.aph.gov.au/e-petitions). Use governed by X
-   [Canada](https://www.ourcommons.ca/petitions/en/Home/Index). Use governed by X
-   [UK](https://petition.parliament.uk/). Use governed by X
-   [Germany](https://epetitionen.bundestag.de/)

The full names of Australia and Canada authors were removed from datasets and replaced with numeric IDs after the author gender classifications had been derived from author names. In Australia, the metadata theme field was created by extracting the minister portfolio name from petition response files and then performing standardising and cleaning to combine variations of the same portfolio name (e.g. 'attorney general' and 'ag' both become 'attorney general'). In Australia, Canada, and the UK, the keywords used in the burstiness analysis were identified by performing a search of each word in the lowercase combined text of each petition.

### Canada baby names
The Canada baby name collections were obtained from the following government sites:
-   [Ontario](https://data.ontario.ca/organization/public-and-business-service-delivery-and-procurement). Use permitted under the [Open Government License - Ontario](https://www.ontario.ca/page/open-government-licence-ontario). 
-   [Quebec](https://www.donneesquebec.ca/recherche/organization/rrq). Use permitted under [Creative Commons License CC BY 4.0 (Attribution)](https://www.donneesquebec.ca/licence/#cc-by).

As the baby name datasets have been updated since the time of analysis, please use the files provided in  `data/canada/author_analysis` when running the code files in this repo. The names datasets were processed and combined into two mutually exclusive male and female name collections by applying a series of filtering and comparative rules to the datasets. The datasets were also reshaped, and anonymising values were replaced with single average numbers to allow for name frequencies to be aggregated and averaged across all years (e.g. where the frequency for a name in a certain year was given as `<5`, this was replaced with 2.5). Data processing of the names is found in: `\gen-auth\canada-baby-names-final.ipynb`. 

### Valence and Arousal lemmas
The dataset of valence and arousal information for 13,915 English lemmas was taken from [Warriner et al. (2013)](doi:10.3758/s13428-012-0314-x). To run the textual features analysis, download the file `BRM-emot-submit.csv` from the supplementary material of this paper and put it in the `data` folder.

## Code Files
The code to generate the figures, tabular information, and statistical tests in the paper can be found in the `burstiness`, `rep-auth`, `signatures`, `temporal`,  `gen-auth`, and  `text-features` folders. The Jupyter notebooks in the `burstiness`, `rep-auth`, `signatures`, `temporal`, and `text-features` folders can be run with the provided datasets in the `data` folder. In the `gen-auth` folder, the following notebooks _cannot_ be run because they rely on data that has not been anonymised: X. These files have been included to illustrate the process of gender classification. 

## Credit
- Eduardo's code repo
- Clauset (?)
- AI credits?
