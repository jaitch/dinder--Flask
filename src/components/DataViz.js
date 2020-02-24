import React, { Component } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import PropTypes from 'prop-types';
import axios from 'axios';
import NetworkGraph from './NetworkGraph'
import './DataViz.css'


class DataViz extends Component {
  constructor(props) {
    super(props);
    this.state = {
      soughtIngredient_name: '',
      graph_data: [],
      ing_found: false,
      error: '',
      y: .01,
    }
  }

  notify = () => toast("Sorry! Ingredient not found.");

  componentDidMount() {
  }

  onInputChange = (event) => {
    this.setState({
      soughtIngredient_name: event.target.value
    });
    console.log(`updated! looking for: ${this.state.soughtIngredient_name}`)
  }

  onSubmit = (event) => {
    event.preventDefault();
    let soughtIngredient = this.state.soughtIngredient_name.toLowerCase()
    axios.get(`${this.props.url}/ingredient/${soughtIngredient}/${this.state.y}`)
      .then((response) => {
        console.log(response.data)
        // format for calling single ingredient: response.data.ing_data[0]
        if (response.data.ing_data.length > 0) {
          this.setState({
            graphData: response.data,
            ing_found: true,
            // soughtIngredient_name: '',
          });
        }
        else {
          this.notify()
        }
      })
      .catch((errors) => {
        this.setState({
          ing_found: false,
          error: errors.title,
        });
        console.log(`errors: ${errors}`)
      });
  }

  findNewSimilarities = (ingredient) => {
    axios.get(`${this.props.url}/ingredient/${ingredient}/${this.state.y}`)
    .then((response) => {
      console.log(response.data)
      this.setState({
        graphData: response.data,
        ing_found: true,
        soughtIngredient_name: ingredient,
      });
    })
    .catch((errors) => {
      this.setState({
        ing_found: false,
        error: errors.title
      });
      console.log(`errors: ${errors}`)
    });
  }

  changeStrength = (event) => {
    this.setState({
      y: event.target.value
    })
    console.log(`changed strength to ${this.state.y}`)
  }

  render() {

    return (
      <div>
        <form className="form" onSubmit={this.onSubmit}>
          <div className="search-area">
            <label className="text" htmlFor="text">What's Cookin'?</label>
          </div>
          <div className="search-box">
            <input
              type="text"
              placeholder="ingredient (singular)"
              // onFocus={this.placeholder}
              name="ingredient"
              onChange={this.onInputChange}
              value={this.state.soughtIngredient}
            />
          </div>
          <div>
            <input
              type = 'range'
              axis="y"
              value={this.state.y}
              max='.2'
              min='.01'
              step='.01'
              onMouseUp={this.onSubmit}
              onChange={this.changeStrength}
              className='slider'
            />
            <p>(adjust strength of match)</p>
            <input
              type="submit"
              value="Search"
              onClick={this.onSubmit}
              className="submit-btn"
            />
          </div>
        </form>
      <div>
        {(this.state.ing_found === true) &&
        <NetworkGraph
          data={this.state.graphData}
          findNewSimilaritiesCallback={this.findNewSimilarities}
          url={this.props.url}
        />
        }
      </div>
      <ToastContainer/>
    </div>
    )
  }
}

DataViz.propTypes = {
  url: PropTypes.string.isRequired,
};

export default DataViz;