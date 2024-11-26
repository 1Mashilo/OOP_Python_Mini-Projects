## Photo Sharing App System Design

### Components:

1. **User Interface (UI):**
   - **CameraScreen:** Allows users to interact with the camera, start and stop capturing images.
   - **ImageScreen:** Displays the captured image and provides options for generating and sharing links.
   - **RootWidget:** Manages the navigation between different screens using the ScreenManager.
   
2. **FileSharer Class:**
   - **Functionality:** Handles uploading images to the web and generating shareable links using the Filestack library.
   - **Attributes:** Holds the file path and API key for Filestack.

3. **App Core:**
   - **MainApp:** Initializes and runs the Kivy application, instantiates the RootWidget.

### Flow:

1. The user launches the app, which triggers the MainApp's build() method.
2. The RootWidget screen manager is created, containing the CameraScreen and ImageScreen.
3. In the CameraScreen:
   - The user can start the camera, which makes the camera view visible and changes the button text.
   - The user can capture an image, which triggers the capture() method.
   - The captured image is saved using a filename based on the current time.
   - The user is navigated to the ImageScreen, where the captured image is displayed.
   
4. In the ImageScreen:
   - The user can create a shareable link by clicking the "Create Link" button.
   - The FileSharer class is used to upload the image to the web using the Filestack API.
   - The generated link is displayed in the Label widget.
   - The user can copy the link to the clipboard by clicking the "Copy Link" button.
   - The user can open the link in their default web browser by clicking the "Open Link" button.
   
### Technologies Used:

- **Kivy Framework:** Used for building the user interface and managing screen navigation.
- **Python:** Programming language used for app logic and functionality.
- **Filestack:** External library for uploading images to the web and generating shareable links.
- **Time Module:** Used to create timestamps for image filenames.
- **Webbrowser Module:** Allows opening links in the default web browser.
- **Clipboard Module:** Enables copying links to the clipboard.

### Benefits and Future Enhancements:

The Photo Sharing App offers users a convenient way to capture, share, and manage images. Its user-friendly interface and integration with Filestack streamline the sharing process. Some potential future enhancements could include implementing user authentication for private sharing, expanding the app to include video sharing, and optimizing for various device resolutions.

This system design illustrates the interaction between components and the technologies used to develop the Photo Sharing App. It highlights the app's functionalities and how users can interact with its features.