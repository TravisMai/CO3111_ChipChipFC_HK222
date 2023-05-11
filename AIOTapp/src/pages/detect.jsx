import React, { useState, useEffect } from 'react';
import { Page, Navbar, List, ListItem, Block, Button, useStore, BlockTitle,
  Card,
  CardHeader,
  CardContent, } from 'framework7-react';


const DetectPage = () => {
  const linkApi = 'https://io.adafruit.com/api/v2/ChipchipFC/groups/default';
  const keyChip = 'aio_NCVK09W8FmQYLTfFBC8PYLEJwQjS';
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(linkApi, {
          headers: {
            'X-AIO-Key': keyChip
            //aio_jwjT59maC5PDDYyK5tgy3GOrnBjy Nghiakey
            //aio_Ysia79rQha42BqRwEiLZNuuBgkAK
            //https://io.adafruit.com/api/v2/EmChes/groups/default
            //https://io.adafruit.com/api/v2/phudinh153/groups/default
          }
        });
        const data = await response.json();
        setData(data);
        //console.log(data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
    const intervalId = setInterval(fetchData, 10000);

    return () => clearInterval(intervalId);
  }, []);

  let pic = 'https://user-images.githubusercontent.com/26833433/127574988-6a558aa1-d268-44b9-bf6b-62d4c605cc72.jpg';

  if (!data || !data.feeds) {
    return null; 
  }
  function getBase64Img(pic) {
    pic = 'data:image/png;base64,' + pic;
    //console.log(pic);
    return pic;
    }
  if(data.feeds[2].last_value){
    pic = getBase64Img(data.feeds[2].last_value);
  }

  let ai = data.feeds[0]?.last_value

  const cardStyle = {
    height: '70%',
    width: '80%',
    color: 'red',
    marginLeft: '10px',
  };
  


  const blockTitle = {
    fontSize: '22px',
    marginBottom: '35px',
    padding: '3px',
  };

  return (
    <Page name="Detect"> 
      <BlockTitle style={blockTitle}>Detect</BlockTitle>
        <Block style={{display: 'flex', flexDirection: 'row', justifyContent: 'center'}}>
          <img src={pic} style={cardStyle}></img>
       </Block>  
       <Block>
       <List>
            <ListItem>
              <Card style={cardStyle}>
                <CardHeader>Result: {ai}</CardHeader>
              </Card>
            </ListItem>
    
          </List>
        </Block>  
    </Page>
  );
};

export default DetectPage;


