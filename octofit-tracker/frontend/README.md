# OctoFit Tracker Frontend

This is the React frontend for the OctoFit Tracker fitness application.

## Features

- User management and profiles
- Activity logging and tracking
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- Running Django backend API on port 8000

## Setup

1. Install dependencies:
```bash
npm install
```

2. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update `REACT_APP_CODESPACE_NAME` with your GitHub Codespace name
   
   For example, if your codespace URL is:
   `https://musical-space-adventure-abc123.github.dev`
   
   Then set:
   ```
   REACT_APP_CODESPACE_NAME=musical-space-adventure-abc123
   ```

3. Start the development server:
```bash
npm start
```

The app will open at `http://localhost:3000`

## API Endpoints

The frontend connects to the following Django REST API endpoints:

- `/api/users/` - User profiles
- `/api/activities/` - Fitness activities
- `/api/teams/` - Team management
- `/api/leaderboard/` - Competition rankings
- `/api/workouts/` - Workout suggestions

All endpoints use HTTPS and point to:
`https://${REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/`

## Components

- **Users** - View and manage user profiles
- **Activities** - Log and track fitness activities
- **Teams** - Create and join fitness teams
- **Leaderboard** - View competition rankings
- **Workouts** - Get personalized workout suggestions

## Navigation

The app uses React Router for navigation. The navigation menu is displayed at the top of every page.

## Debugging

All components include console.log statements to help debug API calls:
- Check browser console for API URLs
- View response status codes
- See fetched data structures

## Technologies

- React 19
- React Router DOM 7
- Bootstrap 5
- Fetch API for HTTP requests

## Available Scripts

- `npm start` - Run development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm eject` - Eject from Create React App

