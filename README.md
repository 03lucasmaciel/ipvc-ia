<a id="readme-top"></a>

<br />
<div align="center">
	<a href="https://www.ipvc.pt">
		<img src="week-0/assets/logo_ipvc_svg2-sunrise.svg" alt="IPVC Logo" width="600">
	</a>
	<h3 align="center">IPVC Artificial Intelligence Coursework Repository</h3>
	<p align="center">
		A centralized repository for all practical assignments developed in the Artificial Intelligence course
		of the Computer Engineering degree at IPVC.
		<br />
		<a href="https://github.com/03lucasmaciel/ipvc-ia"><strong>Explore the repository »</strong></a>
	</p>
</div>

<details>
	<summary>Table of Contents</summary>
	<ol>
		<li><a href="#about-the-repository">About The Repository</a></li>
		<li><a href="#goals">Goals</a></li>
		<li><a href="#repository-structure">Repository Structure</a></li>
		<li><a href="#coursework-index">Coursework Index</a></li>
		<li><a href="#technologies-used">Technologies Used</a></li>
		<li><a href="#how-to-use">How to Use</a></li>
		<li><a href="#evaluation-workflow">Evaluation Workflow</a></li>
	</ol>
</details>

## About The Repository

This repository gathers the coursework developed for the **Artificial Intelligence** course in the
**Computer Engineering** program at **IPVC (Instituto Politecnico de Viana do Castelo)**.

It is organized to keep assignments, support files, and submission-ready code in a single, clear structure,
making it easier to study progress across the semester and maintain reproducible results.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Goals

- Document all AI practical work in one place
- Keep each assignment reproducible and easy to validate
- Separate experimentation code from final submission files
- Maintain a clear historical record of improvements over time

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Repository Structure

```text
ipvc-ia/
├── week-0/
│   ├── README.md
│   ├── TEMPLATE.md
│   ├── docs/
│   ├── src/
│   ├── submissions/
│   └── tests/
├── LICENSE
└── README.md
```

### Folder conventions

- `docs/`: assignment statements, reference PDFs, and supporting documentation
- `src/`: implementation and experimentation code
- `submissions/`: final files prepared for formal submission
- `tests/`: validation or automated checks for assignment requirements

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Coursework Index

### Week 0

- Topic: Uninformed search in the 8-puzzle problem
- Main algorithms: BFS, DFS, UCS
- Focus: solution quality, path cost, and frontier memory usage
- Assignment details: [week-0/README.md](week-0/README.md)
- Submission file: [week-0/submissions/exsps_27712.py](week-0/submissions/exsps_27712.py)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Technologies Used

- Python 3
- Standard library modules (`heapq`, `collections.deque`, and related built-ins)
- Git and GitHub for version control and progress tracking

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How to Use

1. Clone the repository:

   ```sh
   git clone https://github.com/03lucasmaciel/ipvc-ia.git
   ```

2. Enter the project folder:

   ```sh
   cd ipvc-ia
   ```

3. Open a specific assignment folder (example: week 0):

   ```sh
   cd week-0
   ```

4. Read the assignment context:
   - [week-0/README.md](week-0/README.md)

5. Run submission validation when available:

   ```sh
   cd submissions
   python validate.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Evaluation Workflow

For each assignment, the standard workflow is:

1. Read the assignment statement in `docs/`
2. Implement and test in `src/`
3. Prepare the required deliverable in `submissions/`
4. Validate format and behavior before final submission

This approach helps ensure submission files comply with naming, interface, and output constraints required by the course.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
