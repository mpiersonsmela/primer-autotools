import sys

import webbrowser
browser = webbrowser.get('firefox')

import pandas as pd
genes = pd.read_csv("genemap.tsv", sep = '\t')

def get_transcript(genes, target):
    transcripts = genes[genes['Gene name'] == target]['RefSeq mRNA ID']
    #Choose the lowest mRNA ID
    lowest = float("Inf")
    lowest_transcript = ""
    for transcript in transcripts:
        num = int(transcript.split("_")[1])
        if num < lowest:
            lowest = num
            lowest_transcript = transcript
        
    return lowest_transcript

target = sys.argv[1]
transcript = get_transcript(genes, target)

base_website = "https://www.ncbi.nlm.nih.gov/tools/primer-blast/primertool.cgi?INPUT_SEQUENCE="

param_string = "&PRIMER_PRODUCT_MIN=70&PRIMER_PRODUCT_MAX=150&PRIMER_NUM_RETURN=10&PRIMER_ON_SPLICE_SITE=1&SEARCH_SPECIFIC_PRIMER=on&ORGANISM=Homo%20sapiens&PRIMER_SPECIFICITY_DATABASE=refseq_mrna&TOTAL_PRIMER_SPECIFICITY_MISMATCH=1&PRIMER_3END_SPECIFICITY_MISMATCH=1&MISMATCH_REGION_LENGTH=5&TOTAL_MISMATCH_IGNORE=6&MAX_TARGET_SIZE=2000&ALLOW_TRANSCRIPT_VARIANTS=on&NEWWIN=off&NEWWIN=off&SHOW_SVIEWER=true"

full_url = base_website + transcript + param_string

print("Opening:\n"+full_url)

browser.open(full_url)
