import React, { Component } from 'react';
import logo from './pan-icon-3.png';
import DataViz from './components/DataViz';
import './App.css';

class App extends Component {
  constructor(props) {
    super();
    this.state = {
    }
  }

  render() {
    const BASE_URL = 'http://localhost:5000'
    // const BASE_URL = 'https://dinder-flask.herokuapp.com'

    return (
      <div className='App'>
        <header className='App-header'>
          <img src={logo} className='App-logo' alt="logo"/>
          <h1 className='App-title'>dinder</h1>
          <p className='App-subtitle'>The Ingredient Matchmaker</p>
        </header>
        <main className='App-body'>
          <DataViz url={BASE_URL}/>
        </main>
        <footer>
        </footer>
      </div>
    );
  }
}

export default App;
