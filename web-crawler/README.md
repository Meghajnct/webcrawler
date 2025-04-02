Prerequisites:
    1. Install Selenium:
        pip install selenium
        pip install selenium playsound
    2.Download the appropriate WebDriver for your browser:
        ChromeDriver 
        GeckoDriver (Firefox)
    3. Get a sound file (e.g., alert.mp3) and place it in the same directory as the script.

You can download ChromeDriver from the official Chrome WebDriver site:  

🔗 **[ChromeDriver Download Page](https://sites.google.com/chromium.org/driver/)**  

### **Steps to Download and Set Up ChromeDriver**  
1. **Check your Chrome version**  
   - Open Chrome and go to:  
     ```
     chrome://settings/help
     ```
   - Note the version number (e.g., **Version 122.0.0.0**).  

2. **Download the matching ChromeDriver**  
   - Go to the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).  
   - Find the **version matching your Chrome browser**.  
   - Download the appropriate **zip file** for your operating system (**Windows/Mac/Linux**).  

3. **Extract and Place the WebDriver**  
   - Extract the downloaded `chromedriver.exe` (Windows) or `chromedriver` (Mac/Linux).  
   - Move it to a known directory (e.g., `C:\chromedriver\` or `/usr/local/bin/`).  

4. **Add ChromeDriver to PATH (Optional but Recommended)**  
   - On **Windows**:  
     - Add `C:\chromedriver\` to your **System Environment Variables** under `Path`.  
   - On **Mac/Linux**:  
     - Move the file to `/usr/local/bin/` or use:  
       ```sh
       export PATH=$PATH:/path/to/chromedriver
       ```

Now, you can run Selenium without specifying the WebDriver path manually! 🚀  

Would you like a guide on automating login for the **DVSA booking site** as well? 😊