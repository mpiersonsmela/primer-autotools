# primer-autotools
Automatically query NCBI for qPCR primers. Basically you give it a gene symbol (e.g. GATA4) and it automatically opens Primer-BLAST on NCBI with the correct parameters set for qPCR. Parameters are customizable by changing the "param_string" in qPCR_autotool.py

Usage:
`python3 qPCR_autotool.py [gene symbol]`

The mapping from gene symbol to RefSeq ID is provided in `genemap.tsv` (which was the result of a BioMart query; up to date as of September 2021). If there are multiple possible RefSeq IDs, by default the lowest one is chosen.
