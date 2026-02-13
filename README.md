# My Eternal Love for Chomzy

This is a personalized Valentine's Day web page created for Chomzy.

## How to Customize

1. **Images and Videos**: Open `index.html` and look for the `--- CUSTOMIZATION SECTION ---` in the `<script>` tag at the bottom of the file.
   - You will see a `mediaItems` array.
   - To add an image: `{ type: 'image', url: 'YOUR_IMAGE_URL', caption: 'YOUR_CAPTION' }`
   - To add a video: `{ type: 'video', url: 'YOUR_VIDEO_URL', caption: 'YOUR_CAPTION' }`
   - Replace the placeholder URLs with your own photos and videos.
2. **Text**: You can easily change the name "Chomzy" or the romantic message by searching for them in the `index.html` file.
3. **Animations**: The page uses AOS (Animate On Scroll) and floating heart animations. You can adjust the frequency of hearts in the `createHeart` function.

## How to Host

### Option 1: GitHub Pages (Recommended & Free)
1. Create a new repository on GitHub.
2. Upload the `index.html` file to the repository.
3. Go to **Settings** > **Pages**.
4. Under "Build and deployment", select the `main` branch and click **Save**.
5. Your site will be live at `https://<your-username>.github.io/<repository-name>/`.

### Option 2: Netlify (Drag and Drop)
1. Go to [Netlify](https://www.netlify.com/).
2. Drag and drop the folder containing your `index.html` into the Netlify upload area.
3. Your site will be deployed instantly with a custom URL.

### Option 3: Local Server
If you just want to show it on your computer:
- Open the `index.html` file directly in any web browser.
- Alternatively, run a simple server using Python: `python3 -m http.server 8000` and visit `http://localhost:8000`.

Happy Valentine's Day! ❤️
