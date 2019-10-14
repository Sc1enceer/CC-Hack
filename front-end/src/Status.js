import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import { makeStyles } from '@material-ui/core/styles';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import React from 'react';

const useStyles = makeStyles({
  poor: {
    background: 'linear-gradient(45deg,rgb(205,92,92) 30%,#FFA07A 90%)',
    borderRadius: 3,
    border: 0,
    color: 'white',
    boxShadow: '0 3px 5px 2px rgba(255, 105, 135, 0.3)'
  },
  good: {
    background: 'linear-gradient(45deg,#32CD32  30%, #7FFF00 90%)',
    borderRadius: 3,
    border: 0,
    color: 'white',
    boxShadow: '0 3px 5px 2px rgba(50,205,50,0.3)'
  },
  night : {
    background: 'linear-gradient(45deg, rgb(105,105,105) 30%, rgb(220,220,220) 90%)',
    borderRadius: 3,
    border: 0,
    color: 'white',
    boxShadow: '0 3px 5px 2px rgba(211,211,211,0.3)'
  },
  light : {
    background: 'linear-gradient(45deg, rgb(240,230,140) 30%, rgb(255,255,224) 90%)',
    borderRadius: 3,
    border: 0,
    color: 'white',
    boxShadow: '0 3px 5px 2px rgba(255,228,181,0.3)',
    marginTop: '1vh'
  }
});

function Status(props){
  const item = props.item;
  const data = props.data;

// call to flask to request the data. return Json file

  const classes = useStyles();
  const unit = {"Sunlight":"Φ", "Humidity":"%", "Temperature":"°C", "Wind Speed":"m/s", "Spectrum" : " "}
  const exceedThreshold = props.exceedThreshold;

  function checkClass(item) {
    if (item == "Sunlight") {
      return classes.night;
    }else if (item == "Spectrum") {
      return classes.light;
    }else {
      return exceedThreshold? classes.good : classes.poor;
    }
  }

  return (
    <Card className={checkClass(item)}>
      <CardContent>
        <Typography variant="h4" align="center">
          {item}
        </Typography>
        <Typography variant="h3" align="center">
          {data}{unit[item]}
        </Typography>
      </CardContent>
    </Card>
 );
}

// <CardActions>
//   <Button size="small">Learn More</Button>
// </CardActions>
export default Status;
