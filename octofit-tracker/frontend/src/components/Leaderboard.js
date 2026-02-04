import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Fetching leaderboard from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        console.log('Leaderboard response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard data received:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Processed leaderboard data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
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
          <p className="mt-3 text-muted">Loading leaderboard...</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>Unable to load leaderboard: {error}</p>
        </div>
      </div>
    );
  }

  const getMedalEmoji = (rank) => {
    switch(rank) {
      case 1: return '🥇';
      case 2: return '🥈';
      case 3: return '🥉';
      default: return '';
    }
  };

  return (
    <div className="container mt-4">
      <div className="page-header mb-4">
        <h1>🏆 Leaderboard</h1>
        <p className="lead text-muted">See who's leading the competition</p>
      </div>
      
      {leaderboard.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle"></i> No leaderboard entries found.
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover table-bordered align-middle">
            <thead className="table-dark">
              <tr>
                <th scope="col">Rank</th>
                <th scope="col">User</th>
                <th scope="col">Team</th>
                <th scope="col">Points</th>
                <th scope="col">Activities</th>
                <th scope="col">Period</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, index) => {
                const rank = index + 1;
                const rowClass = rank <= 3 ? 'table-warning' : '';
                return (
                  <tr key={entry.id || index} className={rowClass}>
                    <td>
                      <strong>{getMedalEmoji(rank)} {rank}</strong>
                    </td>
                    <td><strong>{entry.user_name || entry.user}</strong></td>
                    <td>{entry.team_name || entry.team || 'N/A'}</td>
                    <td><span className="badge bg-success fs-6">{entry.total_points || entry.points}</span></td>
                    <td><span className="badge bg-info text-dark">{entry.activity_count || entry.activities || 0}</span></td>
                    <td>{entry.period || 'Overall'}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          <div className="text-muted small mt-2">
            Total entries: <strong>{leaderboard.length}</strong>
          </div>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
