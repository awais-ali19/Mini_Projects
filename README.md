# Awesome Streamlit Mini-Projects Collection ✨

This repository is a collection of three interactive mini-projects built with Streamlit, a powerful Python library for creating web applications for data science and machine learning. Each project demonstrates a different aspect of Streamlit's capabilities, from handling user input to interactive visualization.

### 1. URL Shortener 🔗
A simple and fast web application that takes a long URL and generates a unique, shorter version. This project is a great example of input processing and data transformation.

Purpose: To convert unwieldy, long URLs into compact and easy-to-share links.

Technologies: Streamlit, Python's built-in string manipulation.

### 2. Image Editor 🖼️
An interactive tool to apply basic editing filters to uploaded images. This project showcases how to handle file uploads and integrate other Python libraries for image processing.

Purpose: To perform simple, real-time image manipulations directly in a web browser.

Technologies: Streamlit, Pillow (PIL).

### 3. Paragraph Density Checker 📝
A fun and insightful app that calculates the "density" of a paragraph based on its unique word count relative to its total word count. This project is a neat example of text analysis and data summary.

Purpose: To analyze a block of text and provide key metrics about its content density.

Technologies: Streamlit, Python's built-in dictionary and list operations , Re module.

## How to Run the Projects 🚀

To run these projects locally, you need to have Python and pip installed.

### Clone the Repository:

```Bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Install Dependencies:
You'll need Streamlit and any other project-specific libraries.

```Bash
pip install streamlit Pillow
```
Note: Pillow is a dependency for the Image Editor project.

### Run the Apps:
To launch any of the projects, use the streamlit run command followed by the project's file name.

For the URL Shortener:

```Bash
streamlit run url_shortener.py
```
For the Image Editor:

```Bash
streamlit run image_editor.py
```
For the Density Checker:

```Bash
streamlit run density_checker.py
```
After running the command, your web browser will automatically open a new tab with the application.
