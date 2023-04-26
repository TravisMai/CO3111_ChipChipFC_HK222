import React, { useState, useEffect } from 'react';
import { Page, Navbar, List, ListItem, Block, Button, useStore, BlockTitle } from 'framework7-react';


const DetectPage = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`https://io.adafruit.com/api/v2/EmChes/groups/default`, {
          headers: {
            'X-AIO-Key': 'aio_jwjT59maC5PDDYyK5tgy3GOrnBjy'
            //aio_jwjT59maC5PDDYyK5tgy3GOrnBjy Nghiakey
            //aio_Ysia79rQha42BqRwEiLZNuuBgkAK
            //https://io.adafruit.com/api/v2/EmChes/groups/default
            //https://io.adafruit.com/api/v2/phudinh153/groups/default
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
    const intervalId = setInterval(fetchData, 20000);

    return () => clearInterval(intervalId);
  }, []);

  let pic = 'https://user-images.githubusercontent.com/26833433/127574988-6a558aa1-d268-44b9-bf6b-62d4c605cc72.jpg';

  if (!data || !data.feeds) {
    return null; 
  }
  if(data.feeds[2].last_value){
    pic = data.feeds[2].last_value
  }
  const cardStyle = {
    height: '90%',
    width: '80%',
  };
  


  const blockTitle = {
    fontSize: '22px',
    marginBottom: '35px',
    padding: '3px',
  };

  return (
    <Page name="Detect"> 
      <BlockTitle style={blockTitle}>Detect</BlockTitle>
        <Block>
          <img src={pic} style={cardStyle}></img>
       </Block>    
    </Page>
  );
};

export default DetectPage;


