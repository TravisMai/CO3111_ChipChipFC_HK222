import React from 'react';
import {
  Page,
  Navbar,
  List,
  ListInput,
  ListItem,
  Toggle,
  BlockTitle,
  Button,
  Range,
  Block,
} from 'framework7-react';

const SettingsPage = () => (
  <Page name="settings">
    <Navbar title="Settings" />

    <BlockTitle>User</BlockTitle>
    <List strongIos outlineIos dividersIos>
      <ListInput label="Name" type="text" placeholder="Your name"></ListInput>

      <ListInput label="E-mail" type="email" placeholder="E-mail"></ListInput>

      <ListInput label="Password" type="password" placeholder="Password"></ListInput>

      <ListInput label="Phone" type="tel" placeholder="Phone"></ListInput>

      <ListInput label="Gender" type="select">
        <option>Male</option>
        <option>Female</option>
      </ListInput>

      <ListInput
        label="Birth date"
        type="date"
        placeholder="Birth day"
        defaultValue="2014-04-30"
      ></ListInput>


      <ListInput type="textarea" label="Textarea" placeholder="Bio"></ListInput>
      <ListInput type="textarea" label="Resizable" placeholder="Bio" resizable></ListInput>
    </List>


  </Page>
);

export default SettingsPage;
