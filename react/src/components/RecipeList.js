import React from 'react';
import {toast, ToastContainer} from 'react-toastify';
import PropTypes from 'prop-types';
import './RecipeList.css'

function RecipeList(props) {
  const no_recs = () => {
    toast("Sorry! No recipes found for that combination.")
  };
  const list = props.list
  const recipe_array = list["rec_data"].map(r => r["allData"])
  if (recipe_array.length === 0) {
    no_recs();
    return (
      <div>
        <ToastContainer/>
      </div>
    )
  }
  else {
    const recipe_list = recipe_array.map((rec) =>
      <li key={rec["_id"]}>
        <a href={rec['url']} target="_blank" rel="noopener noreferrer"> {rec["name"]} </a>
      </li>);

  return (
    <div>
      <h3 className='recipe-list-header'>RECIPES</h3>
      <ul className='recipe-list'>{recipe_list}</ul>
    </div>
  )}
}

RecipeList.propTypes = {
  list: PropTypes.Array
}

export default RecipeList