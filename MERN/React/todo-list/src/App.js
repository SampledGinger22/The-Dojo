import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import ListForm from './components/ListForm';
import DisplayToDos from './components/ListItems';

function App() {

  const [ListItem, setListItem] = useState([]);

  const handleSubmit = (e, Item) => {
    e.preventDefault();

    if(Item.length !== 0){
      const todoItem = {
        text: Item,
        complete: false
      }
      console.log(todoItem);
      setListItem([...ListItem, todoItem]);
      console.log(ListItem);
      e.target.reset();
    }
    e.target.reset();
    return;
  }

  const handleCompleteChange = (index) => {
    const updatedItem = ListItem.map((todo, i) => {
      if(index == i){
        todo.complete = !todo.complete;
      }
      
      return todo;
    });
  }


  const Delete = (index) => {
    const filteredList = ListItem.filter((todo, i) => {
      return i !== index;
    });
    setListItem(filteredList);
  }

  return (
    <div className="App">
      <ListForm handleSubmit={ handleSubmit }/>
      { ListItem.map( (todoItem, i) =>
        <div className='flexrow'> 
          <DisplayToDos todoItem={ todoItem } key={i}/> 
        </div>
        ) }
    </div>
  );
}

export default App;
