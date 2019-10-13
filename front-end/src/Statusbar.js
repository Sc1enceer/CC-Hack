import React from 'react';
import Status from './Status';
import Graph from './Graph'
import {Grid, Typography} from '@material-ui/core'
import axios from 'axios'

class Statusbar extends React.Component {

  constructor(props){
    super(props);
    this.state = {currentItem:"", isToggleOn: false, list:["Sunlight", "Humidity", "Temperature", "Wind Speed"], values:''}
    this.getData();
    this.exceedThreshold = this.exceedThreshold.bind(this);

  }


  getData(){
    axios.get("http://127.0.0.1:5000/currentValues")
    .then(response => this.setState({'values' : response.data}))
  }

  handleClick(item) {
      this.setState(state => ({
        isToggleOn: "true"
      }));
      this.state.currentItem = item
  }

  exceedThreshold(item, value){
    if (item === "Humidity") {
      return (value >= 50 && value <= 70);
    }
    if (item === "Temperature") {
      return (value <= 25 && value >= 18)
    }
    if (item === "Wind Speed") {
      return (value <= 6)
    }
    else {
      return true;
    }
  }

  render(){
    let graph;
    if (this.state.currentItem != "") {
    graph = <Graph key={this.state.currentItem} item={this.state.currentItem}/>;
    }else {
      graph = <div></div>;
    }
    return (

      <Grid item xs={12}>
        <Grid container spacing = {3}>
        {this.state.list.map((item) =>
          <Grid item xs = {3} onClick={(e) => this.handleClick(item, e)}>
            <Status key={this.state.values} item={item} data={this.state.values[item]} exceedThreshold={this.exceedThreshold(item, this.state.values[item])}/>
          </Grid>
        )
        }
        </Grid>
        <Grid item xs = {12} onClick={(e) => this.handleClick("Spectrum", e)}>
          <Status key={this.state.currentItem} item="Spectrum"/>
        </Grid>
        <br/>
        <Grid item xs = {12} >
          {graph}
        </Grid>
      </Grid>

    );
  }



}

export default Statusbar;
