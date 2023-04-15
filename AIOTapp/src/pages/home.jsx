import React, { useState, useEffect } from 'react';
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

const HomePage = () => {
  // Here you could fetch data from a backend API or from a local store
  // and set it to state or props to pass it to the different components below

  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`https://io.adafruit.com/api/v2/phudinh153/groups/default`, {
          headers: {
            'X-AIO-Key': 'aio_Ysia79rQha42BqRwEiLZNuuBgkAK'
          }
        });
        const data = await response.json();
        setData(data);
        console.log(data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
    const intervalId = setInterval(fetchData, 10000);

    return () => clearInterval(intervalId);
  }, []);

  if (!data || !data.feeds) {
    return null; 
  }

  let temperature = data.feeds[1].last_value;
  let humidity = data.feeds[2].last_value;
  let light = data.feeds[3].last_value;
  let anotherMetric = 1234;

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
                <CardFooter>Updated 10 seconds ago</CardFooter>
              </Card>
              <Card style={cardStyle}>
                <CardHeader>Humidity</CardHeader>
                <CardContent>{humidity} %</CardContent>
                <CardFooter>Updated 10 seconds ago</CardFooter>
              </Card>
            </ListItem>
    
          </List>
       
        
          <List>
            <ListItem>
              <Card style={cardStyle}>
                <CardHeader>Light</CardHeader>
                <CardContent>{light} lux</CardContent>
                <CardFooter>Updated 10 seconds ago</CardFooter>
              </Card>
              <Card style={cardStyle}>
                <CardHeader>Another Metric</CardHeader>
                <CardContent>{anotherMetric}</CardContent>
                <CardFooter>Updated 10 seconds ago</CardFooter>
              </Card>
            </ListItem>
          </List>
      
    </Page>
  );
};

export default HomePage;
