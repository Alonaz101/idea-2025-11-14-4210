import React, { useState, useEffect } from 'react';

function App() {
  const [mood, setMood] = useState('');
  const [recipes, setRecipes] = useState([]);
  const [favorites, setFavorites] = useState([]);

  const fetchRecipes = async (mood) => {
    if (!mood) return;
    const res = await fetch(`/api/recipes?mood=${mood}`);
    const data = await res.json();
    setRecipes(data.recipes);
  };

  const addFavorite = async (recipeId) => {
    await fetch(`/api/favorites`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ recipe_id: recipeId })
    });
    setFavorites([...favorites, recipeId]);
  };

  const handleMoodChange = (e) => {
    setMood(e.target.value);
  };

  const handleMoodSubmit = () => {
    fetchRecipes(mood);
  };

  return (
    <div className="App">
      <h1>Mood-Based Recipe Recommendation</h1>
      <input placeholder="Enter your mood" value={mood} onChange={handleMoodChange} />
      <button onClick={handleMoodSubmit}>Get Recipes</button>
      <h2>Recipes</h2>
      <ul>
        {recipes.map(r => (
          <li key={r.recipe_id}>
            {r.title}
            <button onClick={() => addFavorite(r.recipe_id)}>Favorite</button>
          </li>
        ))}
      </ul>
      <h2>Your Favorites</h2>
      <ul>
        {favorites.map(fav => <li key={fav}>{fav}</li>)}
      </ul>
    </div>
  );
}

export default App;
