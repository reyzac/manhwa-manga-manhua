# Manhwa, Manga & Manhua Recommendations

## Overview
A web-based repository showcasing manhwa, manga, and manhua recommendations with personal comments and reviews. The project transforms the original documentation repository into an interactive web interface.

## Project Structure
- `index.html` - Main HTML page displaying reading lists
- `style.css` - Styling with gradient purple theme and responsive design
- `server.py` - Python HTTP server serving static content on port 5000
- `README.md` - Project documentation
- `LICENSE` - MIT License

## Architecture
- **Frontend**: Dynamic HTML/CSS website with Flask templating
- **Backend**: Flask (Python) server processing JSON data with Pandas
- **Deployment**: Configured as Autoscale deployment (dynamic)

## Recent Changes
- **2025-11-20**: Initial setup in Replit environment
- **2025-11-21**: Switched to Autoscale deployment to support Flask backend and data processing

## Current State
The application is fully functional and ready to use. Users can:
- View the recommendation website with organized sections
- Add their own manhwa/manga/manhua titles to the HTML
- Track reading status (Currently Reading, Completed, Plan to Read)

## Future Enhancements
- Add dynamic content management (JavaScript)
- Implement search/filter functionality
- Add rating system for titles
- Include cover images for each title
- Create backend API for data persistence
