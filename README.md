# ercot-lmp-fuzzymatch

This repository utilizes three files from ERCOT's market participant website page. Settlement points, NOIE, and MORA files are fuzzy matched with existing node names from prism and returns one file with match scores. This file can then be filtered for matches above a certain threshold to complete the remaining nodes to be mapped. 

https://www.ercot.com/mp/data-products/data-product-details?id=NP4-160-SG
- Settlement_Points & NOIE_Mapping files can be found in this link 

https://www.ercot.com/gridinfo/resource
- MORA Sheet is found here 

Potential future improvement could be to have an importer/scraper that is automatically pulling these files from ERCOT 

