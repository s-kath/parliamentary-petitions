# Parliamentary Petitions

This repository contains the datasets and code files for the paper "A cross-country comparison of parliamentary petitions:
what factors lead to success in gathering signatures?" by Shivashankari Kathirgamalingam and Eduardo G. Altmann 

## Data

### Petitions datasets
Petitions data were obtained from the following sites to create standardised, reformatted datasets:
-   [Australia](https://www.aph.gov.au/e-petitions): used under [CC BY-NC-ND 4.0 Deed | Attribution-NonCommercial-NoDerivs 4.0 International license](https://www.aph.gov.au/Help/Disclaimer_Privacy_Copyright#c)
-   [Canada](https://www.ourcommons.ca/petitions/en/Home/Index): provided under [Open Data initiative](https://www.ourcommons.ca/en/open-data#od)
-   [UK](https://petition.parliament.uk/): used under [Open Government Licence 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) - 'Contains public sector information licensed under the Open Government Licence v3.0.'
-   [Germany](https://epetitionen.bundestag.de/)

The full names of Australian and Canadian petition authors were removed from datasets and replaced with numeric IDs after the author gender classifications had been derived from author names. In Australia, the metadata theme field was created by extracting the minister portfolio name from petition response files and then performing standardising and cleaning steps to combine variations of the same portfolio name (e.g. 'attorney general' and 'ag' both become 'attorney general'). In Australia, Canada, and the UK, the keywords used in the burstiness analysis were identified by performing a search of each word in the lowercase combined text of each petition.

### Canada baby names
The Canada baby name collections were obtained from the following government sites:
-   [Ontario](https://data.ontario.ca/organization/public-and-business-service-delivery-and-procurement): used under the [Open Government License - Ontario 1.0](https://www.ontario.ca/page/open-government-licence-ontario). 
-   [Quebec](https://www.donneesquebec.ca/recherche/organization/rrq): used under [Creative Commons License CC BY 4.0 (Attribution)](https://www.donneesquebec.ca/licence/#cc-by).

As the baby name datasets have been updated since the time of analysis, please use the files provided in  `data/canada/author_analysis` when running the code files in this repo. The names data were processed and combined into two mutually exclusive male and female name collections by applying a series of filtering and comparative rules to the datasets. The datasets were also reshaped, and anonymising values were replaced with single average numbers to allow for name frequencies to be aggregated and averaged across all years (e.g. where the frequency for a name in a certain year was given as <5, this was replaced with 2). Data processing of the names is found in [`canada-baby-names-final`](gen-auth/canada-baby-names-final.ipynb). 

### Valence and Arousal lemmas
The dataset of valence and arousal information for 13,915 English lemmas was taken from ["Norms of valence, arousal, and dominance for 13,915 English lemmas"](https://link.springer.com/article/10.3758/s13428-012-0314-x) by Warriner et al. (2013). To run the textual features analysis, download the file `BRM-emot-submit.csv` from the supplementary material of this paper and put it in the `data` folder.

## Code Files
The code to generate the figures, tabular information, and statistical tests in the paper can be found in the `burstiness`, `rep-auth`, `signatures`, `temporal`,  `gen-auth`, and  `text-features` folders. The Jupyter Notebooks in the `burstiness`, `rep-auth`, `signatures`, `temporal`, and `text-features` folders can be run with the provided datasets in the `data` folder. 

In the `gen-auth` folder, the following Jupyter Notebooks _cannot_ be run because they rely on the non-anonymised data (containing petition author names), which is not provided here for privacy reasons: [`author-names-final`](gen-auth/author-names-final.ipynb) and [`creating-gender-classifications-final`](gen-auth/creating-gender-classifications-final.ipynb). These files have been included to illustrate the process of gender classification. 

## Figures

The figures that are included in the paper can be found in the `figures` folder.

## Credit
The signatures analysis builds on code from the [repository](https://github.com/edugalt/StatisticalLaws/tree/main) of ["Statistical Laws in Complex Systems: Combining Mechanistic Models and Data Analysis"](https://link.springer.com/book/10.1007/978-3-031-73164-8) by Eduardo G. Altmann (2024)
