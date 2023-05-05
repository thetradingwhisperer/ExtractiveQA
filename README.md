# ExtractiveQA
Repo to create a streamlit app to do extrative QA on documents.

This application utilizes the Haystack library to perform extractive question answering on PDF documents specifically tailored for the oil and gas industry. The app aims to streamline the process of extracting valuable insights from large volumes of technical and regulatory documents to support decision-making and problem-solving in the industry.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Features
- Supports PDF document input
- Extractive question answering on industry-specific documents
- Built using the Haystack library for efficient information retrieval

## Requirements
- Python 3.7+
- Haystack library

## Installation
1. Clone the repository:
```bash
git clone https://github.com/username/oil-gas-qa-app.git
cd oil-gas-qa-app
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Download and set up the required pre-trained models and document stores. Refer to the Haystack [documentation](https://haystack.deepset.ai/docs/intromd) for detailed instructions.

## Usage
1. Add your PDF documents to the `documents` folder.

2. Index your documents:
```bash
python index_documents.py
```

3. Run the app:
```bash
python app.py
```

4. Open a web browser and navigate to `http://localhost:5000` to access the user interface.

5. Type your question into the search bar and click "Ask" to retrieve relevant answers from the indexed documents.

## Contribution
We welcome contributions to improve this app. Please submit issues and pull requests on the GitHub repository. When submitting a pull request, make sure to follow the existing code style and provide a clear description of your changes.

## License
This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.
