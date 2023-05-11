import React, { useState, useEffect, useRef }from 'react';
import {
  Page,
  Block,
  BlockTitle,
  List,
  ListItem,
  Card,
  CardHeader,
  CardContent,
  Button,
  Segmented,
  Toggle,
} from 'framework7-react';

const HomePage = () => {
 
  const linkApi = 'https://io.adafruit.com/api/v2/ChipchipFC/groups/default';
  const keyChip = 'aio_icAv95gUHiLlsxtbcYTyd42KlFJL';
  const [data, setData] = useState({});
  let [toggleState, setToggleState] = useState(0);
  // let [button, setButtonState] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(linkApi, {
          headers: {
            'X-AIO-Key': keyChip
            //aio_Glir96FKcj9POyTAR0udNa5ADxC6
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

    const intervalId = setInterval(fetchData, 5000);
    // if(tog != toggleState){
    //   fetchData()
    // }
    // Connect to Adafruit server and subscribe to updates
    //https://io.adafruit.com/api/v2/webhooks/feed/9e6nKi5oamr3MaWSJid8goaoCnkw
    //wss://io.adafruit.com/api/v2/phudinh153/feeds/nutnhan1
    //wws://io.adafruit.com/api/v2/webhooks/feed/8vkm4212ErmQT6y1kturLb1dnvzc
    const connection = new WebSocket('wss://io.adafruit.com/api/v2/webhooks/feed/8vkm4212ErmQT6y1kturLb1dnvzc/notify');
    connection.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log('websocket')
      console.log(data);
    };

    return () => {
      clearInterval(intervalId);
      setData(null);
    };
  }, []);

  if (!data || !data.feeds) {
    return null; 
  }

  let temperature = data.feeds[6]?.last_value;
  let humidity = data.feeds[1]?.last_value;
  let light = data.feeds[3]?.last_value;
  let tog = parseInt(data.feeds[4]?.last_value);
  if(tog !== toggleState){
    toggleState = tog;
  }
  console.log(typeof tog);
  console.log("Update: "+ tog);
  
  const fetchButton = async () => {
    try {
      const response = await fetch(linkApi, {
        headers: {
          'X-AIO-Key': keyChip
          //aio_Glir96FKcj9POyTAR0udNa5ADxC6
          //aio_jwjT59maC5PDDYyK5tgy3GOrnBjy Nghiakey
          //aio_Ysia79rQha42BqRwEiLZNuuBgkAK
          //https://io.adafruit.com/api/v2/EmChes/groups/default
          //https://io.adafruit.com/api/v2/phudinh153/groups/default
        }
      });
      const data = await response.json();
      setData(data);
      setToggleState(parseInt(data.feeds[4]?.last_value));
      console.log(data);
      
    } catch (error) {
      console.error(error);
    }
  };

  let moisture = 60;
  // let temperature = data.feeds[7].last_value;
  // let humidity = data.feeds[1].last_value;
  // let light = data.feeds[3].last_value;
  // let moisture = 60;


  const blockTitle = {
    fontSize: '22px',
    marginBottom: '5px',
    padding: '3px',
  };

  const cardStyle = {
    height: '90%',
    width: '80%',
  };

  let tempStyle = {
    ...cardStyle
  };
  let tempWarning = 'Normal';
  
  if(temperature < 20){
    tempStyle = {
      ...cardStyle,
      color: 'white',
      backgroundColor: '#52B1D2',
    };
    tempWarning = 'Cold'
  }
  else if(temperature >= 20 && temperature < 35){
    tempStyle = {
      ...cardStyle,
      color: 'gray',
      backgroundColor: 'yellow',
    };
  }
  else if(temperature >= 35 && temperature < 50){
    tempStyle = {
      ...cardStyle,
      color: 'red',
      backgroundColor: 'yellow',
    };
    tempWarning = 'Hot'
  }
  else if(temperature >= 50){
    tempStyle = {
      ...cardStyle,
      color: 'white',
      backgroundColor: 'red',
      border: '2px solid',
      borderColor: 'red'
    };
    tempWarning = 'Too Hot'
  }

  let humStyle = {
    ...cardStyle
  }; 
  
  let humWarning = 'Normal';

  if(humidity < 20){
    humStyle = {
      ...cardStyle,
      color: 'red',
      backgroundColor: '#05192C',
      border: '3px solid',
      //borderColor: 'red'
    };
    humWarning = 'Too Dry'
  }
  else if(humidity >= 20 && humidity < 40){
    humStyle = {
      ...cardStyle,
      color: 'red',
      backgroundColor: '#D0AE8B',
      border: '3px solid',
      borderColor: 'red'
    };
    humWarning = 'Dry'
  }
  else if(humidity >= 40 && humidity < 60){
    humStyle = {
      ...cardStyle,
      color: 'white',
      backgroundColor: '#E8E4E2',
    };
  }
  else if(humidity >= 60 && humidity < 90){
    humStyle = {
      ...cardStyle,
      color: 'white',
      backgroundColor: '#73CCD8',
    };
  }
  else if(humidity >= 90){
    humStyle = {
      ...cardStyle,
      color: 'red',
      backgroundColor: '#52B1D2',
      border: '3px solid',
      borderColor: 'red'
    };
    humWarning = 'Wet'
  }

  let lightStyle = {
    ...cardStyle
  }; 

  let lightWarning = 'Normal'

  if(light < 100){
    lightStyle = {
      ...cardStyle,
      color: 'white',
      backgroundColor: '#D14009',
    };
    lightWarning = 'Well-lighted'
  }
  else if(light >= 100 && light < 200){
    lightStyle = {
      ...cardStyle,
      color: 'white',
      backgroundColor: '#FFCC33',
    };
  }
  else if(light >= 200 && light < 300){
    lightStyle = {
      ...cardStyle,
      color: 'gray',
      backgroundColor: '#FFE484',
    };
    lightWarning = 'Bright'
  }
  else if(light >= 300){
    lightStyle = {
      ...cardStyle,
      color: 'red',
      backgroundColor: '#FFFFFF',
      border: '3px solid',
    };
    lightWarning = 'Too Bright'
  }

  let moiStyle = {
    ...cardStyle
  }

  let moiWarning = 'Normal';

  if(moisture < 20){
    moiStyle = {
      ...cardStyle,
      color: 'red',
      backgroundColor: '#483226',
      border: '3px solid',
      //borderColor: 'red'
    };
    moiWarning = 'Too Dry'
  }
  else if(moisture >= 20 && moisture < 40){
    moiStyle = {
      ...cardStyle,
      color: 'red',
      backgroundColor: '#604832',
      border: '3px solid',
      borderColor: 'red'
    };
    moiWarning = 'Dry'
  }
  else if(moisture >= 40 && moisture < 60){
    moiStyle = {
      ...cardStyle,
      color: 'gray',
      backgroundColor: '#D4F1FA',
    };
  }
  else if(moisture >= 60 && moisture < 75){
    moiStyle = {
      ...cardStyle,
      color: 'white',
      backgroundColor: '#A4F4F9',
    };
  }
  else if(moisture >= 75){
    moiStyle = {
      ...cardStyle,
      color: 'red',
      backgroundColor: '#7CEAF9',
      border: '3px solid',
      borderColor: 'red'
    };
    moiWarning = 'Wet'
  } 

  const butStyle = {
    fontSize: '22px',
    marginBottom: '10px',
    padding: '3px',
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
  };



let button = toggleState;
const handleToggleChange = (value) => {
  button = parseInt(value);
  const data = {
    "value": value
  };
  fetch('https://io.adafruit.com/api/v2/webhooks/feed/8vkm4212ErmQT6y1kturLb1dnvzc', {
    method: 'POST',
    headers: {
      'X-AIO-Key': keyChip,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => {
    console.log(response);
    setToggleState(value);
    fetchButton();
  })
  .catch(error => {
    console.error(error);
  });
  

}

  let pumpTitle = {
    display: 'flex',
    justifyContent: 'center',
    width: '100%',
    color: '#005BC1',
    fontWeight: '600',
    fontSize: '25px',

  }
  let buttonStyle = {
    display: 'flex',
    justifyContent: 'center',
    width: '95%',
  };

  let toggleStyle = {
    display: 'flex',
    justifyContent: 'center',
    width: '100%',
    marginLeft: '20%',
    border: '2px solid',
    borderColor: '#005BC1',
    borderRadius: '15px',
  };

  // let pumpTitle{
  //   display: 'flex',
  //   justifyContent: 'center',
  //   width: '80%',
  // };

  return (
    <Page>
      <BlockTitle style={blockTitle}>Metrics</BlockTitle>
    
       
          <List>
            <ListItem>
              <Card style={tempStyle}>
                <CardHeader>Temp</CardHeader>
                <CardContent>{temperature} &#8451;</CardContent>
                <CardContent>Status: {tempWarning}</CardContent>
              </Card>
              <Card style={humStyle}>
                <CardHeader>Humidity</CardHeader>
                <CardContent>{humidity} %</CardContent>
                <CardContent>Status: {humWarning}</CardContent>
              </Card>
              
            </ListItem>
    
          </List>
       
        
          <List>
            <ListItem>
              <Card style={lightStyle}>
                <CardHeader>Light</CardHeader>
                <CardContent>{light} lux</CardContent>
                <CardContent> Status: {lightWarning}</CardContent>
              </Card>
              <Card style={moiStyle}>
                <CardHeader>Moisture</CardHeader>
                <CardContent>{moisture}</CardContent>
                <CardContent>Status: {moiWarning}</CardContent>
              </Card>
            </ListItem>
          </List>

          
          {/* <Block strong>
          <BlockTitle style={butStyle}>Pump</BlockTitle>
          <div class="segmented">
            <a class="button button-active onBut">ON</a>
            <a class="button offBut">OFF</a>
          </div>
          </Block> */}

          {/* <List simpleList strong outlineIos dividersIos>
            <ListItem title="Pump" style={{ fontSize: "20px", color: "#005BC1", fontWeight: "600" }}>
              <Toggle slot="after" defaultChecked={tog} onChange={handleToggleChange} />
            </ListItem>
          </List> */}

          <List style={buttonStyle}>
          <Segmented style={pumpTitle}>Pump</Segmented>
          <Segmented style={toggleStyle}>
            <Button onClick={() => handleToggleChange(1)}  className={(button) ? 'button-active' : ''}>
              ON
            </Button>
            <Button onClick={() => handleToggleChange(0)} className={!(button) ? 'button-active' : ''}>
              OFF
            </Button>
          </Segmented>
          </List>
          
    </Page>
  );
};

export default HomePage;
