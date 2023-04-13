import React from 'react';
import { Page, Navbar, List, ListItem, Block, Button, useStore, BlockTitle } from 'framework7-react';


const DetectPage = () => {

  const cardStyle = {
    height: '90%',
    width: '80%',
  };
  const pic = 'https://user-images.githubusercontent.com/26833433/127574988-6a558aa1-d268-44b9-bf6b-62d4c605cc72.jpg';

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


