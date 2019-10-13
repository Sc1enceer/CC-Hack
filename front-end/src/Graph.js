import React from 'react';
import {ResponsiveLine} from '@nivo/line';
import axios from 'axios'
import {Container} from '@material-ui/core'

class Graph extends React.Component {
  constructor(props){
    super(props);
    this.state = {data : ''}
    this.graph = this.graph.bind(this);
    this.getData(this.props.item);
  }

  getData(item){
    axios.get("http://127.0.0.1:5000/"+item)
    .then(response => this.setState({'data' : response.data}))
  }

  graph (item) {
    const data = [this.state.data];
    if (data != '') {
      if (item == "Humidity") {
        return (
          <div className="container" key={this.props.data}>
          <ResponsiveLine
                  data={data}
                  margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
                  xScale={{ type: 'point' }}
                  yScale={{ type: 'linear', stacked: true, min: 'auto', max: 'auto' }}
                  axisTop={null}
                  axisRight={null}
                  axisBottom={null}
                  axisLeft={{
                      orient: 'left',
                      tickSize: 5,
                      tickPadding: 5,
                      tickRotation: 0,
                      legend: 'Humidity',
                      legendOffset: -40,
                      legendPosition: 'middle'
                  }}
                  colors={{ scheme: 'nivo' }}
                  pointSize={10}
                  pointColor={{ theme: 'background' }}
                  pointBorderWidth={2}
                  pointBorderColor={{ from: 'serieColor' }}
                  pointLabel="y"
                  pointLabelYOffset={-12}
                  useMesh={true}
              /></div>
        )
      }
      if (item == "Temperature") {
        const data = [this.state.data];
        return (
          <div key={this.props.data} className="container" >
          <ResponsiveLine
                  data={data}
                  margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
                  xScale={{ type: 'point' }}
                  yScale={{ type: 'linear', min: 'auto', max: 'auto' }}
                  axisTop={null}
                  axisRight={null}
                  axisBottom={null}
                  axisLeft={{
                      orient: 'left',
                      tickSize: 5,
                      tickPadding: 5,
                      tickRotation: 0,
                      legend: 'Temperature',
                      legendOffset: -40,
                      legendPosition: 'middle'
                  }}
                  colors={{ scheme: 'nivo' }}
                  pointSize={10}
                  pointColor={{ theme: 'background' }}
                  pointBorderWidth={2}
                  pointBorderColor={{ from: 'serieColor' }}
                  pointLabel="y"
                  pointLabelYOffset={-12}
                  useMesh={true}
              /></div>);
      }
      if (item == "Spectrum") {
        const data = [this.state.data];
        return (
          <div className="container" key={this.props.data}>
          <ResponsiveLine
                  data={data}
                  margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
                  xScale={{ type: 'point' }}
                  yScale={{ type: 'linear', stacked: true, min: 'auto', max: 'auto' }}
                  axisTop={null}
                  axisRight={null}
                  axisBottom={null}
                  axisLeft={{
                      orient: 'left',
                      tickSize: 5,
                      tickPadding: 5,
                      tickRotation: 0,
                      legend: 'Humidity',
                      legendOffset: -40,
                      legendPosition: 'middle'
                  }}
                  pointSize={10}
                  pointColor={{ theme: 'background' }}
                  pointBorderWidth={2}
                  pointBorderColor={{ from: 'serieColor' }}
                  pointLabel="y"
                  pointLabelYOffset={-12}
                  useMesh={true}
              /></div>
        )
      }
  }else {
  return (<div>Loading Graph...</div>);
}
}

  render () {
    const graph = <Container>{this.graph(this.props.item)}</Container>;
    return graph;
  }
}

export default Graph;
