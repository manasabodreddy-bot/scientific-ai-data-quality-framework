# Scientific AI Data Quality & Evaluation Framework

A reproducible framework for evaluating chemical and biomedical
scientific data quality and AI-generated scientific claims using
authoritative databases, ontology-aware validation, and
rule-based evaluation.

## Project Status

In development.

## Objective

The project explores how scientific AI outputs can be evaluated
against structured reference data and authoritative scientific
sources.

The framework focuses on:

- scientific data quality
- chemical and biomedical entity resolution
- structured scientific claim validation
- ontology-aware validation
- API-based reference data retrieval
- evidence verification
- AI-generated scientific claim evaluation
- error classification
- root-cause analysis
- reproducible reporting

## Data Sources

The project uses authoritative scientific resources including:

- PubChem
- ChEMBL
- ChEBI

## Evaluation Approach

The project uses a primarily rule-based, agent-style evaluation
pipeline.

The workflow is designed to resemble a tool-assisted scientific
AI evaluation process:

1. Identify the scientific entity
2. Retrieve reference information
3. Identify claims in an AI-generated response
4. Compare structured claims with reference records
5. Evaluate evidence support
6. Classify errors
7. Assign severity
8. Recommend remediation
9. Report evaluation results

## Important Scope Limitation

This project does not implement a fully autonomous AI agent.

The term "agent-style evaluation pipeline" refers to the
sequential, tool-assisted evaluation workflow.

## Data Quality Principles

The project emphasizes:

- source provenance
- reproducibility
- entity identity
- data consistency
- evidence traceability
- explicit uncertainty
- conservative interpretation

Ontology classes and relationships are not invented manually.
Ontology information is derived from authoritative ontology
sources.

Scientific relationships are retained with their source
information.

## Project Status

Results, statistics, and performance measurements will only be
reported after they have been actually measured.

Recommended remediation steps will be clearly distinguished from
implemented fixes.

## Limitations

This is an independent portfolio project and is not intended to
represent a production-scale scientific data platform.
