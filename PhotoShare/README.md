# Photo Sharing App

The Photo Sharing App is a Kivy-based Python application that allows users to capture photos from their camera, upload them to the web, and share the generated link. The app offers a user-friendly interface with features like starting/stopping the camera, capturing images, generating sharable links, copying links to the clipboard, and opening links in the default browser. The following are the key components of the app:

## Components

### 1. **MainApp (main.py)**
- The entry point of the application.
- Creates and runs the Kivy app, presenting the GUI to the user.
- Utilizes the ScreenManager to manage and switch between different screens.

### 2. **CameraScreen**
- Inherits from the Screen class and represents the camera functionality.
- Starts and stops the camera.
- Captures and saves images with a timestamp as the filename.
- Switches to the ImageScreen after capturing an image to display it.

### 3. **ImageScreen**
- Inherits from the Screen class and handles image sharing and linking.
- Creates a sharable link for the captured image using the FileSharer class.
- Allows users to copy the link to the clipboard and open the link in the default browser.

### 4. **RootWidget**
- Inherits from the ScreenManager class.
- Acts as the root widget for the app's UI.

### 5. **FileSharer (filesharer.py)**
- A class responsible for uploading the image file to the web and generating a sharable link.
- Utilizes the Filestack library to handle the uploading process.
- Accepts the filepath and API key during initialization.

### 6. **frontend.kv**
- A Kivy language file that defines the app's user interface structure and interactions.
- Contains screen layouts, widgets, and their properties.

## Functionality

1. The CameraScreen provides options to start and stop the camera, capture images, and switch to the ImageScreen to display the captured image.
2. The ImageScreen offers the ability to create a sharable link for the captured image and provides options to copy the link to the clipboard or open it in the browser.

## Usage

1. Run the app using `MainApp().run()` in the `main.py` file.
2. The GUI will be presented to the user.
3. Start the camera to capture images, stop it when done.
4. After capturing, the user can create a sharable link, copy the link, and open it in the browser.

## Requirements

The app requires Kivy and the Filestack library. You can install the necessary dependencies using the provided `requirements.txt` file.

## Design and Screenshots

For the app's design and UI screenshots, refer to the included `design.txt` and `design-frontend.png` files.

The Photo Sharing App showcases Kivy-based development skills and demonstrates the ability to interact with external services for file sharing. It's a valuable addition to a programming portfolio, highlighting proficiency in creating interactive applications with user-friendly features.