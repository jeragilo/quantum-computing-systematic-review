# Supporting aggregate data for a cross-domain quantum computing review

**GitHub release candidate — limited supporting aggregates.**

Associated manuscript: *From Quantum Possibility to Quantum Utility: A Cross-Domain Systematic Review and Six-Level Evidence Framework* (Jesus Rafael Gil Lopez and Nasseh Tabrizi).

## Contents
- `data/domain_year_counts.csv`: aggregated annual counts for eight overlapping Scopus search domains (QC01–QC08), totaling 1,172 **search occurrences**, not unique studies.
- `verification/figure2a_verification.csv`: comparison against the manuscript's Figure 2(a) values.
- `code/reproduce_domain_trends.py`: **reconstructed** script to regenerate annual counts from the authors' private source workbook. It is not the original analysis code and cannot run without that private workbook.
- `DATA_DICTIONARY.md`: field descriptions.

## Scope and limitations
This deposit would support only the domain/year aggregate analysis (Figure 2(a)). It does **not** provide the 778-record deduplicated inventory, 349-review selection decisions, methodology classifications (Figure 2(b)), country analysis (Figure 2(c)), or thematic synthesis. The original Scopus exports and private master workbook are not included. The data were generated from a working workbook; the authors' previously finalized screening corrections are not reconstructed here. Do not infer full-paper reproducibility from this subset.

## Reproduction
Run `python code/reproduce_domain_trends.py /path/to/private_master.xlsx`. The script writes `code/domain_year_counts.csv`; compare it with the packaged `data/domain_year_counts.csv`. Python 3 standard library is sufficient.

## Sharing and citation
This repository provides only aggregate Figure 2(a) data and a reconstructed reproduction script. It does not claim to reproduce the full systematic review. The private workbook and Scopus record-level content are not distributed. Repository maintainers should confirm coauthor approval and appropriate rights before making the repository public. Cite the stable GitHub release URL or commit permalink in the manuscript; GitHub alone does not automatically provide a DOI.

