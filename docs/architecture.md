# Architecture

The app is a dependency-free static site. `index.html` provides accessible structure, `assets/styles.css` provides the responsive visual layer, and `assets/app.js` fetches `data/tasks.json`, filters tasks, and stores completion identifiers in browser localStorage. Python standard-library scripts validate data, tests, and internal Markdown links.
