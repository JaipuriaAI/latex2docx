<img width="553" alt="Screenshot 2025-02-18 at 12 20 27 PM" src="https://github.com/user-attachments/assets/27ffdf15-d3c5-45c7-b320-294bb3d82b73" />


### README.md for LaTeX to Word Converter Extension

#### Overview
The LaTeX to Word Converter is a Chrome extension that allows users to convert LaTeX code into Word documents (.docx) seamlessly. This tool is particularly useful for academics, researchers, and anyone who frequently works with LaTeX documents and needs an easy way to convert them into a more universally accessible format.

#### Features
- **Simple Interface**: A user-friendly interface that allows for easy input of LaTeX code and a single button to convert it to a Word document.
- **Instant Download**: Converts and downloads the Word document directly through the browser.
- **Secure**: Utilizes environment variables and CORS to ensure secure and flexible API communication.

#### Components
1. **Frontend**: A Chrome extension that provides the user interface.
2. **Backend**: A server hosted on Render that handles the conversion from LaTeX to Word using Pandoc.

#### Installation and Usage
##### Chrome Extension
1. **Installation**:
   - Visit the Chrome Web Store at [LaTeX to Word Converter](https://chromewebstore.google.com/detail/latex-to-word-converter-b/ojakplemjejkpjigdlbmplkmamaadeod?authuser=0&hl=en).
   - Click on "Add to Chrome" to install the extension.

2. **Usage**:
   - Click on the extension icon in the Chrome toolbar.
   - Enter your LaTeX code into the textarea provided.
   - Click the "Convert to Word" button.
   - The .docx file will be automatically downloaded to your computer.

##### Backend Server
The server is hosted on Render and is responsible for the actual conversion process. It is not necessary to manually set up the server for general use of the extension, as it communicates with the already deployed server.

#### Development
##### Prerequisites
- Docker
- Python 3.11
- Node.js and npm

##### Local Setup
1. **Server**:
   - Navigate to the server directory.
   - Build the Docker image:
     ```bash
     docker build -t latex-to-word-converter .
     ```
   - Run the Docker container:
     ```bash
     docker run -p 80:80 latex-to-word-converter
     ```

2. **Extension**:
   - Load the extension locally in Chrome:
     - Open Chrome and navigate to `chrome://extensions/`
     - Enable Developer Mode.
     - Click "Load unpacked" and select the extension directory.

#### Contributing
Contributions are welcome! Please fork the repository and submit pull requests with your proposed changes.

#### License
This project is licensed under the MIT License - see the LICENSE file for details.

#### Support
For support, feature requests, or bug reports, please file an issue through the GitHub repository issue tracker.

This README provides a comprehensive guide to both using and contributing to the LaTeX to Word Converter project. For any further details or specific queries, refer to the GitHub repository or contact the project maintainers.
