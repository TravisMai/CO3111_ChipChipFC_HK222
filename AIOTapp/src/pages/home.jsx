import React from 'react';
import {
  Page,
  Block,
  BlockTitle,
  List,
  ListItem,
  Card,
  CardHeader,
  CardContent,
  CardFooter,

} from 'framework7-react';
import { useState, useEffect } from 'react';

const HomePage = () => {
  // Here you could fetch data from a backend API or from a local store
  // and set it to state or props to pass it to the different components below
  let temperature = 25;
  let humidity = 60;
  let light = 800;
  let anotherMetric = 1234;

  const [data, setData] = useState([]);
  useEffect(() => {
    fetch("https://io.adafruit.com/api/v2/phudinh153/feeds/cambien1")
      .then((response) => response.json())
      .then((data) => {
      setData(data);
      console.log(data);
    })
      
      .catch((error) => console.error(error));
  }, []);
  temperature = data.last_value;
  const cardStyle = {
    height: '90%',
    width: '80%',
  };

  const blockTitle = {
    fontSize: '22px',
    marginBottom: '5px',
    padding: '3px',
  };

  return (
    <Page>
      <BlockTitle style={blockTitle}>Metrics</BlockTitle>
    
       
          <List>
            <ListItem>
              <Card style={cardStyle}>
                <CardHeader>Temperature</CardHeader>
                <CardContent>{temperature} &#8451;</CardContent>
                <CardFooter>Updated 2 minutes ago</CardFooter>
              </Card>
              <Card style={cardStyle}>
                <CardHeader>Humidity</CardHeader>
                <CardContent>{humidity} %</CardContent>
                <CardFooter>Updated 2 minutes ago</CardFooter>
              </Card>
            </ListItem>
    
          </List>
       
        
          <List>
            <ListItem>
              <Card style={cardStyle}>
                <CardHeader>Light</CardHeader>
                <CardContent>{light} lux</CardContent>
                <CardFooter>Updated 2 minutes ago</CardFooter>
              </Card>
              <Card style={cardStyle}>
                <CardHeader>Another Metric</CardHeader>
                <CardContent>{anotherMetric}</CardContent>
                <CardFooter>Updated 2 minutes ago</CardFooter>
              </Card>
            </ListItem>
          </List>
      
    </Page>
  );
};

export default HomePage;
