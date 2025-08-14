# Quotation Generator

This project is a Streamlit application that allows users to generate quotations based on client information and selected concepts. The generated quotations can be saved as PDFs and stored in a Supabase database for easy retrieval.

## Features

- User input for client information
- Selection of concepts from a predefined list
- Generation of PDF quotations
- Storage of quotations in a Supabase database

## Project Structure

```
quotation-generator
├── src
│   ├── stream.py                # Main entry point of the Streamlit application
│   ├── components
│   │   └── __init__.py          # Initializes the components package
│   ├── services
│   │   └── supabase_service.py   # Functions to interact with Supabase
│   ├── utils
│   │   └── pdf_generator.py      # Functions to generate PDF quotations
│   └── data
│       └── concepts.py          # Predefined list of concepts for quotations
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd quotation-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
streamlit run src/stream.py
```

Follow the on-screen instructions to input client information, select concepts, and generate quotations.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.