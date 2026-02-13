# Our Eternal Love Story - Valentine's Day Gift for Chomzy

A personalized, multi-stage interactive web page that tells the story of your love journey, from the first meeting at NYSC camp to your future plans together.

## Features
- **Narrative Journey:** 6 distinct stages chronicling your relationship milestones.
- **Interactive Unlock:** Chomzy can "unlock" the next chapter of your story by clicking a heart icon.
- **Progress Heart:** A romantic progress bar at the top shows how far she is in the journey.
- **Dramatic Surprise:** A final "Reveal" interaction that opens the memory slideshow and video.
- **Romantic Atmosphere:** Background music, floating hearts, and elegant animations (AOS & Swiper.js).
- **Secure Comment Section:** A place for her to leave a heartfelt response.

## How to Customize
1.  **Dates and Text:** Search for the `<section class="stage">` blocks in `index.html` to update the dates or story text.
2.  **Photos and Videos:** Find the `mediaItems` array in the `<script>` section at the bottom of the file. Replace the placeholder URLs with links to your own photos and videos.
3.  **Background Music:** Replace the `src` in the `<audio>` tag with a link to your favorite romantic song.
4.  **Names:** If you wish to change the name "Chomzy", search and replace it throughout the file.

## How to Host
### Option 1: GitHub Pages (Recommended)
1.  Create a new repository on GitHub.
2.  Upload `index.html` to the repository.
3.  Go to **Settings > Pages**.
4.  Select the **main** branch and click **Save**. Your site will be live at `https://yourusername.github.io/your-repo-name/`.

### Option 2: Vercel / Netlify
1.  Drag and drop the folder containing `index.html` onto the Vercel or Netlify dashboard.
2.  Follow the prompts to deploy.

## Technical Details
- **No Backend Required:** Works entirely in the browser.
- **Responsive:** Optimized for mobile phones, tablets, and desktops.
- **Dependencies:** Uses Google Fonts, AOS (Animate on Scroll), Swiper.js, and Font Awesome (all via CDN).

*Created with love for Chomzy.*
