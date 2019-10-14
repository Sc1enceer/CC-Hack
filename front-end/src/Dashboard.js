
import {Container, Grid, Typography} from '@material-ui/core'
import React from 'react';
import Statusbar from './Statusbar';

class Dashboard extends React.Component {
  constructor(props) {
    super(props);
    // this.state = {data: };
  }

  render(){
    return (
      <Container maxWidth="lg">
        <Grid container spacing = {3}>
          <Grid item xs = {12}>
            <Typography variant="h2" align = "center">Plant Health Monitoring</Typography>
          </Grid>
          <Statusbar/>
        </Grid>
      </Container>
    )
  }
}

export default Dashboard;
