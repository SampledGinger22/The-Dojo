import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import ListForm from './components/ListForm';
import DisplayToDos from './components/ListItems';

function App() {

  const [ListItem, setListItem] = useState([]);

  const pushItem = (todoItem) => {
    setListItem([...ListItem, todoItem]);
  }

  const Delete = (index) => {
    const filteredList = ListItem.filter((todo, i) => {
      return i !== index;
    });
    setListItem(filteredList);
  }

  return (
    <div className="App">
      <ListForm onNewItem={ pushItem }/>
      { ListItem.map( (todoItem, i) =>
          <DisplayToDos todoItem={ todoItem } onDeletion={ Delete } idx={ i } key={i}/> 
        ) }
    </div>
  );
}

export default App;
