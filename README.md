# SavePageNow CLI

SavePageNow CLI is for turning [savepagenow](https://github.com/palewire/savepagenow) into a standalone binary.

## Requirements

- Python 3.6 or higher
- `pip` (Python package installer)

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/nickali/savepagenow-cli.git
   cd savepagenow-cli
   ```

2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Script

You can run the script directly using Python:

```sh
python savepagenow_cli.py https://example.com/
```

### Compiling to a Standalone Executable

To compile the script into a standalone executable, follow these steps:

1. **Install PyInstaller**:
   ```sh
   pip install pyinstaller
   ```

2. **Generate the Executable**:
   ```sh
   pyinstaller --onefile savepagenow_cli.py
   ```

3. **Locate the Executable**:
   The executable will be located in the `dist` directory:
   ```sh
   dist/savepagenow_cli
   ```

### Running the Standalone Executable

You can run the standalone executable as follows:

```sh
./dist/savepagenow_cli https://example.com/
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
