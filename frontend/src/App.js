import React from 'react';
import {Title } from './Title';
import { TournamentName } from './TournamentName';
import { Totalplayers } from './TotalPlayers';
import { Seed } from './Seed';
import { Createbuttom } from './CreateButtom';
//import './App.css';



function App() {
  return (
    <React.fragment>

      <Title/>

      <TournamentName/>

      <TotalPlayers/>

      <Seed/>

      <playersBox/>

      <Createbuttom/>

    </React.fragment>
 
  );
}

export default App;
