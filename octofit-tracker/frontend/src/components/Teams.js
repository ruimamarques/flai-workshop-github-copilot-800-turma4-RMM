import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Fetching teams from:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        console.log('Teams response status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams data received:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Processed teams data:', teamsData);
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
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
          <p className="mt-3 text-muted">Loading teams...</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">Error!</h4>
          <p>Unable to load teams: {error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="page-header mb-4">
        <h1>Teams</h1>
        <p className="lead text-muted">Create and join fitness teams</p>
      </div>
      
      {teams.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle"></i> No teams found.
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover table-bordered align-middle">
            <thead className="table-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Description</th>
                <th scope="col">Members</th>
                <th scope="col">Created</th>
              </tr>
            </thead>
            <tbody>
              {teams.map(team => (
                <tr key={team.id}>
                  <td><span className="badge bg-secondary">{team.id}</span></td>
                  <td><strong>{team.name}</strong></td>
                  <td>{team.description}</td>
                  <td><span className="badge bg-primary">{team.member_count || team.members?.length || 0}</span></td>
                  <td>{new Date(team.created_at).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <div className="text-muted small mt-2">
            Total teams: <strong>{teams.length}</strong>
          </div>
        </div>
      )}
    </div>
  );
}

export default Teams;
