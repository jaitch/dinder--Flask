import React from 'react';
import PropTypes from 'prop-types';
import './RecipeSearch.css'

function RecipeSearch(props) {

  const onClickSearch = () => {
    props.recipeSearchCallback();
  }

  const ings = props.ings
  if (ings !== []) {
    const listItems = ings.map((ing) =>
      <li key={ing["id"]}>{ing["name"]}</li>);

    return(
      <div className='recipe-search-box'>
        <h3 className='instructions'>To matchmake another ingredient, click on the circle.</h3>
        <h3>To add an ingredient to the recipe search, click on the name.</h3>
        <ul className='list'>
          {listItems}
        </ul>
        <div>
          <input
            type="submit"
            value="Search"
            onClick={onClickSearch}
            className="recipe-submit-btn"
          />
          <input
            type="submit"
            value="Clear"
            onClick={() => props.onClickClearCallback()}
            className="recipe-clear-btn"
          />
        </div>
      </div>
    );
  }
}

RecipeSearch.propTypes = {
  ings: PropTypes.array,
  recipeSearchCallback: PropTypes.func,
  onClickClearCallback: PropTypes.func
}

export default RecipeSearch