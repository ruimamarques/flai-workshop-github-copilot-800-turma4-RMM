import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Fetching workouts from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        console.log('Workouts response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts data received:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Processed workouts data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="container mt-4">
        <div className="text-center py-5">
          <div className="spinner-border text-primary" role="status" style={{width: '3rem', height: '3rem'}}>
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3 text-muted">Loading workouts...</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>Unable to load workouts: {error}</p>
        </div>
      </div>
    );
  }

  const getDifficultyBadge = (level) => {
    const badges = {
      'Beginner': 'success',
      'Intermediate': 'warning',
      'Advanced': 'danger'
    };
    return badges[level] || 'secondary';
  };

  return (
    <div className="container mt-4">
      <div className="page-header mb-4">
        <h1>💪 Workout Suggestions</h1>
        <p className="lead text-muted">Personalized workout plans to achieve your fitness goals</p>
      </div>
      
      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle"></i> No workout suggestions available.
        </div>
      ) : (
        <>
          <div className="row">
            {workouts.map(workout => (
              <div key={workout.id} className="col-md-6 col-lg-4 mb-4">
                <div className="card h-100 shadow-sm">
                  <div className="card-header bg-primary text-white">
                    <h5 className="card-title mb-0">{workout.name}</h5>
                  </div>
                  <div className="card-body">
                    <p className="card-text text-muted">{workout.description}</p>
                    <hr />
                    <div className="d-flex justify-content-between align-items-center mb-2">
                      <span className="text-muted"><strong>Type:</strong></span>
                      <span className="badge bg-info text-dark">{workout.workout_type}</span>
                    </div>
                    <div className="d-flex justify-content-between align-items-center mb-2">
                      <span className="text-muted"><strong>Duration:</strong></span>
                      <span className="badge bg-secondary">{workout.duration} min</span>
                    </div>
                    <div className="d-flex justify-content-between align-items-center mb-2">
                      <span className="text-muted"><strong>Difficulty:</strong></span>
                      <span className={`badge bg-${getDifficultyBadge(workout.difficulty_level)}`}>
                        {workout.difficulty_level}
                      </span>
                    </div>
                    <div className="d-flex justify-content-between align-items-center">
                      <span className="text-muted"><strong>Calories:</strong></span>
                      <span className="badge bg-success">{workout.calories_estimate} kcal</span>
                    </div>
                  </div>
                  <div className="card-footer text-center bg-light">
                    <button className="btn btn-primary btn-sm">Start Workout</button>
                  </div>
                </div>
              </div>
            ))}
          </div>
          <div className="text-muted small mt-2">
            Total workout plans: <strong>{workouts.length}</strong>
          </div>
        </>
      )}
    </div>
  );
}

export default Workouts;
